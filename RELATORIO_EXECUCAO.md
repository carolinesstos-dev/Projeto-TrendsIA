## Decisões principais



### 1. Gemini como LLM



Decisão: usar a API do Gemini pela conta pessoal do Google.

Alternativa: usar um modelo local pelo Ollama, disponibilizado pela instituição.

Justificativa: optei pelo Gemini nesta fase porque o Ollama não era obrigatório, e preferi adiar a configuração de um modelo local para quando for exigido. Assim, mantenho o foco no fluxo principal do projeto.



### 2. Triagem por regra fixa, com o LLM apenas para extrair sintomas



Decisão: a prioridade (vermelho, amarelo ou verde) é definida por regras no código, a partir dos sintomas e dos dados informados. O LLM apenas converte a queixa em uma lista de sintomas.

Alternativa: deixar o modelo classificar diretamente a prioridade a partir do relato.

Justificativa: regras no código tornam a triagem previsível, testável e auditável, evitando variações e falhas não anunciadas que um modelo poderia produzir.



### 3. Parâmetros de geração em arquivo JSON



Decisão: temperatura e limite de tokens ficam no arquivo parametros.json, já carregado pelo config.py, em vez de fixados no código.

Alternativa: definir os valores diretamente na chamada ao modelo.

Justificativa: permite ajustar estabilidade e tamanho das respostas sem alterar o núcleo do código, conforme pedido no Avançado. A leitura já está pronta no config.py, restando integrar esses parâmetros à chamada.



## Falhas e limitações



Modelo descontinuado: na primeira execução, o modelo gemini-2.5-flash retornou erro 404, informando que não estava mais disponível para novos usuários. Identifiquei pela mensagem de erro e troquei para gemini-3.6-flash, depois de conferir a documentação oficial do Google.



Chave exposta: uma chave de API apareceu em uma conversa. Revoguei essa chave no AI Studio e gerei outra, guardada apenas no arquivo .env, que está no .gitignore. Conferi que a chave não está nos arquivos versionados.



requirements.txt em UTF-16: o arquivo foi gerado com o operador > do PowerShell, que grava em UTF-16, e o Git passou a tratá-lo como binário. Corrigi regravando o arquivo em UTF-8 e refazendo o commit com amend, antes de publicar.



Limitações conhecidas: os testes de credencial inválida e de falha de comunicação ainda não foram escritos. O prompt atual não restringe a resposta do modelo, e nos testes ele deu orientações de tratamento além da extração de sintomas. A regra de prioridade no código é a proteção principal, mas essa restrição ainda precisa ser resolvida.

