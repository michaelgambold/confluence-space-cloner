import json
from typing import TypeAlias

import requests
from requests.auth import HTTPBasicAuth
from pydantic import BaseModel, Field

from .typing import Space, SpacePermission

# https://developer.atlassian.com/cloud/confluence/rest/v1/intro
# https://developer.atlassian.com/cloud/confluence/rest/v2/intro


SpaceResponse: TypeAlias = Space


class Links(BaseModel):
    next: str


class SpacePermsissionsResponse(BaseModel):
    results: list[SpacePermission]
    links: Links = Field(alias="_links")


class ConfluenceError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def clone_space(
    confluence_domain: str,
    username: str,
    api_token: str,
    new_space_id: str,
    new_space_name: str,
    space: Space,
) -> None:
    url = f"https://{confluence_domain}/wiki/rest/api/space"

    auth = HTTPBasicAuth(username, api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    payload = json.dumps(
        {
            "key": new_space_id,
            "name": new_space_name,
            "description": {"plain": space.description.plain},
            "permissions": [
                {
                    "subjects": {},
                }
            ],
        }
        #   "permissions": [
        #     {
        #       "subjects": {
        #         "user": {
        #           "results": [
        #             {
        #               "type": "known",
        #               "username": "<string>",
        #               "userKey": "<string>",
        #               "accountId": "<string>",
        #               "accountType": "atlassian",
        #               "email": "<string>",
        #               "publicName": "<string>",
        #               "profilePicture": {
        #                 "path": "<string>",
        #                 "width": 2154,
        #                 "height": 2154,
        #                 "isDefault": true
        #               },
        #               "displayName": "<string>",
        #               "timeZone": "<string>",
        #               "isExternalCollaborator": true,
        #               "externalCollaborator": true,
        #               "operations": [
        #                 {
        #                   "operation": "administer",
        #                   "targetType": "<string>"
        #                 }
        #               ],
        #               "details": {},
        #               "personalSpace": {
        #                 "key": "<string>",
        #                 "name": "<string>",
        #                 "type": "<string>",
        #                 "status": "<string>",
        #                 "_expandable": {},
        #                 "_links": {}
        #               },
        #               "_expandable": {
        #                 "operations": "<string>",
        #                 "details": "<string>",
        #                 "personalSpace": "<string>"
        #               },
        #               "_links": {}
        #             }
        #           ],
        #           "size": 2154
        #         },
        #         "group": {
        #           "results": [
        #             {
        #               "type": "group",
        #               "name": "<string>",
        #               "id": "<string>"
        #             }
        #           ],
        #           "size": 2154
        #         }
        #       },
        #       "operation": {
        #         "operation": "administer",
        #         "targetType": "<string>"
        #       },
        #       "anonymousAccess": true,
        #       "unlicensedAccess": true
        #     }
        #   ]
        # }`;
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
) -> Space:
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
        return SpaceResponse.model_validate_json(response.json())

    raise ConfluenceError("Get Space returned an error")


def get_space_permissions(
    confluence_domain: str, username: str, api_token: str, space_id: str
) -> list[SpacePermission]:
    url = f"https://{confluence_domain}/wiki/api/v2/spaces/{space_id}/permissions"

    auth = HTTPBasicAuth(username, api_token)

    headers = {"Accept": "application/json"}

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth,
    )

    # For MVP we are only going to get the first page of space permissions.
    # Will have to add support for paging multiple pages at a later stage.
    if response.ok:
        model_response = SpacePermsissionsResponse.model_validate_json(response.json())
        return model_response.results

    raise ConfluenceError("Get Space returned an error")
