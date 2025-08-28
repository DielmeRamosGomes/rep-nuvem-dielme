create database if not exists db_product;

create table if not exists db_product.product(
    id int auto_increment primary key,
    nome varchar(100) not null,
    preco decimal(10, 2) not null
);

CREATE PROCEDURE IF NOT EXISTS db_product.PRODUCT_REGISTER(pr_nome varchar(100), pr_preco decimal(10, 2))
    BEGIN
        INSERT INTO db_product.product(nome, preco)
            VALUES(pr_nome, pr_preco);
    END;

select * from db_product.product;


