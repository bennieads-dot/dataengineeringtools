import os
import csv
import json
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials


def update_google_sheet(csv_file_path, sheet_key, worksheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds_dict = json.loads(os.environ['GOOGLE_SHEETS_CREDENTIALS'])
    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_key).worksheet(worksheet_name)

    with open(csv_file_path, 'r') as file:
        csv_data = list(csv.reader(file))

    sheet.clear()

    num_rows = len(csv_data)
    num_cols = len(csv_data[0]) if csv_data else 0

    cell_range = f'A1:{gspread.utils.rowcol_to_a1(num_rows, num_cols)}'
    sheet.update(csv_data, cell_range)

    print("Public sheet updated successfully")

def main():
    csv_file_path = 'det_tools.csv'
    sheet_key = os.environ['SHEET_KEY']
    worksheet_name = os.environ['SHEET_NAME']
    update_google_sheet(csv_file_path, sheet_key, worksheet_name)


if __name__ == '__main__':
    load_dotenv()
    main()