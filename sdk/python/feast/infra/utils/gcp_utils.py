
import os
from typing import List
from google.auth.credentials import Credentials
from google_auth_oauthlib import flow


def get_appflow(file_path: str="client_secret.json", scopes: List[str]=["https://www.googleapis.com/auth/bigquery"]) -> Credentials:
    """
    Get the Google AppFlow for BigQuery offline store.
    This method is a no-op if ELEMENO_MODE is not production, in this case authentication happens through service account.
    """
    if not os.environ['ELEMENO_MODE'] == 'production':
        appflow = flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file=file_path, scopes=scopes)
        appflow.run_console()
        return appflow.credentials