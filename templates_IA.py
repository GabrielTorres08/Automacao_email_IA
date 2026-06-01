from dotenv import load_dotenv
import os
load_dotenv()

email_remetente = os.getenv("EMAIL_REMETENTE")
nome_remetente = os.getenv("NOME_REMETENTE")
idade_remetente = os.getenv("IDADE_REMETENTE")
telefone_contato = os.getenv("TELEFONE_CONTATO")
infos = os.getenv("INFORMACOES_PROFISSIONAIS")

def template_padrao() :
    texto = '''Quais as informações de contato do texto? Gere uma resposta como um JSON, faça alguma alteração caso encontre algum erro de digitação, SOMENTE O JSON, SEM NENHUMA OUTRA MENSAGEM DE RESPOSTA, DO EXATO FORMATO: ''' + '''
                {
                    "telefone": "numero_nos_dados",
                    "email": "email_nos_dados",
                    "corpo_email": "escreva um corpo de email adequado às informações dos dados",
                    "cabeçalho_email" "cabeçalho de email adequado às informações dos dados": 
                }''' + f'''
    REGRAS:

    0 - Os dados que você analisará são resgatados usando o cv2 python, então por isso, só considere informações que possuam valores de clareza/confiança >= 0.5, se os valores forem menores, descarte-os ou coloque-os como Null, em caso de email ou contato de telefone

    1 - Caso não haja telefone ou email, retorne o parâmetro do JSON como Null.


    2 - Os parâmetros "corpo_email" e "cabeçalho_email", devem possuir valores gerados por você, esses valores devem ser formatados de maneira formal, de acordo com as regras de um e-mail. Se houver informações importantes nos dados passados, você pode colocar tanto no "corpo_email", quanto no "cabeçalho_email", mas só o que pode ser necessário.

    3 - No "corpo_email", devem haver informações minhas, são elas:
        Nome: {nome_remetente};
        Idade {idade_remetente};
        Email de contato: {email_remetente};
        Telefone de contato: {telefone_contato}.
    Todos os dados formatados devidamente no corpo do email. A IDADE E O NOME SÓ DEVEM APARECER UMA VEZ NO COMEÇO DO TEXTO, E O {email_remetente} JUNTO COM O {telefone_contato} AO FINAL DO TEXTO, SEGUINDO A RISCA A REGRA 4.

    4 - Um template de email padrão para embasamento, formate ele com as informações necessesárias e com as regras desse manual de execução:
        "Olá, tudo bem?

        Meu nome é [SEU NOME] e estou entrando em contato para me candidatar à vaga anunciada. Tenho interesse na oportunidade e acredito que posso contribuir positivamente com a equipe.

        Sou uma pessoa dedicada, responsável e com vontade de aprender e crescer profissionalmente. Em anexo, envio meu currículo para avaliação.

        Fico à disposição para uma entrevista ou para fornecer mais informações, caso necessário.

        Agradeço pela atenção e pela oportunidade.

        Atenciosamente,
        [SEU NOME]
        [SEU TELEFONE]".

    4.1 - Não esqueça de colocar no corpo do email que o meu curriculo está anexado ao documento.

    5 - Use formatação HTML para melhorar a coesão do texto, use <br> <em> <hr> e entre outras tags, mas só tags que sejam compatíveis com o Gmail.
    
    6 - NÃO EXAGERE NAS INFORMAÇÕES DO CORPO DO EMAIL, FAÇA ELOGIOS MAS NÃO DE MANEIRA EXARCEBADA.

    7 - INFORMACOES_PROFISSIONAIS:{infos}. PS: Leve isso em consideração ao escrever o corpo de e-mail, só para você não passar nenhuma informação falsa.  

    8 - Os dados passados a seguir são os que serão analisados, ANALISE-OS COM EXTREMO CUIDADO:
    
                '''
    return texto

