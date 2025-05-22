create database bd_loja;

create table bd_loja.Clientes (
    id_cliente int primary key,
    nome varchar(100),
    email varchar(100),
    telefone varchar(15)
);

insert into bd_loja.Clientes (id_cliente, nome, email, telefone) values
(1, 'João Silva', 'joao@exemplo.com', '123456789'),
(2, 'Maria Oliveira', 'maria@exemplo.com', '987654321');

create table bd_loja.Produtos (
    id_produto int primary key,
    nome varchar(100),
    preco decimal(10, 2),
    estoque int
);

insert into bd_loja.Produtos (id_produto, nome, preco, estoque) values
(1, 'Camisa', 10, 100),
(2, 'Bola', 20, 50),
(3, 'Computador', 2500, 200);

create table bd_loja.Vendas (
    id_venda int primary key,
    id_cliente int,
    id_produto int,
    data_venda date,
    foreign key (id_cliente) references Clientes(id_cliente),
    foreign key (id_produto) references Produtos(id_produto)
);

insert into bd_loja.Vendas (id_venda, id_cliente, id_produto, data_venda) values
(1, 1, 1, '2025-04-22'),
(2, 2, 2, '2025-04-23'),
(3, 1, 3, '2025-04-24'),
(4, 2, 1, '2025-04-25');

select * from bd_loja.Clientes;
select * from bd_loja.Produtos;
select * from bd_loja.Vendas;

/* Exemplo básico: Imagine que você precise inserir uma nova venda na tabela Vendas e atualizar o estoque do produto. Se algo der errado, você deve ser capaz de desfazer todas as alterações. */

START TRANSACTION;

-- Inserir uma nova venda
INSERT INTO bd_loja.Vendas (id_venda, id_cliente, id_produto, data_venda) 
VALUES (5, 1, 1, '2024-09-05');

-- Atualizar o estoque do produto
UPDATE bd_loja.Produtos 
SET estoque = estoque - 1 
WHERE id_produto = 1;

-- Confirmar a transação
COMMIT;

-- Se algo der errado e você quiser cancelar as alterações:
ROLLBACK;


/* O controle de concorrência no MySQL garante que múltiplas transações possam ocorrer simultaneamente sem causar inconsistências nos dados. Quando vários usuários estão acessando ou manipulando o banco de dados ao mesmo tempo, podem surgir problemas como leituras sujas, repetições de leitura ou anomalias de atualização. Para evitar isso, o MySQL oferece níveis de isolamento. */

/* Os níveis de isolamento controlam como as transações são isoladas umas das outras e como elas lidam com dados não confirmados (não committed). */

/*
READ UNCOMMITTED: transações podem ler dados não confirmados (dirty reads), o que pode resultar em inconsistências.
READ COMMITTED: transações só podem ler dados que já foram confirmados (committed), evitando leituras sujas.
REPEATABLE READ: as transações garantem que, dentro de uma transação, todas as leituras retornarão os mesmos dados, mesmo que outras transações alterem os dados.
SERIALIZABLE: o nível mais restritivo, em que as transações são completamente isoladas umas das outras, garantindo consistência máxima, mas com menos desempenho.
*/

/* Exemplo de definição do nível de isolamento: */

/* 
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
Operações da transação aqui
COMMIT;
*/

/* Tarefa 1: Implementação de transações simples */

/* Realize a inserção de uma nova venda na tabela Vendas e atualize o estoque do produto correspondente. Certifique-se de que, caso algo falhe durante o processo, todas as alterações sejam revertidas usando ROLLBACK. */

START TRANSACTION;

INSERT INTO Vendas (id_venda, id_cliente, id_produto, data_venda)
VALUES (6, 3, 3, '2024-09-05');

UPDATE Produtos
SET estoque = estoque - 1
WHERE id_produto = 2;

COMMIT;
ROLLBACK;
/*
Tarefa 2: Testar o uso de ROLLBACK
Simule uma falha durante a transação anterior. Após inserir a venda, mas antes de atualizar o estoque, decida usar ROLLBACK para garantir que nenhuma mudança seja aplicada no banco de dados.
*/

START TRANSACTION;

INSERT INTO bd_loja.Vendas (id_venda, id_cliente, id_produto, data_venda)
VALUES (6, 3, 3, '2024-09-05');

ROLLBACK;

UPDATE bd_loja.Produtos
SET estoque = estoque - 1
WHERE id_produto = 2;

COMMIT;

/*
Tarefa 3: Controle de concorrência com nível de isolamento
Defina o nível de isolamento da transação como SERIALIZABLE para garantir que não haja conflitos entre transações simultâneas de vendas e atualizações de estoque.
*/

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

START TRANSACTION;

INSERT INTO Vendas (id_venda, id_cliente, id_produto, data_venda)
VALUES (8, 5, 4, '2024-09-05');

UPDATE Produtos
SET estoque = estoque - 1
WHERE id_produto = 4;

COMMIT;

/*
Tarefa 4: Resolução de conflitos
Explique como o controle de concorrência ajuda a evitar problemas, como leituras sujas e transações parcialmente aplicadas. Em qual cenário você aplicaria o nível de isolamento READ COMMITTED em vez de SERIALIZABLE? Faça um exercício de reflexão sobre desempenho versus segurança.
*/


