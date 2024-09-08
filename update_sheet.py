import gspread
from google.oauth2.service_account import Credentials
import csv

def update_google_sheet(csv_file_path, sheet_key, worksheet_name):
    # Set up credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    gs_creds = os.environ['GOOGLE_SHEETS_CREDENTIALS']
    creds = Credentials.from_service_account_file(gs_creds, scopes=scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet = client.open_by_key(sheet_key).worksheet(worksheet_name)

    # Read CSV and update the sheet
    with open(csv_file_path, 'r') as file:
        csv_data = list(csv.reader(file))

    # Clear existing content
    sheet.clear()
    
    # Get the number of rows and columns in the CSV data
    num_rows = len(csv_data)
    num_cols = len(csv_data[0]) if csv_data else 0

    cell_range = f'A1:{gspread.utils.rowcol_to_a1(num_rows, num_cols)}'
    sheet.update(csv_data, cell_range)

    print("Google Sheet has been updated successfully!")

# Usage
csv_file_path = 'det_tools.csv'
sheet_key = os.environ['SHEET_KEY']
worksheet_name = os.environ['SHEET_NAME']  # or the name of your specific worksheet

update_google_sheet(csv_file_path, sheet_key, worksheet_name)