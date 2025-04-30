create table if not exists vendas(
    id_venda int auto_increment primary key,
    produto varchar(100) not null,
    quantidade int not null,
    valor_unitario int not null,
    data_venda date not null
);

insert into vendas(id_venda, produto, quantidade, valor_unitario, data_venda)
    values(default, "geladeira", 2, 1000, "2025-03-30");

update vendas set produto = "cadeira" where id_venda = 3;

/* 1) Quantas vendas foram realizadas no mês passado?*/

SELECT COUNT(*) AS total_vendas FROM vendas WHERE data_venda 
    BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND 
        LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

/* vendas nos ultimos 30 dias */
SELECT COUNT(*) AS total_vendas FROM vendas WHERE data_venda 
    BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE();

/* 2) Qual foi o valor total de vendas de cada produto? */

select produto, sum(quantidade * valor_unitario) as total_vendas from vendas
    group by produto;

/* 3) Qual foi o produto mais vendido em quantidade? */

select produto, sum(quantidade) as total_vendas from vendas
    group by produto order by total_vendas desc limit 1;

/* 4) Qual foi o valor médio das vendas por dia no mês passado? */

select avg(total_vendas) as media_vendas from (
    select sum(quantidade * valor_unitario) as total_vendas, data_venda from vendas
        where data_venda between DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and 
            LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
        group by data_venda
) as vendas_por_dia;

/* 5) Qual foi a venda de maior valor e a de menor valor no mês passado? */

select max(total_vendas) as maior_venda, min(total_vendas) as menor_venda from (
    select sum(quantidade * valor_unitario) as total_vendas, data_venda from vendas
        where data_venda between DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and 
            LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
        group by data_venda
) as vendas_por_dia;

/* Crie uma consulta que mostre o valor médio da venda por dia para cada produto no mês passado. */

select produto, avg(total_vendas) as media_vendas from (
    select produto, sum(quantidade * valor_unitario) as total_vendas, data_venda from vendas
        where data_venda between DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and 
            LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
        group by produto, data_venda
) as vendas_por_dia group by produto;

select * from vendas;


