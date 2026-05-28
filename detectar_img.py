import os

# Caminho da pasta que deseja verificar ('.' representa o diretório atual)
caminho_pasta = './imagens'

# Lista todos os arquivos e pastas
itens = os.listdir(caminho_pasta)

# Exibe cada item na tela
for item in itens:
    print(item)