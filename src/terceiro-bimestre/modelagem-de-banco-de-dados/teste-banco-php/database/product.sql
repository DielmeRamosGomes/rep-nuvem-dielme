create database if not exists db_product;

create table if not exists db_product.product(
    id int primary key,
    nome varchar(100) not null,
    preco decimal(10, 2) not null
);

CREATE PROCEDURE IF NOT EXISTS db_product.PRODUCT_REGISTER(pr_id int, pr_nome varchar(100), pr_preco decimal(10, 2))
    BEGIN
        INSERT INTO db_product.product(id, nome, preco)
            VALUES(pr_id, pr_nome, pr_preco);
    END;

select * from db_product.product;

