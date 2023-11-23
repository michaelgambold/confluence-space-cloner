import os
from pydantic import BaseModel


class Config(BaseModel):
    api_token: str
    confluence_domain: str
    username: str


def get_config() -> Config:
    return Config(
        api_token=os.environ.get("API_TOKEN"),
        confluence_domain=os.environ.get("CONFLUENCE_DOMAIN"),
        username=os.environ.get("USERNAME"),
    )
