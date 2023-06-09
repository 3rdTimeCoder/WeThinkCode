from __future__ import print_function
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
import json


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/calendar' ]
        
        

def set_calendar_access_rule(email):
    """Refreshes calendar_token.json
    Gives user access to the codeClinic calendar (jhb19.wethinkcode@gmail.com)
    """
    creds = None
   
    if os.path.exists('calendar_token.json'):
        creds = Credentials.from_authorized_user_file('calendar_token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'code_clinic/clinic_credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('calendar_token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        rule = {
            'scope': {
                'type': 'group',
                'value': email,
            },
            'role': 'writer'
        }

        created_rule = service.acl().insert(calendarId='primary', body=rule).execute()

    except HttpError as error:
        print(f'An error occurred: {error}')
        
        
def refreshToken(client_id, client_secret, refresh_token, token):
        params = {
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token
        }        
        authorization_url = "https://oauth2.googleapis.com/token"        
        r = requests.post(authorization_url, data=params)        
        if r.ok:
                data = r.json()
                new_data = dict()
                f = open(token)
                new_data = json.load(f)
                new_data["token"] = data["access_token"]                
                with open(token, 'w') as token:
                    token.write(str(new_data).replace("'",'"'))
        else:
            return None