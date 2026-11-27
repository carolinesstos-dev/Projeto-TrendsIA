from google import genai

from config import carregar_parametros


class ErroLLM(Exception):
    """Falha ao consultar o modelo."""


def consultar_modelo(chave: str, modelo: str, texto: str) -> str:
    parametros = carregar_parametros()
    cliente = genai.Client(api_key=chave)
    try:
        resposta = cliente.models.generate_content(
            model=modelo,
            contents=texto,
            config=genai.types.GenerateContentConfig(
                temperature=parametros["temperatura"],
                max_output_tokens=parametros["max_tokens"],
            ),
        )
    except Exception as erro:
        raise ErroLLM(f"Não foi possível consultar o modelo: {erro}") from erro

    if not resposta.text:
        raise ErroLLM("O modelo respondeu sem texto.")
    return resposta.text