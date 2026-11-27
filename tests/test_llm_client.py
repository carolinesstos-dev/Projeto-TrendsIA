from unittest.mock import MagicMock, patch

import pytest

from llm_client import ErroLLM, consultar_modelo


def _resposta_com_texto(texto):
    resposta = MagicMock()
    resposta.text = texto
    return resposta


def test_resposta_valida_e_retornada(monkeypatch):
    with patch("llm_client.genai.Client") as cliente_falso:
        cliente_falso.return_value.models.generate_content.return_value = (
            _resposta_com_texto("tosse e febre")
        )
        resultado = consultar_modelo("chave-ficticia", "modelo-teste", "tosse")
    assert resultado == "tosse e febre"


def test_resposta_vazia_gera_erro():
    with patch("llm_client.genai.Client") as cliente_falso:
        cliente_falso.return_value.models.generate_content.return_value = (
            _resposta_com_texto("")
        )
        with pytest.raises(ErroLLM):
            consultar_modelo("chave-ficticia", "modelo-teste", "tosse")


def test_falha_de_comunicacao_gera_erro_compreensivel():
    with patch("llm_client.genai.Client") as cliente_falso:
        cliente_falso.return_value.models.generate_content.side_effect = (
            ConnectionError("sem rede")
        )
        with pytest.raises(ErroLLM) as info:
            consultar_modelo("chave-ficticia", "modelo-teste", "tosse")
    assert "Não foi possível consultar o modelo" in str(info.value)



def test_credencial_invalida_gera_mensagem_clara():
    with patch("llm_client.genai.Client") as cliente_falso:
        cliente_falso.return_value.models.generate_content.side_effect = (
            Exception("401 UNAUTHENTICATED: API key not valid")
        )
        with pytest.raises(ErroLLM) as info:
            consultar_modelo("chave-ficticia", "modelo-teste", "tosse")
    assert "Credencial inválida" in str(info.value)

def test_indisponibilidade_gera_mensagem_clara():
    with patch("llm_client.genai.Client") as cliente_falso:
        cliente_falso.return_value.models.generate_content.side_effect = (
            Exception("503 UNAVAILABLE: high demand")
        )
        with pytest.raises(ErroLLM) as info:
            consultar_modelo("chave-ficticia", "modelo-teste", "tosse")
    assert "temporariamente indisponível" in str(info.value)