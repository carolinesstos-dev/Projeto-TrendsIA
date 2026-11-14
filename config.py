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

import json
from pathlib import Path

CAMINHO_PARAMETROS = Path(__file__).parent / "parametros.json"


def carregar_parametros() -> dict:
    try:
        with open(CAMINHO_PARAMETROS, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError as erro:
        raise ErroConfiguracao("O arquivo parametros.json não foi encontrado.") from erro
    except json.JSONDecodeError as erro:
        raise ErroConfiguracao("O arquivo parametros.json não é um JSON válido.") from erro

    return {
        "temperatura": float(dados.get("temperatura", 0.2)),
        "max_tokens": int(dados.get("max_tokens", 300)),
    }