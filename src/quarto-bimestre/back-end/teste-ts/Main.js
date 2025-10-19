"use strict";
exports.__esModule = true;
var Usuario_js_1 = require("./Usuario.js");
var TipoUsuario_js_1 = require("./TipoUsuario.js");
var usuario = new Usuario_js_1["default"](1, 'Dielme', 'dielme@exemplo.com', '1234', TipoUsuario_js_1["default"].Administrador);
usuario.exibirDetalhes(usuario.getTipoUsuario());
