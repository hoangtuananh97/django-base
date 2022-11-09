# App

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy app

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

### Celery

This app comes with Celery.

To run a celery worker:

```bash
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

### Create i18n
    $ python manage.py makemessages --all
    $ python manage.py compilemessages

### Generate your schema docs with the CLI:

    $ ./manage.py spectacular --file schema.yml
    $ docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui

### Remove expired token jwt
    $ python manage.py flushexpiredtokens
### Run pre-commit before commit (Can setup pre-commit of git)
    $ pre-commit run --all-files
    $ pre-commit run --files <dir of file>
## Deployment

The following details how to deploy this application.
