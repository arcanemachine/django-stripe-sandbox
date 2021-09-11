# django-stripe-sandbox

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
  - Running tests
    - To run unit tests
      - in the Django project folder, with virtualenv activated, run `python3 manage.py test`.
    - To run e2e tests
      - From the project's root folder, run `npm install`.
      - Install [Cypress](https://docs.cypress.io/guides/getting-started/installing-cypress) (make sure to install [any required dependencies](https://docs.cypress.io/guides/getting-started/installing-cypress) as well)
      - In the Django project folder, run `npm run cypress`.

- (optional) You can generate a new secret key from the Django shell (`manage.py shell`) and set it as the `SECRET_KEY` in `settings.py`:
`from django.core.management import utils
    print(utils.get_random_secret_key())`

- Run `manage.py migrate` to generate a database.
- Run `manage.py runserver` to start the development server
