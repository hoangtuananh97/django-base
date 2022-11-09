import psycopg2
import pytest
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def run_sql(sql):
    conn = psycopg2.connect(database="postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


@pytest.fixture(scope="session")
def django_db_setup(django_db_blocker, django_db_keepdb=True) -> None:
    yield
    # if env.bool("RUN_TEST", default=False):
    #     from django.conf import settings
    #
    #     database_name = "postgres"
    #     user_name = "jpox_test_user"
    #     password = "jpox_test_pw"
    #     settings.DATABASES["default"]["NAME"] = database_name
    #     settings.DATABASES["default"]["USER"] = user_name
    #     settings.DATABASES["default"]["PASSWORD"] = password
    #
    #     # run_sql(f"DROP DATABASE IF EXISTS {database_name}")
    #     # run_sql(f"-- CREATE DATABASE {database_name} IF NOT EXISTS {database_name}")
    #     # run_sql("DROP extension IF EXISTS dblink")
    #     # run_sql(
    #     #     f"""
    #     # DO
    #     # $do$
    #     # BEGIN
    #     #    IF EXISTS (SELECT FROM pg_database WHERE datname = '{database_name}') THEN
    #     #       RAISE NOTICE 'Database already exists';  -- optional
    #     #    ELSE
    #     #       CREATE extension dblink;
    #     #       PERFORM dblink_exec('dbname=' || current_database()  -- current db
    #     #                         , 'CREATE DATABASE {database_name}');
    #     #    END IF;
    #     # END
    #     # $do$;
    #     # """
    #     # )
    #     run_sql(
    #         f"""
    #     DO
    #         $do$
    #         BEGIN
    #            IF EXISTS (
    #               SELECT FROM pg_catalog.pg_roles
    #               WHERE  rolname = '{user_name}') THEN
    #               RAISE NOTICE 'Role "{user_name}" already exists. Skipping.';
    #            ELSE
    #               CREATE ROLE {user_name} LOGIN PASSWORD '{password}';
    #               ALTER USER {user_name} CREATEDB;
    #               GRANT ALL PRIVILEGES ON DATABASE {database_name} TO {user_name};
    #            END IF;
    #         END
    #     $do$;
    #     """
    #     )
    #
    #     with django_db_blocker.unblock():
    #         call_command("migrate", "--noinput")
    #     yield
    #     for connection in connections.all():
    #         connection.close()
    #
    #     # run_sql(f"DROP DATABASE {database_name}")
    # else:
    #     yield


pytest_plugins = [
    "app.tests.fixtures",
    "app.core.tests.fixtures",
]
