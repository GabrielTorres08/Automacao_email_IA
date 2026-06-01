from drive_connection.upload_arquivos import fazer_uploads
from ocr import raspagem_dados
from groq import fazer_pergunta
import os


def arquivos_upload():
    os.makedirs('uploads', exist_ok=True)
    caminho_pasta = './uploads'
    itens = os.listdir(caminho_pasta)
    return itens


dict = {}

fazer_uploads()
arquivos = arquivos_upload()

for arquivo in arquivos:
    ponto = arquivo.rfind(".")
    extensao = arquivo[ponto:len(arquivo)]
    dict[f"{arquivo}"] = f"{extensao}"


for item in dict:
    extens = dict[item]
    if extens == ".jpeg" or extens == ".png" or extens == ".jpg":
        print(f"O arquivo \033[32m'{item}'\033[m está OK")
        textos = raspagem_dados(item)
        print(fazer_pergunta(textos))
    else:
        print(f"O arquivo \033[31m'{item}'\033[m não passou")
