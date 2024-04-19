# Dev - WIP

Before building images, be sure to create .env file in the root folder and the folders for the services that will be built.
To run Dev env, navigate to root folder of project and run 'docker compose up'.

## Env - Root folder

In order to build the postgres service, an .env file with the following variables is required:
POSTGRES_PASSWORD
POSTGRES_DB
PGADMIN_DEFAULT_EMAIL
PGADMIN_DEFAULT_PASSWORD

## Back end

### FastAPI

#### Endpoints

- /sign_up [email, password]
- /login [email, password]

## Database

This project uses a containerized Postgres database. It is being developed without an attached persistant volume to prevent accidental retention of developer data when testing with bank API's.

### Models

users
|column|type|description|
|---|---|---|
| | | |
| | | |
| | | |
