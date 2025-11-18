// npm install express
// npm install cors
// npm install mongoose 
// npm install dotenv
import express from 'express';
import cors from 'cors';
import mongoose from 'mongoose';
import USUARIO from './Usuario.js';

const app = express();

// use middleware cors
app.use(cors({
  origin: 'http://127.0.0.1:5500' // Apenas a origem, sem o caminho do arquivo
}));

app.use(express.json());

const PORT = 3000;

mongoose.connect(process.env.MONGODB_URI, {})
.then(() => console.log(`Conectado ao MongoDB!`))
.catch(error => console.error(`Erro ao conectar ao MongoDB: ${error}`));

app.post('/cadastrodeusuario', async (req, res) => {
    try {
        const usuario = new USUARIO(req.body);
        await usuario.save();
        res.status(201).send(usuario);
    } catch (error) {
        res.status(400).send(error);
    }
});

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta: ${PORT}`);
});

