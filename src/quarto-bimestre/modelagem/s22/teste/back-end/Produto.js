class Produto {

    constructor(id, nome, imagem) {
        this._id = id;
        this._nome = nome;
        this._imagem = imagem
    }

    getId() {
        return this._id_produto;
    }

    getNome() {
        return this._nome;
    }

    getImagem(){
        return this._imagem;
    }

}
export default Produto;


