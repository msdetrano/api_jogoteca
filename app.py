from flask import Flask, render_template, request
import sqlite3


# Init da Aplicação
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console


app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    resultado = cursor.fetchall()
    cursor.close()
    return render_template('lista.html',titulo='Jogos', resultado=resultado)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Tela de Cadastro')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (nome, categoria, console) VALUES (?, ?, ?)", (nome, categoria, console))
    conn.commit()
    conn.close()
    return index()

app.run(port=80, host='0.0.0.0',debug=True)
