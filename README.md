# LFG Challenge

Este é um projeto em Python e Django com os seguintes requisitos funcionais:

- O sistema deverá ter uma interface web onde pessoas possam solicitar propostas, nessa interface não será necessário que a pessoa esteja logada no sistema ou mesmo que ela possua um usuário no sistema

- O sistema deve oferecer flexibilidade para que o admin do sistema possa configurar quais os campos que a proposta deve conter, ou seja, caberá a alguém de dentro da empresa definir o que deverá ser pedido de informação para o solicitante da proposta

- A proposta deverá passar por uma avaliação automatizada através de uma API de Análise de Crédito já desenvolvida (documentação da API disponível em: https://loan-processor.digitalsys.com.br/swagger/index.html), caso a API retorne o status de não aprovado, a proposta deve ser negada automaticamente, caso seja aprovada, deverá ser disponibilizada para avaliação humana.

- Deve haver uma listagem dentro do sistema para que o admin visualize as propostas, para aquelas marcadas para análise humana o admin deve poder mudar o status da proposta para 'Aprovada' ou 'Negada'

## Tecnologias usadas

- Python
- Django
- Django REST Framework
- Requests
- Celery
- RabbitMQ
- HTML, CSS, JS
- Docker

## Como instalar e usar

Para instalar e usar este projeto, siga os seguintes passos:

### Via Docker

1. Clone este repositório

2. Utilize o comando `docker-compose up` e aguarde o término do processo (termina quando iniciar o servidor web)

3. Vá para o passo 8

### Local

1. Clone este repositório

2. Certifique-se que você [tem o RabbitMQ instalado](https://www.rabbitmq.com/download.html)

3. Instale as dependências do projeto:
`pip3 install -r requirements.txt`

4. Faça as migrações do banco de dados:
`python3 manage.py makemigrations`
`python3 manage.py migrate`

5. Crie um usuario admin:
`python3 manage.py createsuperuser`

6. Rode o servidor de desenvolvimento:
`python3 manage.py runserver`

7. Inicie o worker do Celery:
`celery -A lfg_project worker -l info`

8. Acesse o app no navegador ou em algum cliente HTTP:

- `http://localhost:8000/` ou `http://127.0.0.1:8000/` para ver a interface de envio de propostas
- rota `/admin` para criar campos de propostas (Proposal Fields) -> Via docker user = luiz, senha = luiz

9. O admin conseguirá ver as propostas enviadas em `Proposals` dentro do painel Admin

- Existem 4 `status` de propostas: `Pendente` se trata da proposta recem criada e em analise pela API; `Negada` se trata da proposta recusada pela API ou pelo humano; `Humana` se trata da proposta aprovada pela API para revisão humana; `Aprovada` é a proposta aprovada pelo humano.
- No lado direito da tela, filtre por `Humana`, essas serão as propostas aprovadas pela API para revisão humana.

