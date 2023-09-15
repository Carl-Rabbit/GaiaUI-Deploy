import os
from flask import Flask, request, render_template, send_file, redirect, url_for


app = Flask(__name__, template_folder="./dist", static_folder="./dist/static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/<path:path>')
def send_data(path):
    return send_file(os.path.join('./dist/data', path))

if __name__ == '__main__':
    print('server start')
    app.run(host='0.0.0.0', debug=False)
