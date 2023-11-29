from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username and password:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

if __name__ == '__main__':
    app.run(debug=True)
