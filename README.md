# Projeto Backend com Flask

## Introdução
Este projeto é uma introdução ao desenvolvimento de backend usando o Flask, um microframework para Python. O Flask é uma escolha excelente para começar no mundo do desenvolvimento web devido à sua simplicidade e flexibilidade. Neste projeto, nós construímos uma API RESTful básica que simula um sistema de blog, onde podemos criar, ler, atualizar e deletar posts.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação.
- **Flask**: Framework web usado para construir a API.
- **Git**: Sistema de controle de versão para rastrear mudanças no código-fonte.

## Estrutura do Projeto
O projeto consiste em um único arquivo Python (`app.py`) que contém todo o código necessário para rodar a aplicação Flask. Este arquivo define várias rotas da API para interagir com os posts do blog.

- `app.py`: O coração da nossa aplicação. Este arquivo contém a lógica da API e as rotas para lidar com as requisições HTTP.

## Funcionalidades da API
- **Listar Todos os Posts**: Uma requisição GET para `/api/posts` retorna uma lista de todos os posts.
- **Obter um Post Específico**: Uma requisição GET para `/api/posts/<post_id>` retorna os detalhes de um post específico.
- **Criar um Novo Post**: Uma requisição POST para `/api/posts` permite criar um novo post.
- **Atualizar um Post Existente**: Uma requisição PUT para `/api/posts/<post_id>` permite atualizar um post existente.
- **Deletar um Post**: Uma requisição DELETE para `/api/posts/<post_id>` permite deletar um post específico.

## Executando o Projeto
Para executar o projeto, você precisa ter o Python instalado em seu ambiente. Clone o repositório do projeto, navegue até a pasta do projeto no terminal e execute:

```bash
python app.py

# Importa as funções necessárias do módulo flask
from flask import Flask, jsonify, request

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Uma lista de dicionários que simula um banco de dados em memória para armazenar posts
posts = [
    {'id': 1, 'title': 'Primeiro Post', 'content': 'Este é o conteúdo do primeiro post'},
    {'id': 2, 'title': 'Segundo Post', 'content': 'Este é o conteúdo do segundo post'}
]

Cont...

```
