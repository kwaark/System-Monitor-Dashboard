from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/servidor-api')
def api_server():
    return render_template('servidor-api.html')

@app.route('/servidor-database')
def servidor_database():
    return render_template('database.html')

if __name__ == '__main__':
    app.run(port=5000)
