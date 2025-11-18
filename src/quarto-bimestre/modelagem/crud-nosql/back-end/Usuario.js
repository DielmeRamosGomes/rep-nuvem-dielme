import mongoose from "mongoose";

const usuarioSchema = new mongoose.Schema(
    {
        nome: {type: String, require: true},
        email: {type: String, require: true},
        senha: {type: String, require: true}
    }
);

const USUARIO = mongoose.model('Usuario', usuarioSchema);
export default USUARIO;


