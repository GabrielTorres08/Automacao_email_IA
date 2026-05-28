from openai import OpenAI
from dotenv import load_dotenv
from templates_IA import template_padrao
import os
load_dotenv()

def fazer_pergunta(msn):

    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": template_padrao() + f'''DADOS: {msn}'''
            }
        ]
    )

    return response.choices[0].message.content