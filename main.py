from config import ErroConfiguracao, carregar_chave, carregar_modelo
from llm_client import ErroLLM, consultar_modelo


def main() -> None:
    try:
        chave = carregar_chave()
        modelo = carregar_modelo()
    except ErroConfiguracao as erro:
        print(f"Erro de configuração: {erro}")
        return

    entrada = input("Digite sua mensagem: ").strip()
    if not entrada:
        print("A mensagem não pode estar vazia. Descreva o que você está sentindo.")
        return

    try:
        resposta = consultar_modelo(chave, modelo, entrada)
    except ErroLLM as erro:
        print(f"Erro ao consultar o modelo: {erro}")
        return

    print(resposta)


if __name__ == "__main__":
    main()