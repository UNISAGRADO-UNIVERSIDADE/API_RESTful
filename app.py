# Importa as funções necessárias do módulo flask
from flask import Flask, jsonify, request

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Uma lista de dicionários que simula um banco de dados em memória para armazenar posts
posts = [
    {'id': 1, 'title': 'Primeiro Post', 'content': 'Este é o conteúdo do primeiro post', 'author_id': 1},
    {'id': 2, 'title': 'Segundo Post', 'content': 'Este é o conteúdo do segundo post', 'author_id': 2}
]

# Uma lista de dicionários que simula um banco de dados em memória para armazenar usuários
users = [
    {'id': 1, 'name': 'Usuário 1', 'email': 'usuario1@example.com'},
    {'id': 2, 'name': 'Usuário 2', 'email': 'usuario2@example.com'}
]

# Endpoint GET para '/api/posts' que retorna a lista de todos os posts, incluindo o nome do autor
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts_with_authors = []
    for post in posts:
        author = next((user for user in users if user['id'] == post.get('author_id')), None)
        if author:
            post_with_author = post.copy()
            post_with_author['author_name'] = author['name']
            posts_with_authors.append(post_with_author)
        else:
            posts_with_authors.append(post)
    return jsonify(posts_with_authors), 200

# Endpoint GET para '/api/posts/<int:post_id>' que retorna um post específico pelo seu ID
@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is not None:
        return jsonify(post), 200
    else:
        return jsonify({'message': 'Post not found'}), 404

# Endpoint POST para '/api/posts' que cria um novo post
@app.route('/api/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

# Endpoint PUT para '/api/posts/<int:post_id>' que atualiza um post existente pelo seu ID
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is not None:
        data = request.get_json()
        post.update(data)
        return jsonify(post), 200
    else:
        return jsonify({'message': 'Post not found'}), 404

# Endpoint DELETE para '/api/posts/<int:post_id>' que deleta um post específico pelo seu ID
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({'message': 'Post deleted'}), 204

# Novo endpoint GET para '/api/users' que retorna uma lista de usuários
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Novo endpoint POST para '/api/users' que cria um novo usuário
@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

# Novo endpoint DELETE para '/api/users/<int:user_id>' que deleta um usuário específico pelo seu ID
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 204

# Verifica se o arquivo é o módulo principal e executa o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)