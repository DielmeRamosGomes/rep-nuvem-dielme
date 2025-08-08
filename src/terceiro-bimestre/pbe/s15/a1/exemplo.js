class Candidato {
    constructor(nome, nome_vice, partido, cargo, numero) {
        this._nome = nome;
        this._nome_vice = nome_vice;
        this._partido = partido;
        this._cargo = cargo;
        this._numero = numero;
    }

    nome() {
        return this._nome;
    }

    nome_vice() {
        return this._nome_vice;
    }

    partido() {
        return this._partido;
    }

    cargo() {
        return this._cargo;
    }

    numero() {
        return this._numero;
    }

    mostrar_detalhes() {
        console.log(`Candidato: ${this.nome()}`);
        console.log(`Vice: ${this.nome_vice()}`);
        console.log(`Partido: ${this.partido()}`);
        console.log(`Cargo: ${this.cargo()}`);
        console.log(`Número: ${this.numero()}`);
    }
}
export default Candidato;

const candidato = new Candidato("João Silva", "Maria Souza", "Partido A", "Prefeito", 20);
candidato.mostrar_detalhes();


