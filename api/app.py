from flask import Flask, jsonify, request
from SmartAgent import SmartAgent

app = Flask(__name__)

@app.route('/')
def index():
    return "Back-End da aplicação"

@app.route('/api/movimento', methods=['POST'])
def movimento():
    data = request.json
    tabuleiro = data.get('tabuleiro')
    agente = SmartAgent(tabuleiro)
    return jsonify(agente.gameMove())

if __name__ == '__main__':
    app.run(debug=True)
