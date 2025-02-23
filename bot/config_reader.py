from pydantic_settings import BaseSettings
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_URL: str
    MEDIA_URL: str = 'media/'
    STATIC_URL: str = 'static/'
    TIME_ZONE: str = 'Asia/Tashkent'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
