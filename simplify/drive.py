from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import Resource, build
from pydantic import BaseModel


class DriveObj(BaseModel):
    name: str
    id: str
    kind: str
    mime_type: str
    drive_id: str


class Doc(DriveObj):
    public: bool
    draft: bool


class Folder(DriveObj):
    pass


class Drive:
    def __init__(self, drive_id: str, service: Resource):
        self.drive_id = drive_id
        self.drive_info = service.teamdrives().get(teamDriveId=drive_id).execute()
        self.service = service
        self.files = self.contains()

    def contains(self):
        drive_obj = (
            self.service.files()
            .list(
                corpora="teamDrive",
                supportsTeamDrives=True,
                teamDriveId=self.drive_id,
                includeTeamDriveItems=True,
            )
            .execute()
            .get("files")
        )

        container = []
        for each_obj in drive_obj:
            if each_obj.get("mimeType") == "application/vnd.google-apps.document":
                if each_obj.get("name").startswith("PUBLIC:"):
                    public = True
                    draft = False
                elif each_obj.get("name").startswith("DRAFT:"):
                    public = False
                    draft = True
                else:
                    public = False
                    draft = False

                container.append(
                    Doc(
                        kind=each_obj.get("kind"),
                        id=each_obj.get("id"),
                        name=each_obj.get("name"),
                        mime_type=each_obj.get("mimeType"),
                        drive_id=each_obj.get("driveId"),
                        draft=draft,
                        public=public,
                    )
                )

            elif each_obj.get("kind") == "application/vnd.google-apps.folder":
                container.append(
                    Doc(
                        kind=each_obj.get("kind"),
                        id=each_obj.get("id"),
                        name=each_obj.get("name"),
                        mime_type=each_obj.get("mimeType"),
                        drive_id=each_obj.get("driveId"),
                    )
                )

        return container

    def docs(self):
        return [x for x in self.files if isinstance(x, Doc)]

    def folders(self):
        return [x for x in self.files if isinstance(x, Folder)]
