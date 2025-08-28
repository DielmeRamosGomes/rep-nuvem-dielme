create database if not exists db_fast_tech;

CREATE TABLE if not exists
    db_fast_tech.pedidos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cliente VARCHAR(100),
        produto VARCHAR(100),
        quantidade INT,
        valor DECIMAL(10, 2),
        status VARCHAR(20) DEFAULT 'Pendente'
    );

create procedure if not exists db_fast_tech.add_pedidos(ap_cliente VARCHAR(100), ap_produto VARCHAR(100), ap_quantidade INT, ap_valor DECIMAL(10, 2))
    begin
        insert into db_fast_tech.pedidos(cliente, produto, quantidade, valor)
            values(ap_cliente, ap_produto, ap_quantidade, ap_valor);
    end;

-- Simulando transação que falha com o rollback
start transaction;
    call db_fast_tech.add_pedidos('Carlos', 'TV', 1, 4500.99);
    rollback;

-- simulando transação que funciona com o commit
start transaction;
    call db_fast_tech.add_pedidos('Carlos', 'TV', 1, 4500.99);
    commit;

-- Simulação de falha e recuperação de dados
start transaction;
    call db_fast_tech.add_pedidos('Lucas', 'Tablet', 1, 999.99);
    call db_fast_tech.add_pedidos(null, 'Relógio', 3, 450.99);
    rollback;


select * from db_fast_tech.pedidos;