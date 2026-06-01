from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os
from drive_connection.conectar_drive import conectar

def fazer_uploads():

    infos = conectar()

    SCOPES = infos[1]

    # ID DA PASTA DO GOOGLE DRIVE
    FOLDER_ID = infos[0]

    # AUTENTICAÇÃO
    service = infos[2]

    # CRIA PASTA LOCAL
    os.makedirs('uploads', exist_ok=True)


    # LISTA TODOS OS ARQUIVOS DA PASTA

    query = (
        f"'{FOLDER_ID}' in parents "
        f"and trashed=false"
    )

    results = service.files().list(
        q=query,
        fields="files(id, name)"
    ).execute()

    arquivos = results.get('files', [])

    # VERIFICA SE EXISTEM ARQUIVOS

    if not arquivos:
        print('Nenhum arquivo encontrado.')

    else:

        print(f'{len(arquivos)} arquivos encontrados.')
        print()

        # BAIXA CADA ARQUIVO

        for arquivo in arquivos:

            file_id = arquivo['id']
            file_name = arquivo['name']

            print(f'Baixando: {file_name}')

            caminho = os.path.join(
                'uploads',
                file_name
            )

            request = service.files().get_media(
                fileId=file_id
            )

            fh = io.FileIO(caminho, 'wb')

            downloader = MediaIoBaseDownload(fh, request)
            done = False
            
            while not done:

                status, done = downloader.next_chunk()
                progresso = int(status.progress() * 100)
                print(f'  {progresso}%')

            print(f'Concluído: {file_name}')
            print()

    print('Todos os downloads terminaram.')