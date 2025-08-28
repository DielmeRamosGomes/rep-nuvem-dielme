<?php
	if (session_status() !== PHP_SESSION_ACTIVE){  //Verificar se a sessão já está aberta.
		session_start();
	} 
	$hostname = "localhost";
	$user = "root";
	$password = "1234";
	$database = "db_product";
    $port = "3307";

	$conexao = @new mysqli($hostname, $user, $password, $database, $port);

	if($conexao->connect_error){
		die('Não foi possível conectar: '.$conexao->connect_error);
	}

?>



