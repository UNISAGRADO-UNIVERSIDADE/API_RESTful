from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados para posts e usuários
posts = [
    {'id': 1, 'title': 'Primeiro Post', 'content': 'Este é o conteúdo do primeiro post', 'author_id': 1},
    {'id': 2, 'title': 'Segundo Post', 'content': 'Este é o conteúdo do segundo post', 'author_id': 2},
    # Adicione mais posts aqui para testar a paginação
]

users = [
    {'id': 1, 'name': 'Usuário 1', 'email': 'usuario1@example.com'},
    {'id': 2, 'name': 'Usuário 2', 'email': 'usuario2@example.com'},
    # Adicione mais usuários aqui para testar a paginação
]

def paginate(data, page, per_page):
    """Simples helper para paginar dados."""
    start = (page - 1) * per_page
    end = start + per_page
    return data[start:end]

def sort_data(data, sort_by, direction):
    """Simples helper para ordenar dados."""
    reverse = direction == 'desc'
    return sorted(data, key=lambda x: x.get(sort_by), reverse=reverse)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    sort_by = request.args.get('sort_by', 'id')
    direction = request.args.get('direction', 'asc')

    sorted_posts = sort_data(posts, sort_by, direction)
    paginated_posts = paginate(sorted_posts, page, per_page)
    
    return jsonify(paginated_posts), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    sort_by = request.args.get('sort_by', 'id')
    direction = request.args.get('direction', 'asc')

    sorted_users = sort_data(users, sort_by, direction)
    paginated_users = paginate(sorted_users, page, per_page)
    
    return jsonify(paginated_users), 200

if __name__ == '__main__':
    app.run(debug=True)

