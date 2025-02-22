
class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_URL: PostgresDsn
    MEDIA_URL: str = 'media/'
    STATIC_URL: str = 'static/'
    TIME_ZONE: str = 'Asia/Tashkent'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
