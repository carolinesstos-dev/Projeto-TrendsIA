import pytest

from config import ErroConfiguracao, carregar_chave


def test_chave_ausente_gera_erro(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(ErroConfiguracao):
        carregar_chave()


def test_chave_vazia_gera_erro(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "   ")
    with pytest.raises(ErroConfiguracao):
        carregar_chave()


def test_chave_presente_e_retornada(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "chave-ficticia")
    assert carregar_chave() == "chave-ficticia"