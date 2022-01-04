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

sheet = 'EDEL'

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
SAMPLE_SPREADSHEET_ID = ID   # unique for each google sheet
SAMPLE_RANGE_NAME = 'Sheet1!A1:C1'                                       # variable that was used below, to output the value we need to print
def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API


    # Below is the code to test if input is working or not
    
    # fam_cell = 'Guidelines!A1:C1'
    # fam_type = 'abc'
    # #fam_type = 'Employee Only'
    # cell_input = [[fam_type],]
    # print('Fam_type - ', cell_input)
    # body = {'values': cell_input}

    # #print('family type update')

    # result = service.spreadsheets().values().update(
    #     spreadsheetId=SAMPLE_SPREADSHEET_ID, range = fam_cell,       #
    #     valueInputOption="USER_ENTERED", body=body).execute()   
    

                
if __name__ == '__main__':
    main()