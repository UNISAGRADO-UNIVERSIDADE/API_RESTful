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

# Define um endpoint GET para '/api/posts' que retorna a lista de todos os posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Converte a lista de posts para JSON e retorna com o status HTTP 200 (OK)
    return jsonify(posts), 200

# Define um endpoint GET para '/api/posts/<int:post_id>' que retorna um post específico pelo seu ID
@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    # Procura na lista de posts o post com o ID fornecido, retorna None se não for encontrado
    post = next((post for post in posts if post['id'] == post_id), None)
    # Se um post for encontrado, retorna o post como JSON com status HTTP 200 (OK)
    if post is not None:
        return jsonify(post), 200
    # Se não, retorna uma mensagem de erro como JSON com status HTTP 404 (Not Found)
    else:
        return jsonify({'message': 'Post not found'}), 404

# Define um endpoint POST para '/api/posts' que cria um novo post
@app.route('/api/posts', methods=['POST'])
def create_post():
    # Obtém os dados JSON enviados com a requisição POST
    new_post = request.get_json()
    # Atribui um novo ID ao post, que é um mais que o número de posts existentes
    new_post['id'] = len(posts) + 1
    # Adiciona o novo post à lista de posts
    posts.append(new_post)
    # Retorna o novo post como JSON com status HTTP 201 (Created)
    return jsonify(new_post), 201

# Define um endpoint PUT para '/api/posts/<int:post_id>' que atualiza um post existente pelo seu ID
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    # Procura na lista de posts o post com o ID fornecido, retorna None se não for encontrado
    post = next((post for post in posts if post['id'] == post_id), None)
    # Se um post for encontrado, atualiza-o com os dados enviados
    if post is not None:
        data = request.get_json()
        post.update(data)
        # Retorna o post atualizado como JSON com status HTTP 200 (OK)
        return jsonify(post), 200
    # Se não, retorna uma mensagem de erro como JSON com status HTTP 404 (Not Found)
    else:
        return jsonify({'message': 'Post not found'}), 404

# Define um endpoint DELETE para '/api/posts/<int:post_id>' que deleta um post específico pelo seu ID
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    # A palavra-chave 'global' é usada para modificar a variável global 'posts'
    global posts
    # Cria uma nova lista de posts que não inclui o post com o ID fornecido
    posts = [post for post in posts if post['id'] != post_id]
    # Retorna uma mensagem de sucesso como JSON com status HTTP 204 (No Content)
    return jsonify({'message': 'Post deleted'}), 204

# Verifica se o arquivo é o módulo principal e executa o aplicativo Flask
if __name__ == '__main__':
    # Inicia o aplicativo Flask em modo de depuração
    app.run(debug=True)
```
