import logging

from config import ErroConfiguracao, carregar_chave, carregar_modelo
from llm_client import ErroLLM, consultar_modelo

logging.basicConfig(
    filename="execucao.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)
log = logging.getLogger("triagem")


def main() -> None:
    log.info("Execução iniciada.")
    try:
        chave = carregar_chave()
        modelo = carregar_modelo()
    except ErroConfiguracao as erro:
        log.error("Erro de configuração: %s", erro)
        print(f"Erro de configuração: {erro}")
        return

    entrada = input("Digite sua mensagem: ").strip()
    if not entrada:
        log.warning("Entrada vazia recebida.")
        print("A mensagem não pode estar vazia. Descreva o que você está sentindo.")
        return

    log.info("Entrada recebida com %d caracteres.", len(entrada))

    try:
        resposta = consultar_modelo(chave, modelo, entrada)
    except ErroLLM as erro:
        log.error("Falha ao consultar o modelo: %s", erro)
        print(erro)
        return

    log.info("Resposta recebida com %d caracteres.", len(resposta))
    print(resposta)


if __name__ == "__main__":
    main()