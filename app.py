from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [
    {'id': 1, 'title': 'Primeiro Post', 'content': 'Este é o conteúdo do primeiro post', 'author_id': 1},
    {'id': 2, 'title': 'Segundo Post', 'content': 'Este é o conteúdo do segundo post', 'author_id': 2}
]

users = [
    {'id': 1, 'name': 'Usuário 1', 'email': 'usuario1@example.com'},
    {'id': 2, 'name': 'Usuário 2', 'email': 'usuario2@example.com'}
]

def validate_post_data(data):
    if not data.get('title') or not data.get('content') or not data.get('author_id'):
        return False
    return True

def validate_user_data(data):
    if not data.get('name') or not data.get('email'):
        return False
    return True

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

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post), 200
    return jsonify({'message': 'Post not found'}), 404

@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not validate_post_data(data):
        return jsonify({'message': 'Missing or invalid data'}), 400
    new_post_id = len(posts) + 1
    data['id'] = new_post_id
    posts.append(data)
    return jsonify(data), 201

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    data = request.get_json()
    if not validate_post_data(data):
        return jsonify({'message': 'Missing or invalid data'}), 400
    post.update(data)
    return jsonify(post), 200

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({'message': 'Post deleted'}), 204

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_user_data(data):
        return jsonify({'message': 'Missing or invalid data'}), 400
    new_user_id = len(users) + 1
    data['id'] = new_user_id
    users.append(data)
    return jsonify(data), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
