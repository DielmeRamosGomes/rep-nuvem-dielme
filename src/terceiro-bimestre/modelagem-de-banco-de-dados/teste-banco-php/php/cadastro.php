<?php
include_once "conexao.php";

header("Access-Control-Allow-Origin: http://127.0.0.1:5500");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit(0);
}

$nome = $_POST["input-name"];
$preco = $_POST["input-price"];

$sql = "CALL PRODUCT_REGISTER(?, ?, ?);";

// Preparar a declaração
if ($stmt = $conexao->prepare($sql)) {
    // Vincular parâmetros
    $stmt->bind_param("sd", $nome, $preco);

    // Executar a consulta
    if ($stmt->execute()) {
        echo "Produto cadastrado com sucesso!";
    } else {
        echo "Erro ao cadastrar o produto: " . $stmt->error;
    }

    // Fechar a declaração
    $stmt->close();
} else {
    echo "Erro na preparação da consulta: " . $conexao->error;
}

// Fechar a conexão
$conexao->close();

?>