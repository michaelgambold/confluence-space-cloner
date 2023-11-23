import json

import requests
from requests.auth import HTTPBasicAuth

# https://developer.atlassian.com/cloud/confluence/rest/v1/intro
# https://developer.atlassian.com/cloud/confluence/rest/v2/intro


class ConfluenceError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def create_space(
    confluence_domain: str,
    username: str,
    api_token: str,
    space_id: str,
    space_name: str,
) -> None:
    url = f"https://{confluence_domain}/wiki/rest/api/space"

    auth = HTTPBasicAuth(username, api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    payload = json.dumps(
        {
            "key": space_id,
            "name": space_name,
        }
    )

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth,
    )

    if response.ok:
        return

    raise ConfluenceError("Create Space returned an error")


def get_space(
    confluence_domain: str, username: str, api_token: str, space_id: str
) -> dict:
    url = f"https://{confluence_domain}/wiki/api/v2/spaces/{space_id}"

    auth = HTTPBasicAuth(username, api_token)

    headers = {"Accept": "application/json"}

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth,
    )

    if response.ok:
        return response.json()

    raise ConfluenceError("Get Space returned an error")
