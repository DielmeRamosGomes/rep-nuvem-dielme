<?php
include_once "conexao.php";

$id = $_POST["input-id"];
$nome = $_POST["input-name"];
$preco = $_POST["input-price"];

$sql = "CALL PRODUCT_REGISTER(?, ?, ?);";

// Preparar a declaração
if ($stmt = $conexao->prepare($sql)) {
    // Vincular parâmetros
    $stmt->bind_param("isd", $id, $nome, $preco);

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