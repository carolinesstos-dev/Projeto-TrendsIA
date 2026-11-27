\# Triagem PA: primeiro fluxo com LLM



Projeto do P0 do Programa de Capacitação em Desenvolvimento de Agentes de IA (Softex e Trends IA).



\## Problema escolhido



Organizar a fila de um pronto atendimento a partir do que a enfermagem já registrou, classificando cada caso em vermelho, amarelo ou verde.



\## Usuário



A equipe de recepção, que precisa saber quem chamar primeiro sem reabrir a avaliação de cada paciente.



\## Por que usar um LLM



O relato do paciente costuma vir em linguagem livre e variada ("tá queimando de febre", "meu peito aperta ao subir a escada"). Uma regra por palavra-chave deixaria muitos casos de fora. O LLM faz apenas essa extração de sintomas.



\## Funcionamento



1\. A entrada é um texto com a queixa.

2\. O LLM (Gemini) devolve a queixa como texto livre.

3\. A prioridade é definida por regras no código, não pelo modelo, para que a classificação seja previsível e testável.



\## Limites do projeto



\- Execução local, pelo terminal.

\- Um único modelo, o Gemini.

\- A classificação usa limites fictícios para fins de teste. Não deve ser usada para orientar atendimento real.

\- A decisão final de gravidade é sempre da equipe de saúde.



\## Instalação



Requisitos: Python 3.10 ou superior e Git.



```powershell

git clone https://github.com/carolinesstos-dev/Projeto-TrendsIA.git

cd Projeto-TrendsIA

python -m venv .venv

.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

```



\## Configuração do acesso ao Gemini



1\. Acesse https://aistudio.google.com com uma conta Google pessoal.

2\. Clique em \*\*Get API key\*\* e depois em \*\*Create API key\*\*.

3\. Copie o arquivo `.env.example` para um novo arquivo chamado `.env`.

4\. No `.env`, preencha `GEMINI\_API\_KEY` com a sua chave.



A chave nunca deve ser colocada no código nem enviada ao repositório. O arquivo `.env` está no `.gitignore`.



Os parâmetros do modelo, como temperatura e limite de tokens, ficam em `parametros.json`.



\## Execução



```powershell

python main.py

```



Depois de iniciar, digite a queixa e aperte Enter.



\## Exemplos de entrada e saída



Entrada: `Estou com tosse há uma semana e ontem tive febre`



Saída: \[### 1. Tipos de Tosse

\* \*\*Tosse Seca (Irritativa):\*\* Não produz catarro. É comum em alergias, exposição à poluição/ar seco, refluxo ou no início de gripes e resfriados.

\* \*\*Tosse Produtiva (com catarro):\*\* Produz secreção. Serve para expulsar o muco acumulado nos pulmões ou bronquios. Comum no final de gripes, em bronquites ou pneumonias.]



Entrada vazia: a aplicação avisa que a mensagem não pode estar vazia e encerra sem chamar o modelo.



\## Testes



Testes locais, sem chamada ao modelo:



```powershell

python -m pytest

```



Testes reais: a execução do `main.py` com uma entrada válida faz uma chamada real ao Gemini.



Testes simulados: \[PREENCHER QUANDO OS TESTES DE CREDENCIAL INVÁLIDA E FALHA DE COMUNICAÇÃO ESTIVEREM PRONTOS].



\## Limitações conhecidas



\- O prompt ainda não restringe a resposta do modelo. Nos testes, ele deu orientações de tratamento além da extração de sintomas. A regra de prioridade no código é a proteção principal.

\- Os testes de credencial inválida e de falha de comunicação ainda não foram escritos.

\- O modelo Ollama, disponibilizado pela instituição, foi considerado, mas não foi implementado nesta fase.



\## Vídeo de demonstração



\[LINK DO VÍDEO NO YOUTUBE, NÃO LISTADO]

