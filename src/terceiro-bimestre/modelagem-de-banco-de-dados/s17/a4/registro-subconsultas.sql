create database if not exists db_ecommerce;

create table if not exists db_ecommerce.clientes(
    id int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) unique not null
);

create table if not exists db_ecommerce.compras(
    id int auto_increment primary key,
    id_cliente int not null,
    valor_total decimal(10, 2) not null,
    data_compra date not null,
    foreign key (id_cliente) references db_ecommerce.clientes(id)
);

create procedure if not exists db_ecommerce.add_clientes(ac_nome varchar(100), ac_email varchar(100))
    begin
        insert into db_ecommerce.clientes(nome, email)
            values(ac_nome, ac_email);
    end;

call db_ecommerce.add_clientes('Roberto', 'roberto@exemplo.com');
call db_ecommerce.add_clientes('Michael', 'michael@exemplo.com');

select * from db_ecommerce.clientes;

create procedure if not exists db_ecommerce.add_compras(ac_id_cliente int, ac_valor_total decimal(10, 2), ac_data_compra date)
    begin
        insert into db_ecommerce.compras(id_cliente, valor_total, data_compra)
            values(ac_id_cliente, ac_valor_total, ac_data_compra);
    end;

call db_ecommerce.add_compras(1, 999.99, '2025-08-25');
call db_ecommerce.add_compras(1, 500.50, '2025-08-26');

call db_ecommerce.add_compras(2, 600.48, '2025-08-25');
call db_ecommerce.add_compras(2, 399.99, '2025-08-26');

select * from db_ecommerce.compras;

/*1. Subconsulta em SELECT – Qual o total de compras por cliente?*/

create view if not exists db_ecommerce.total_compras_por_cliente as
    select c.nome as cliente, (select sum(valor_total) 
        from db_ecommerce.compras co 
            where co.id_cliente = c.id) as total_compras
                from db_ecommerce.clientes c
                    group by cliente;

select * from db_ecommerce.total_compras_por_cliente;

/*2. Subconsulta em WHERE – Quais clientes gastaram acima da média?*/
create view if not exists db_ecommerce.clientes_acima_da_media as
    select c.nome as cliente, (select sum(valor_total)
        from db_ecommerce.compras co 
            where co.id_cliente = c.id) as total_compras
                from db_ecommerce.clientes c
                    group by cliente
                        having total_compras > (select avg(valor_total)
                            from db_ecommerce.compras);

select * from db_ecommerce.clientes_acima_da_media;

/*3. Subconsulta em FROM – Relatório com total de compras por cliente acima da média geral*/



