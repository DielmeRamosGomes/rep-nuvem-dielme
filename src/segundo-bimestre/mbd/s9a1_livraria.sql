create database bd_livraria;

CREATE TABLE clientes_online (
  id_cliente INT,
  nome VARCHAR(100),
  email VARCHAR(100),
  cidade VARCHAR(100)
);

INSERT INTO clientes_online (id_cliente, nome, email, cidade) VALUES
(1, 'Ana Silva', 'ana@email.com', 'São Paulo'),
(2, 'Carlos Santos', 'carlos@email.com', 'Rio de Janeiro'),
(3, 'Bia Oliveira', 'bia@email.com', 'Brasília');

CREATE TABLE clientes_fisicos (
  id_cliente INT,
  nome VARCHAR(100),
  email VARCHAR(100),
  cidade VARCHAR(100)
);

INSERT INTO clientes_fisicos (id_cliente, nome, email, cidade) VALUES
(1, 'Carlos Santos', 'carlos@email.com', 'Rio de Janeiro'),
(2, 'Bia Oliveira', 'bia@email.com', 'Brasília'),
(3, 'Denis Pereira', 'denis@email.com', 'Salvador');

/*1.	UNION: Retorne todos os clientes que compraram em qualquer uma das lojas (on-line ou física) sem duplicar informações. */
explain SELECT nome, email, cidade FROM clientes_online
UNION
SELECT nome, email, cidade FROM clientes_fisicos;

/* INTERSECT: Encontre os clientes que compraram tanto na loja on-line quanto na loja física.*/
SELECT nome, email, cidade FROM clientes_online
INTERSECT
SELECT nome, email, cidade FROM clientes_fisicos;

/* EXCEPT: Liste os clientes que compraram na loja on-line, mas não compraram na loja física.*/
SELECT nome, email, cidade FROM clientes_online
EXCEPT
SELECT nome, email, cidade FROM clientes_fisicos;



