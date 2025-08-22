<?php
	if (session_status() !== PHP_SESSION_ACTIVE){  //Verificar se a sessão já está aberta.
		session_start();
	} 
	$hostname = "localhost";
	$user = "root";
	$password = "";
	$database = "db_product";
    $port = "3306";

	$conexao = mysqli_connect(hostname: $hostname,username: $user,password: $password,database: $database, port: $port);

	if($conexao->connect_error){
		die('Não foi possível conectar: '.$conexao->connect_error);
	}

?>



