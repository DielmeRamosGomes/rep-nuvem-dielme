# pip install flask

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1,
     "nome": "Harry Potter e a pedra filosofal",
     "autor": "J.K Rowling",
     "editora": "Rocco",
     "ano": "1997-06-26"
     },
    {"id": 2,
     "nome": "Harry Potter e a câmara secreta",
     "autor": "J.K Rowling",
     "editora": "Rocco",
     "ano": "1998-07-02"
     }
]

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/livros', methods=['POST'])
def adicionar_livros():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify({"mensagem": "Produto adicionado com sucesso!"}), 201

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
    
    