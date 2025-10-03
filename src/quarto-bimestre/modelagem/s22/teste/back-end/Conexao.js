import mysql from 'mysql2/promise'; // Usando a API de Promises para facilitar o async/await

class Conexao {
    constructor(host, port, user, password, database) {
        this.config = {
            host: host,
            port: port,
            user: user,
            password: password,
            database: database,
            waitForConnections: true,
            connectionLimit: 10,
            queueLimit: 0
        };
        this.pool = null; // Usando Pool para melhor gerenciamento de conexões
    }

    async conectar() {
        if (!this.pool) {
            try {
                this.pool = mysql.createPool(this.config);
                const connection = await this.pool.getConnection();
                console.log("Conexão com o banco de dados estabelecida com sucesso!");
                connection.release(); // Libera a conexão de volta para o pool
            } catch (error) {
                console.error("Erro ao conectar ao banco de dados:", error);
                throw error; // Rejeita a promise para que o erro seja tratado no código que chama
            }
        }
        return this.pool;
    }

    async getConexao() {
        if (!this.pool) {
            await this.conectar();
        }
        return this.pool.getConnection();
    }
}

export default Conexao;

