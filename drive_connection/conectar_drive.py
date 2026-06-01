from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR.parent / '.env'
load_dotenv(env_path)


def conectar():

    # ID da pasta
    folder_id = os.getenv("ID_PASTA")

    # Scope
    SCOPES = [os.getenv("SCOPE_LOCAL")]

    # Caminho do JSON
    json_path = BASE_DIR / 'service_account.json'

    # Credenciais
    creds = service_account.Credentials.from_service_account_file(
        json_path,
        scopes=SCOPES
    )

    # Conecta Drive
    service = build(
        'drive',
        'v3',
        credentials=creds
    )

    print("Bot conectado!")

    return folder_id, SCOPES, service