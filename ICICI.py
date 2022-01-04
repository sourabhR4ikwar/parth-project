from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import time
import random

# ICICI - 13RgZAAQA7i9e_tAwU5YLevuUCTZx4U9_vlVsJNbjPrE
# TATA - 1Rl9-ASs5ya9N-kQzt4sQPNrjCDJuliQQH5plgSyHWqM
# MAGMA - 1o5yv5CvBu2iv6YW3Wij2UvlpKFmBfrsuNeNFT7i_r8I
# CHOLA - 1H8kWdJTNppb4U2IfytSTxrMg9CeFbwAL1RffQBE-90s
# ABHI - 1eam2OcpiUfKxwT55uxFHCz2Y1a3bMAVxem4fhB9lIxg
# EDEL - 1hLL3lfuqO9xVcERo2KxALsQ-rrcGMkFFoRtNxHYXvvU

sheet = 'ICICI'

Dict = {'ICICI': '13RgZAAQA7i9e_tAwU5YLevuUCTZx4U9_vlVsJNbjPrE',
        'TATA':  '1Rl9-ASs5ya9N-kQzt4sQPNrjCDJuliQQH5plgSyHWqM',
        'MAGMA': '1o5yv5CvBu2iv6YW3Wij2UvlpKFmBfrsuNeNFT7i_r8I',
        'CHOLA': '1H8kWdJTNppb4U2IfytSTxrMg9CeFbwAL1RffQBE-90s',
        'ABHI':  '1eam2OcpiUfKxwT55uxFHCz2Y1a3bMAVxem4fhB9lIxg',
        'EDEL':  '1hLL3lfuqO9xVcERo2KxALsQ-rrcGMkFFoRtNxHYXvvU'}

ID = Dict[sheet]
print(ID)


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ID   

def cell_input(content, cell):
        cell_body = [[content],]
        body = {'values': cell_body}
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range = cell,       
            valueInputOption="USER_ENTERED", body=body).execute() 



def calculate(tot_lives, sum_insured, age, family_type, room_rent, maternity_amount, wait, initial_wait, maternity_wait):
    creds = None
    if os.path.exists(r'tokens/token'+ sheet + '.json'):                                         # a file generated, for each spreadsheet i would be analysing, unque for a spreadsheet
        creds = Credentials.from_authorized_user_file(r'tokens/token'+ sheet + '.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r'credentials.json', SCOPES)                                  # unique credentials of my account, project
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(r'tokens/token'+ sheet + '.json', 'w') as token:
            token.write(creds.to_json())
    global service 
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API


    cell = 'D27:D27'
    cell_input(int(tot_lives), 'GHI Input!'+cell)
    cell_input(int(tot_lives)/2, 'GHI Input!C8:C8')
    cell_input(int(tot_lives)/2, 'GHI Input!C9:C9')
    cell_input(int(tot_lives)/2, 'GHI Input!M24:M24')


    price_cell = 'Quote Format!I19:K19'
    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range = price_cell).execute()       # the output I want to see
    values = result.get('values', [])
    
    return values[0][0]




    



