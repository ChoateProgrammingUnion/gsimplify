import pickle
import os.path
from googleapiclient.discovery import build, Resource
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

TEAM_DRIVE_ID = '0AFB5gF1TxS1vUk9PVA'

def main():
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # flow = InstalledAppFlow.from_client_secrets_file('titanium-haiku-294920-a2a9bb798460.json', SCOPES)

    credentials = service_account.Credentials.from_service_account_file(
        'titanium-haiku-294920-a2a9bb798460.json', scopes=SCOPES)

    service: Resource = build('drive', 'v3', credentials=credentials)

    drive_info = service.teamdrives().get(teamDriveId=TEAM_DRIVE_ID).execute()
    files_in_drive = service.files().list(
        corpora='teamDrive',
        supportsTeamDrives=True,
        teamDriveId=TEAM_DRIVE_ID,
        includeTeamDriveItems=True
    ).execute()

    pass


if __name__ == '__main__':
    main()
