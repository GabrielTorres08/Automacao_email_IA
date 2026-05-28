import easyocr
import cv2
from groq import fazer_pergunta

msn = ""

# Inicializa OCR em português
reader = easyocr.Reader(['pt'])

# Caminho da imagem
imagem = 'imagens/imagem.jpeg'

# Ler imagem
img = cv2.imread(imagem)

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Melhorar contraste
gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

# Ler texto
resultado = reader.readtext(gray)

print("\n=== TEXO ENCONTRADO ===\n")

for item in resultado:
    texto = item[1]
    confianca = item[2]

    msn += f"{texto}\n"
    print(f"Texto: {texto}")
    print(f"Confiança: {confianca:.2f}")
    print("-" * 30)

print(fazer_pergunta(msn=resultado))