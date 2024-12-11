from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Valorant', 'FPS', 'PC')
    jogo2 = Jogo('The Last of us', 'Surviver Horror', 'PS3/ PS4 e PS5')
    jogo3 = Jogo('Halo', 'FPS', 'Xbox 360')
    lista = [jogo1, jogo2, jogo3]
    
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo(): 
    return render_template('novo.html', titulo='Novo Jogo')

app.run()