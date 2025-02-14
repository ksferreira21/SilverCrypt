from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

# Define the required Google Drive API scope
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Path to the service account credentials file (User should specify their own path)
SERVICE_ACCOUNT_FILE = "your_service_account.json"

# Google Drive folder ID where the file will be uploaded (User should specify their own folder ID)
FOLDER_ID = "your_drive_folder_id"

def upload_to_drive(file_path, file_name):
    """Uploads a file to Google Drive in the specified folder."""
    
    try:
        # Load credentials from the service account file
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('drive', 'v3', credentials=creds)

        # Define file metadata, including the folder where it should be uploaded
        file_metadata = {
            'name': file_name,
            'parents': [FOLDER_ID]
        }
        
        # Define the media upload type (JSON in this example)
        media = MediaFileUpload(file_path, mimetype='application/json')
        
        # Upload the file
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f"File {file_name} successfully uploaded to Google Drive! ID: {file.get('id')}")
    
    except Exception as e:
        print(f"Error uploading the file to Google Drive: {e}")

if __name__ == "__main__":
    # Example usage (User should specify their own file path and name)
    upload_to_drive("../your_file.json", "your_file.json")

