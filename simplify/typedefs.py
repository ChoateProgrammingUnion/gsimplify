from typing import Optional

from pydantic import BaseModel


class DriveObj(BaseModel):
    name: str
    id: str
    kind: str
    mime_type: str
    drive_id: str


class DocType(DriveObj):
    public: bool
    draft: bool
    pointer: str
    title: Optional[str]
    content: Optional[dict]


class FolderType(DriveObj):
    pass
