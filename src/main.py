from flask import Flask, render_template, request, jsonify

app  = Flask(__name__)

#Variables
VALID_USERNAME = 'test'
VALID_PASSWORD = 'test'
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return jsonify({"success": True, "message": "Login successful"})
        else :
            return jsonify({"success": False, "message": "Username and password do not match"})

    return render_template('index.html')

@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)