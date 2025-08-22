<?php
include_once "conexao.php";

$id = $_POST["id"];
$nome = $_POST["nome"];
$preco = $_POST["price"];

$sql = "CALL PRODUCT_REGISTER($id, $nome, $preco);";

// Preparar a declaração
if ($stmt = $conexao->prepare($sql)) {
    // Vincular parâmetros
    $stmt->bind_param("ssd", $id, $nome, $preco);

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