# /src/app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Sistema de Gerenciamento de Tarefas</h1><p>Em construção...</p>"


if __name__ == '__main__':
    app.run(debug=True)