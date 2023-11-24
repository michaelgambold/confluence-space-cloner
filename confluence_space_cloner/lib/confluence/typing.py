from typing import Literal

from pydantic import BaseModel, Field


class BodyType(BaseModel):
    representation: str
    value: str


class SpaceDescription(BaseModel):
    plain: BodyType
    view: BodyType


class SpaceIcon(BaseModel):
    path: str
    api_download_link: str = Field(alias="apiDownloadLink")


class SpaceLinks(BaseModel):
    webui: str


class Space(BaseModel):
    id: str
    key: str
    name: str
    type: str
    status: str
    author_id: str = Field(alias="authorId")
    created_at: str = Field(alias="createdAt")
    homepage_id: str = Field(alias="homepageId")
    description: SpaceDescription
    icon: SpaceIcon
    links: SpaceLinks = Field(alias="_links")


class SpacePermissionPrinciple(BaseModel):
    id: str
    type: Literal["group", "role", "user"]


class SpacePermissionOperation(BaseModel):
    key: Literal[
        "administer",
        "archive",
        "create_space",
        "copy",
        "create",
        "delete",
        "export",
        "move",
        "purge",
        "purge_version",
        "read",
        "restrict_content",
        "restore",
        "update",
        "use",
    ]
    targetType: Literal[
        "application",
        "attachement",
        "blogpost",
        "comment",
        "page",
        "space",
        "userProfile",
        "whiteboard",
    ]


class SpacePermission(BaseModel):
    id: str
    principal: SpacePermissionPrinciple
    operation: SpacePermissionOperation
