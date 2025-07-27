import gspread
from google.oauth2.service_account import Credentials
import resume_parser

def authenticate_google_sheets(service_account_file, scopes):
    creds = Credentials.from_service_account_file(service_account_file, scopes=scopes)
    return gspread.authorize(creds)

def open_spreadsheet(client, spreadsheet_id):
    return client.open_by_key(spreadsheet_id).sheet1  # Access first sheet

def extract_resume_data(file_path):
    return

def append_data_to_sheet(sheet, data):
    sheet.append_row([data["Name"], data["Email"], data["Phone Number"],
                      data["Education"], data["Experience"], data["Skills"]])

def parse_and_append():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    SERVICE_ACCOUNT_FILE = "eternal-mark-449814-t2-8e614c36ca55.json"
    SPREADSHEET_ID = "18iujrvc3Eb4wRp451w1qouVFa6DIJ-AB2Mv1-Ml3pSc"
    OUT_PATH = "output.txt"

    client = authenticate_google_sheets(SERVICE_ACCOUNT_FILE, SCOPES)

    sheet = open_spreadsheet(client, SPREADSHEET_ID)

    data = resume_parser.extract_data(OUT_PATH)

    append_data_to_sheet(sheet, data)

    print("Data successfully added to Google Sheets!")
    if int(resume_parser.validate(data))>55:
        print("email")

