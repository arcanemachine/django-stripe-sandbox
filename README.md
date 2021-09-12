# django-stripe-sandbox

![Coverage Badge](/static/img/coverage.svg "Coverage Badge")

This project shows how to use and test Stripe functionality.

Examples include: Create PaymentIntent, PaymentMethod...

## Setup Instructions

- Create a virtualenv and install the required dependencies
  - Using [Poetry](https://python-poetry.org/docs/) (recommended):
    - Create a virtualenv and install the required dependencies
      - Dev/Testing environment: `poetry install`
      - Production environment: `poetry install --no-dev`
    - Activate the virtualenv
      - `poetry shell`
  - Using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):
    - Create a new virtualenv
      - `mkvirtualenv django-stripe-sandbox`
    - Activate the virtualenv
      - `workon django-stripe-sandbox`
    - From the project's root folder, install the required dependencies
      - `pip install -r requirements.txt`
    - generate a database
      - Run `python manage.py migrate` to generate a database.
    - start the server
      - Run `python manage.py runserver` to start the development server
      - (optional) You can generate a new secret key from the Django shell (`python manage.py shell`) and set it as the `SECRET_KEY` in `settings.py`:
        `from django.core.management import utils`
        `print(utils.get_random_secret_key())`
  - Running tests
    - To run unit tests
      - ensure the virtualenv is activated
      - in the Django project folder run `python manage.py test`.
    - To run E2E tests
      - ensure the virtualenv is activated
        - to avoid polluting the database, use `manage.py` to run a test server that will create its own database
          - either execute `scripts/runserver-test.sh`
          - or, use `manage.py`'s `testserver` command to specify your own settings, e.g.:
            - `python manage.py testserver --addrport 0.0.0.0:7000 cypress/fixtures/empty.json`
      - Ensure [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) is installed (If not already installed, I recommend using [nvm](https://github.com/nvm-sh/nvm#installing-and-updating) instead to more easily manage npm versions)
      - From the project's root folder, run `npm install`.
      - Install [Cypress](https://docs.cypress.io/guides/getting-started/installing-cypress) (make sure to install [any required dependencies](https://docs.cypress.io/guides/getting-started/installing-cypress) as well)
      - In the Django project folder, run `npm run cypress`.
