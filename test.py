import pickle
import os.path
from googleapiclient.discovery import build, Resource
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

TEAM_DRIVE_ID = "0AFB5gF1TxS1vUk9PVA"


def main():
    credentials = service_account.Credentials.from_service_account_file(
        "titanium-haiku-294920-a2a9bb798460.json", scopes=SCOPES
    )

    service: Resource = build("drive", "v3", credentials=credentials)

    drive_info = service.teamdrives().get(teamDriveId=TEAM_DRIVE_ID).execute()
    files_in_drive = (
        service.files()
        .list(
            corpora="teamDrive",
            supportsTeamDrives=True,
            teamDriveId=TEAM_DRIVE_ID,
            includeTeamDriveItems=True,
        )
        .execute()
    )

    pass


if __name__ == "__main__":
    main()
