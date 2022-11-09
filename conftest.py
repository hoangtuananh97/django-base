import psycopg2
import pytest
from django.core.management import call_command
from django.db import connections
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def run_sql(sql):
    conn = psycopg2.connect(database="postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


@pytest.fixture(scope="session")
def django_db_setup(django_db_blocker, django_db_keepdb=True) -> None:
    from django.conf import settings
    database_name = "jpox_test_db"
    user_name = "jpox_test_user"
    password = "jpox_test_pw"
    settings.DATABASES["default"]["NAME"] = database_name
    settings.DATABASES["default"]["USER"] = user_name
    settings.DATABASES["default"]["PASSWORD"] = password

    run_sql(f"DROP DATABASE IF EXISTS {database_name}")
    run_sql(f"CREATE DATABASE {database_name}")
    run_sql(f"""
    DO
        $do$
        BEGIN
           IF EXISTS (
              SELECT FROM pg_catalog.pg_roles
              WHERE  rolname = '{user_name}') THEN

              RAISE NOTICE 'Role "{user_name}" already exists. Skipping.';
           ELSE
              CREATE ROLE {user_name} LOGIN PASSWORD '{password}';
              ALTER USER {user_name} CREATEDB;
              GRANT ALL PRIVILEGES ON DATABASE {database_name} TO {user_name};
           END IF;
        END
    $do$;
    """)

    with django_db_blocker.unblock():
        call_command("migrate", "--noinput")
    yield
    for connection in connections.all():
        connection.close()

    run_sql(f"DROP DATABASE {database_name}")


pytest_plugins = [
    "app.tests.fixtures",
    "app.core.tests.fixtures",
]
