from pydantic import BaseSettings, SecretStr, PostgresDsn


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr = '7362304291:AAHsSLbhZozUvZboGh_brEXMFp22bMkwF4E'
    DB_URL: PostgresDsn = 'postgresql+psycopg://shoxista:shoxista@localhost/shoxista'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
