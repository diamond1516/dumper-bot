from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings as PydanticSettings

load_dotenv()


class BaseSettings(PydanticSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = "ignore"


class Settings(BaseSettings):
    BOT_TOKEN: str
    SCRIPT_PATH: str
    SCRIPT_VENV_PATH: str
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: str = '6379'
    MEDIA_URL: str = 'media/'
    STATIC_URL: str = 'static/'
    TIME_ZONE: str = 'Asia/Tashkent'


class DBSettings(BaseSettings):
    DB_USER: str = None
    DB_PASS: str = None
    DB_HOST: str = None
    DB_PORT: int = 5432
    DB_NAME: str = None
    ECHO: bool = True

    @property
    def database_url(self) -> str:
        return str(
            PostgresDsn.build(
                host=self.DB_HOST,
                port=self.DB_PORT,
                username=self.DB_USER,
                password=self.DB_PASS,
                path=self.DB_NAME,
                scheme="postgresql+asyncpg"
            )
        )


SETTINGS = Settings()
DB_SETTINGS = DBSettings()
