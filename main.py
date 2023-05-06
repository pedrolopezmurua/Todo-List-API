from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/saludar', methods=['GET'])
def saludar():
    if (request.method=='GET'):
        return '¡Hola, mundo! hice un GET'

@app.route('/', methods=['GET'])
def html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port="3000")