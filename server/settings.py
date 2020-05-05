from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: str = "true"
    DB_USER: str = "yapki"
    DB_USER_PWD: str = "yapki"
    DB_HOST: str = "localhost"
    DB_NAME: str = "yapki"
    DB_TYPE: str = "mysql+pymysql"
    JWT_SECRET: str = None
    sqlalchemy_url: str = None
    # sqlalchemy_url: str = "postgresql://user:password@postgresserver/db"
    access_token_expire_minutes: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

    class Config:
        env_file = ".env"


settings = Settings()

if settings.sqlalchemy_url is None:
    settings.sqlalchemy_url = settings.DB_TYPE + '://' + settings.DB_USER + ':' + settings.DB_USER_PWD + '@' + settings.DB_HOST + '/' + settings.DB_NAME