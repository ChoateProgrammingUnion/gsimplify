from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import Resource, build


class Drive:
    def __init__(self, drive_id: str, service: Resource):
        self.drive_id = drive_id
        self.drive_info = service.teamdrives().get(teamDriveId=drive_id).execute()
        
    def files(self):
        return service.files().list(
            corpora='teamDrive',
            supportsTeamDrives=True,
            teamDriveId=self.drive_id,
            includeTeamDriveItems=True
        ).execute()

