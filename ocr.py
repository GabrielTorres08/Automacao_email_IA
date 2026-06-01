import easyocr
import cv2

def raspagem_dados(nome_arquivo):

    msn = ""

    # Inicializa OCR em português
    reader = easyocr.Reader(['pt'])

    # Caminho da imagem
    imagem = f'uploads/{nome_arquivo}'

    # Ler imagem
    img = cv2.imread(imagem)

    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Melhorar contraste
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    # Ler texto
    resultado = reader.readtext(gray)

    msm = ""

    print("\n=== TEXO ENCONTRADO ===\n")

    for item in resultado:
        texto = item[1]
        confianca = item[2]

        print(f"Texto: {texto}")
        print(f"Confiança: {confianca:.2f}")
        print("-" * 30)

        msm += f"Texto: {texto}\n"
        msm += f"Confiança: {confianca:.2f}\n"
        msm += "-" * 30
        msm += "\n"


    print("\n=======================\n")
    return msm

# print(fazer_pergunta(msn=resultado))