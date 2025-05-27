from flask import Flask, render_template, request, jsonify
from labirinto import resolver_labirinto

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('labirinto.html')

@app.route('/resolver', methods=['POST'])
def resolver():
    dados = request.get_json()
    inicio = int(dados['inicio'])
    fim = int(dados['fim'])
    caminho = resolver_labirinto(inicio, fim)
    return jsonify({"caminho": caminho})

if __name__ == '__main__':
    app.run(debug=True)
