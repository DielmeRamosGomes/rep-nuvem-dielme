create table if not exists vendas(
    id_venda int auto_increment primary key,
    produto varchar(100) not null,
    quantidade int not null,
    valor_unitario int not null,
    data_venda date not null
);

insert into vendas(id_venda, produto, quantidade, valor_unitario, data_venda)
    values(default, "cama", 6, 600, "2025-03-25");

update vendas set produto = "cadeira" where id_venda = 3;

SELECT COUNT(*) AS total_vendas FROM vendas WHERE data_venda 
    BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND 
        LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH));


select * from vendas;