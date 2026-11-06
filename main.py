import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

chave = os.getenv("GEMINI_API_KEY")
if not chave:
    raise SystemExit("GEMINI_API_KEY não encontrada. Verifique o arquivo .env.")

cliente = genai.Client(api_key=chave)

resposta = cliente.models.generate_content(
       model="gemini-3.6-flash",
    contents="Em uma frase, o que é triagem em um pronto-socorro?",
)

print(resposta.text)