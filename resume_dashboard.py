from flask import Flask, render_template
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import add_data_sheet  # Your script for adding data to Google Sheets

app = Flask(__name__)

# Google Sheets API setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "***"
SPREADSHEET_ID = "***"

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

def get_data():
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df.to_dict(orient='records')

# Run the function to parse and append data when the server starts
add_data_sheet.parse_and_append()

@app.route('/')
def dashboard():
    data = get_data()
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=False)
