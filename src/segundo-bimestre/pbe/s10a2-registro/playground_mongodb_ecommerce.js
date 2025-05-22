
import { MongoClient } from 'mongodb';

// Substitua pela sua string de conexão real do MongoDB
// Exemplo para Atlas: mongodb+srv://<username>:<password>@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority
// Exemplo para local: mongodb://localhost:27017
const uri = "mongodb+srv://dielme:1234@cluster0.g8uqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"; 

async function connectToMongo() {
    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("Conectado ao MongoDB!");

        // Seleciona o banco de dados 'ecommerce'
        const db = client.db('ecommerce');
        console.log("Usando o banco de dados: ecommerce");

        // Agora você pode interagir com as coleções dentro do banco de dados 'ecommerce'
        const productsCollection = db.collection('produtos');

        // Exemplo: Encontra todos os documentos na coleção 'produtos'
        const products = await productsCollection.find({}).toArray();
        console.log("Produtos:", products);

        // Exemplo: Insere um novo produto (descomente para usar)
        // const result = await productsCollection.insertOne({ nome: "Novo Produto", preco: 99.99 });
        // console.log("Produto inserido com _id:", result.insertedId);

    } catch (error) {
        console.error("Erro ao conectar ao MongoDB:", error);
    } finally {
        // Fecha a conexão quando terminar
        await client.close();
        console.log("Conexão MongoDB fechada.");
    }
}

connectToMongo();
