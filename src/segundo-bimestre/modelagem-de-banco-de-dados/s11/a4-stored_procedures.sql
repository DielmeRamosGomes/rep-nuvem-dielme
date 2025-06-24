create database if not exists db_loja_ecommerce;

create table
    if not exists db_loja_ecommerce.produtos (
        id int auto_increment primary key,
        nome varchar(100) not null,
        preco decimal(10, 2) not null,
        estoque int not null
    );

create procedure db_loja_ecommerce.atualizar_preco (in id_produto int, in percentual decimal(5, 2)) begin
update db_loja_ecommerce.produtos as p
set
    preco = preco + (preco * percentual / 100)
where
    p.id = id_produto;

end;

insert into
    db_loja_ecommerce.produtos (nome, preco, estoque)
values
    ('Computador', 3000.00, 50),
    ('Ventilador', 450.00, 30),
    ('Televisão', 4000.00, 20);

call db_loja_ecommerce.atualizar_preco (1, 50);

select
    *
from
    db_loja_ecommerce.produtos;