import os

from dotenv import load_dotenv

load_dotenv()


class ErroConfiguracao(Exception):
    """Configuração ausente ou inválida."""


def carregar_chave() -> str:
    chave = os.getenv("GEMINI_API_KEY", "").strip()
    if not chave:
        raise ErroConfiguracao(
            "A chave GEMINI_API_KEY não foi encontrada. "
            "Crie o arquivo .env na pasta do projeto, a partir do .env.example."
        )
    return chave


def carregar_modelo() -> str:
    return os.getenv("GEMINI_MODELO", "gemini-3.6-flash")