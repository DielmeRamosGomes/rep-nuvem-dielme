create database if not exists bd_ecommerce;

create table if not exists produtos(
    id_produto int auto_increment primary key,    
    nome varchar(50) not null,
    categoria varchar(50) not null,
    preco decimal(10,2) not null
);

create table if not exists vendas(
    id_venda int auto_increment primary key,
    id_produto int not null,
    quantidade int not null,
    data_venda date not null,
    foreign key (id_produto) references produtos(id_produto)
);

insert into produtos (nome, categoria, preco) values
('Produto A', 'Categoria 1', 10.00),
('Produto B', 'Categoria 2', 20.00),
('Produto C', 'Categoria 1', 15.00),
('Produto D', 'Categoria 3', 30.00),
('Produto E', 'Categoria 2', 25.00);

insert into vendas (id_produto, quantidade, data_venda) values
(1, 5, '2025-01-15'),
(2, 3, '2025-02-20'),
(1, 2, '2025-03-10'),
(3, 4, '2025-03-15'),
(4, 1, '2025-04-05'),
(5, 6, '2025-04-10'),
(2, 2, '2025-05-01'),
(1, 1, '2025-05-05');

select * from produtos;
select * from vendas;

/* 1) Qual foi o produto mais vendido nos últimos três meses? */

SELECT p.nome, COUNT(v.id_venda) AS total_vendas
    FROM produtos p INNER JOIN vendas v ON p.id_produto = v.id_produto
        WHERE v.data_venda >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) GROUP BY p.nome
            ORDER BY total_vendas DESC LIMIT 1;

/* 2) Qual foi o valor total de vendas por categoria no mês passado? */

select p.categoria, SUM(v.quantidade * p.preco) as total_vendas
    from produtos p inner join vendas v on p.id_produto = v.id_produto
        where v.data_venda >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and v.data_venda < CURDATE()
            group by p.categoria;

/* 3) Qual foi a média de produtos vendidos por pedido nos últimos três meses? */

select AVG(quantidade) as media_produtos_vendidos
    from vendas v where v.data_venda >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH);

/* 4) Qual foi o valor da venda mais alta e da mais baixa nos últimos três meses? */

select MAX(v.quantidade * p.preco) as maior_venda, MIN(v.quantidade * p.preco) as menor_venda
    from produtos p inner join vendas v on p.id_produto = v.id_produto
        where v.data_venda >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH);

/* 5) Qual categoria teve a maior quantidade de produtos vendidos nos últimos três meses? */

select p.categoria, SUM(v.quantidade) as total_vendas
    from produtos p inner join vendas v on p.id_produto = v.id_produto
        where v.data_venda >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) group by p.categoria
            order by total_vendas desc limit 1;

/* Crie uma consulta que mostre o faturamento total por mês dos últimos três meses, agrupado por categoria de produto. */

select DATE_FORMAT(v.data_venda, '%Y-%m') as mes, p.categoria, SUM(v.quantidade * p.preco) as faturamento_total
    from produtos p inner join vendas v on p.id_produto = v.id_produto
        where v.data_venda >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) group by mes, p.categoria
            order by mes desc, p.categoria;

select * from produtos;            