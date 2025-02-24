from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_URL: str
    ECHO: bool = True
    SCRIPT_PATH: str
    SCRIPT_VENV_PATH: str
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: str = '6379'
    MEDIA_URL: str = 'media/'
    STATIC_URL: str = 'static/'
    TIME_ZONE: str = 'Asia/Tashkent'

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'


SETTINGS = Settings()
