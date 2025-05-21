create database if not exists bd_cliente_pedido_produto;

create table if not exists clientes (
    id_cliente int auto_increment primary key,
    nome varchar(50) not null,
    email varchar(50) not null
);

create table if not exists produtos (
    id_produto int auto_increment primary key,
    nome varchar(50) not null,
    preco decimal(10,2) not null,
    quantidade int not null,
    id_pedido int not null,
    foreign key (id_pedido) references pedidos(id_pedido);
);

create table if not exists pedidos (
    id_pedido int auto_increment primary key,
    id_cliente int not null,
    data_pedido date not null,
    foreign key (id_cliente) references clientes(id_cliente)
);

insert into clientes (nome, email) values
('João Silva', 'joao@exemplo.com'),
('Ana Santos', 'ana@exemplo.com'),
('Maria Oliveira', 'maria@exemplo');

insert into pedidos (id_cliente, data_pedido) values
(1, '2025-04-15'),
(2, '2025-04-16'),
(3, '2025-04-17');

insert into produtos (nome, preco, quantidade, id_pedido) values
('Produto A', 10.00, 2, 1),
('Produto B', 20.00, 3, 1),
('Produto C', 30.00, 4, 2),
('Produto D', 40.00, 7, 3),
('Produto E', 50.00, 8, 3),
('Produto C', 30.00, 4, 2);

SELECT c.nome, SUM(p.quantidade) AS total_produtos FROM Clientes c 
    JOIN Pedidos pe ON c.id_cliente = pe.id_cliente 
        JOIN Produtos p ON pe.id_produto = p.id_produto WHERE c.id_cliente IN
            (SELECT id_cliente FROM Pedidos GROUP BY  id_cliente HAVING SUM(preco_total) > 500) GROUP BY c.nome;


