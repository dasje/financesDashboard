# Dev
## Env
Add a .env file with the following keys:
+ POSTGRES_PASSWORD: default "admin"
+ POSTGRES_DB: default "fd_db"
+ PGADMIN_DEFAULT_EMAIL
+ PGADMIN_DEFAULT_PASSWORD: default "admin"
+ POSTGRES_USER: default "postgres"
+ POSTGRES_SERVICE_NAME: default "postgres"
+ DB_PORT: default 5432
+ SECRET_KEY: generate with openssl "openssql ran -hex 32"
+ ALGORITHM: "HS256"
+ ACCESS_TOKEN_EXPIRE_MINUTES: default 30

## Endpoints
- /sign_up [email, password]
- /login [email, password]