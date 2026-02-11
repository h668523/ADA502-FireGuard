from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import folium

app  = Flask(__name__)
app.secret_key = "supersecretkey"

#Variables
VALID_USERNAME = 'test'
VALID_PASSWORD = 'test'

m = folium.Map(location=[62.972077, 10.395563], zoom_start=6)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['username'] = username
            return jsonify({"success": True, "message": "Login successful"})
        else :
            return jsonify({"success": False, "message": "Username and password do not match"})

    return render_template('index.html')

@app.route('/set-guest', methods=['POST'])
def set_guest():
    session['username'] = "Guest"
    return '', 204

@app.route('/mainpage')
def mainpage():
    username = session.get('username', 'Guest')
    return render_template('mainpage.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)