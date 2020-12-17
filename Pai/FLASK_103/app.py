from flask import Flask, jsonify, request, redirect, url_for, render_template

app = Flask(__name__)
users_list = []


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users.html', users=users_list)


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    for user in users_list:
        if user['id'] == int(id):
            return jsonify(user)
        else:
            return jsonify({"status": "User does not exist!"}), 404


@app.route('/user', methods=['POST'])
def create_user():
    user = request.json
    print(user)
    users_list.append(user)
    return jsonify({
        "status": "User created"
    })


@app.route('/admin', methods=['GET'])
def admin_view():
    return jsonify({
        "status": "Hello Admin"

    })


@app.route('/dashboard/<int:id>', methods=['GET'])
def user_view(id):
    return render_template('user_view.html', user_id=id)


@app.route('/mobile', methods=['GET'])
def mobile_view():
    return jsonify({
        "status":"Mobile view"
    })


@app.route('/login/<int:id>', methods=['GET'])
def login(id):
    # if request.headers['IS-MOBILE'] == 'True':
    #     return redirect(url_for('mobile_view'))
    if int(id) == 0:
        return redirect(url_for('admin_view'))
    else:
        return redirect(url_for('user_view', id=id))


if __name__ == '__main__':
    app.run(debug=True)
