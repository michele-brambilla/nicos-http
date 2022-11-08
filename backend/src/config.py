from pydantic import BaseSettings


class Settings(BaseSettings):
    hostname: str = "localhost"
    port: int = 1301
    nicos_user: str = "guest"
    password: str = ""

    class Config:
        env_file = "./.env"