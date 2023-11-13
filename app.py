from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class cadvolei:
    def __init__(self, nome, idade, posicaoJogo, nivelExperiencia, cidadeEestado, dias, horarios):
        self.nome = nome
        self.idade = idade
        self.posicaoJogo = posicaoJogo
        self.nivelExperiencia = nivelExperiencia
        self.cidadeEestado = cidadeEestado
        self.dias = dias
        self.horarios = horarios


Lista = []


@app.route('/volei')
def volei():
    return render_template('JogadoresVolei.html', Titulo = 'Jogadores De Vôlei: ', ListaVolei = Lista)


@app.route('/')
def inicio():
    return 'Começando'


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = 'Cadastro de Jogadores')


@app.route("/criar", methods = ['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    posicaoJogo = request.form['posicaoJogo']
    nivelExperiencia = request.form['nivelExperiencia']
    cidadeEestado = request.form['cidadeEestado']
    dias = request.form['dias']
    horarios = request.form['horarios']

    obj = cadvolei(nome, idade, posicaoJogo, nivelExperiencia, cidadeEestado, dias, horarios)

    Lista.append(obj)

    return redirect('/volei')


if __name__ == '__main__':
    app.run()
