from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: str
    db_user: str
    db_user_pwd: str
    db_host: str
    db_name: str
    db_type: str
    jwt_secret: str
    sqlalchemy_url: str
    # sqlalchemy_url: str = "postgresql://user:password@postgresserver/db"
    access_token_expire_minutes: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

    class Config:
        env_file = ".env"


settings = Settings()

if settings.sqlalchemy_url is None:
    settings.sqlalchemy_url = settings.db_type + '://' + settings.db_user + ':' + settings.db_user_pwd + '@' + settings.db_host + '/' + settings.db_name