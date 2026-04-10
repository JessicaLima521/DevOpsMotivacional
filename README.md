# DevOpsMotivacional

Projeto simples em Python que gera frases motivacionais aleatórias.


## Objetivo
Este projeto foi desenvolvido para praticar Git, controle de versões
e conceitos utilizados em pipelines de CI/CD.


 

## Como executar


python app.py
### 1. Build da imagem
docker build -t devops-motivacional .


### 2. Rodar o container
docker run -p 3000:3000 devops-motivacional

### 3. Acessar no navegador
http://localhost:3000

Aplicação testada e funcionando via Docker
