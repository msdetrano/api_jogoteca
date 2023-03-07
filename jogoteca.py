from flask import Flask, render_template, request
import sqlite3

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogo4 = Jogo('Mario', 'Aventura', 'Super Nintendo')
jogo5 = Jogo('FIFA', 'Futebol', 'PS4')
lista = [jogo1, jogo2, jogo3, jogo4, jogo5]



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html', titulo='Tela Inicial')


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
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True)