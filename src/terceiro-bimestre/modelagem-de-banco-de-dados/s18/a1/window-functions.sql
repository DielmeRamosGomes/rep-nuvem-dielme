create database if not exists db_commerce_tech;

create table if not exists db_commerce_tech.vendas(
    id_venda int auto_increment primary key,
    data_venda date not null,
    produto varchar(100) not null,
    vendedor varchar(100) not null,
    quantidade int not null,
    valor_total decimal(10, 2) 
);

create procedure if not exists db_commerce_tech.add_vendas(av_data_venda date, av_produto varchar(100), av_vendedor varchar(100), av_quantidade int, av_valor_total decimal(10,2))
    begin
        insert into db_commerce_tech.vendas(data_venda, produto, vendedor, quantidade, valor_total)
            values(av_data_venda, av_produto, av_vendedor, av_quantidade, av_valor_total);
    end;

call db_commerce_tech.add_vendas('2025-08-15', 'Notebook', 'Alice', 2, 2500.00);
call db_commerce_tech.add_vendas('2025-08-16', 'Smartphone', 'Bob', 5, 3000.00);
call db_commerce_tech.add_vendas('2025-08-17', 'Tablet', 'Carlos', 3, 1500.00);
call db_commerce_tech.add_vendas('2025-08-18', 'Monitor', 'Charlie', 4, 800.00);
call db_commerce_tech.add_vendas('2025-08-19', 'Headphones', 'Antônio', 6, 600.00);
call db_commerce_tech.add_vendas('2025-08-20', 'Teclado', 'Thomas', 7, 350.00);                    
call db_commerce_tech.add_vendas('2025-08-21', 'Mouse', 'Michael', 8, 400.00);
call db_commerce_tech.add_vendas('2025-08-22', 'Webcam', 'Maria', 2, 200.00);
call db_commerce_tech.add_vendas('2025-08-23', 'Mesa Gamer', 'Felipe', 1, 150.00);
call db_commerce_tech.add_vendas('2025-08-24', 'Cadeira Gamer', 'Gustavo', 3, 300.00);
call db_commerce_tech.add_vendas('2025-08-25', 'Cadeira Gamer', 'Gustavo', 3, 200.00);

select * from db_commerce_tech.vendas;

create view if not exists db_commerce_tech.vendas_mais_recentes as
SELECT v.id_venda, v.data_venda, v.produto, v.vendedor, ROW_NUMBER() OVER (ORDER BY data_venda DESC) AS numero_venda
    FROM db_commerce_tech.vendas v;

select * from db_commerce_tech.vendas_mais_recentes;

create view if not exists db_commerce_tech.numero_venda_por_vendedor as
    SELECT v.id_venda, v.data_venda, v.produto, v.vendedor, ROW_NUMBER() OVER (PARTITION BY vendedor ORDER BY data_venda DESC) AS numero_venda_por_vendedor
        FROM db_commerce_tech.vendas v;

select * from db_commerce_tech.numero_venda_por_vendedor;

create view if not exists db_commerce_tech.venda_de_maior_valor_de_cada_produto as with vendas_ordenadas as (
    select v.id_venda, v.data_venda, v.produto, v.vendedor, v.valor_total, row_number() over (partition by produto order by produto, valor_total desc) as numero_venda_por_produto
        from db_commerce_tech.vendas v)
            select id_venda, data_venda, produto, vendedor, valor_total
                from vendas_ordenadas
                    where numero_venda_por_produto = 1;

select * from db_commerce_tech.venda_de_maior_valor_de_cada_produto;

