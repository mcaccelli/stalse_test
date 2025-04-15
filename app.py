from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)


##########################################################
########################### 01 ###########################
##########################################################
@app.route('/')
def index():
    return render_template('index.html')


##########################################################
########################### 02 ###########################
##########################################################
# CRIANDO O DATAFRAME
df = pd.DataFrame({
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html (CRIE UM HTML PARA ISSO)


@app.route('/table')
def table():
    return render_template('table.html', tables=[df.to_html(classes=('data', 'display'))])


# Foi criado um método de inicialização para a aplicação (dev ou prod) ao iniciar via python app.py
# Caso seja em produção, é uma boa prática utilizar um serviço WSGI para Flask, inserido o GUNICORN
if __name__ == '__main__':
    environment = os.getenv('MODE', 'development').lower()

    if environment == 'development':
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True
        )
    elif environment == 'production':
        os.system("gunicorn -w 4 -b 127.0.0.1:5000 app:app")
