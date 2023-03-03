from flask import Flask, render_template

from produto import Produto

#para instalar o flask por comando:
#1.acessar o terminal
#2.acessar venv: CD venv
#3.acessar scripts: CD scripts
#4.para visualizar arquivos: DIR
#5. .\pip install flask
#OU para instalar uma versão específica. Ex:
# .\pip install flask=2.0.2

p1 = Produto('TV LG 50"', 3999, 5)
p2 = Produto('CELULAR Samsung', 1999, 10)
p3 = Produto('Geladeira Brastemp', 1500, 3)

lista = [p1, p2, p3]
print(p1)




#criar um app do flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('relatorio.html', titulo='Relatório estoque', produtos=lista)

@app.route('/cadastrar')
def cadastrar():
    return '<h1>Cadastro de produto</h1>'

@app.route('/editar')
def editar():
    return '<h1>Alteração de produto</h1>'




if __name__ == '__main__':
    app.run(debug=True)
