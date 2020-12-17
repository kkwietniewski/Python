from flask import Flask,jsonify, request, url_for, render_template

app = Flask(__name__)
users_list = []


@app.route('/')
def hello_world():
    return render_template('hello_world.html')


@app.route('/api/users/add/<int:user_id>', methods=['POST'])
def create_user(user_id):
    user_data = {'id': user_id, 'email': request.json['email']}
    users_list.append(user_data)
    print(users_list)
    return jsonify({
        'status': 'User Created'
    })


@app.route('/api/users', methods=['GET'])
def get_users():
    return render_template('users.html', users=users_list)


@app.route('/api/users/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    for user in users_list:
        if user['id'] == int(user_id):
            users_list.remove(user)
            return jsonify(users_list)
        else:
            return jsonify({
                "status": "User does not exist!"
            }), 404


@app.route('/api/users/flush_db', methods=['GET'])
def flush_db():
    users_list.clear()
    return jsonify(users_list)


if __name__ == '__main__':
    app.run(debug=True)
