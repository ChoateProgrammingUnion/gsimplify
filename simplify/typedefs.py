from typing import List, Optional

from pydantic import BaseModel


class DriveObj(BaseModel):
    name: str
    id: str
    kind: str
    mime_type: str
    drive_id: str
    parents: str


class DocType(DriveObj):
    public: bool
    draft: bool
    pointer: str
    title: Optional[str]
    content: Optional[dict]
    ast: Optional[dict]


class FolderType(DriveObj):
    path: Optional[List[str]]


class Drive(BaseModel):
    path: List[str] = [""]
