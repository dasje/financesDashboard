import os

SECRET_KEY = os.environ.get("SECRET_KEY", "")
ALGORITHM = os.environ.get("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

POSTGRES_USER = os.getenv('POSTGRES_USER', "postgres")
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', "admin")
POSTGRES_SERVICE_NAME = os.getenv('POSTGRES_SERVICE_NAME', "postgres")
POSTGRES_PORT = os.getenv('DB_PORT', 5432)
POSTGRES_DB_NAME = os.getenv('POSTGRES_DB', "fd_db")