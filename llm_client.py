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
        mensagem = str(erro)
        if "401" in mensagem or "API key" in mensagem:
            raise ErroLLM(
                "Credencial inválida. Verifique GEMINI_API_KEY no arquivo .env."
            ) from erro
        if "503" in mensagem or "UNAVAILABLE" in mensagem:
            raise ErroLLM(
                "O serviço do modelo está temporariamente indisponível. "
                "Tente novamente em alguns minutos."
            ) from erro
        raise ErroLLM(
            "Não foi possível consultar o modelo. Verifique a conexão e tente novamente."
        ) from erro

    if not resposta.text:
        raise ErroLLM("O modelo respondeu sem texto.")
    return resposta.text