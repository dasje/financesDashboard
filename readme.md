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
- /login form-data{email, password}

## Database

This project uses a containerized Postgres database. It is being developed without an attached persistant volume to prevent accidental retention of developer data when testing with bank API's.

### Models

#### users

| column          | type    | description                    |
| --------------- | ------- | ------------------------------ |
| id              | uuid    | unique id                      |
| email           | string  | user email                     |
| hashed_password | string  | user password stored as a hash |
| sign_up_date    | date    | sign up date                   |
| active          | boolean | is the account active?         |

#### auth

| column                 | type     | description                                        |
| ---------------------- | -------- | -------------------------------------------------- |
| id                     | uuid     | unique id                                          |
| user_id                | uuid     | foreign key with users table                       |
| auth_token             | string   | authentication token logged in with                |
| login_datetime         | datetime | login datetime                                     |
| auto_logout_datetime   | datetime | datetime on which user is automatically logged out |
| actual_logout_datetime | datetime | datetime on which user logged out                  |
| active                 | boolean  | user status                                        |

#### uploads

| column          | type     | description                             |
| --------------- | -------- | --------------------------------------- |
| id              | uuid     | unique id                               |
| user_id         | uuid     | foreign key with users table            |
| filename        | string   | name of file at upload (with extension) |
| upload_datetime | datetime | datetime of file upload                 |
