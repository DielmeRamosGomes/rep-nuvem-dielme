create database if not exists db_data_soft;

create table
    db_data_soft.clientes (
        id_cliente int auto_increment primary key,
        nome varchar(100) not null,
        email varchar(100) not null unique,
        data_cadastro date
    );

create table
    db_data_soft.pedidos (
        id_pedido int auto_increment primary key,
        id_cliente int not null,
        data_pedido date not null,
        status varchar(20) not null,
        foreign key (id_cliente) references clientes (id_cliente)
    );

create table
    db_data_soft.auditoria_pedidos (
        id_auditoria int auto_increment primary key,
        id_pedido int not null,
        id_cliente int not null,
        data_pedido date not null,
        status varchar(20) not null,
        data_atualizacao datetime not null,
        foreign key (id_pedido) references pedidos (id_pedido),
        foreign key (id_cliente) references clientes (id_cliente)
    );

insert into
    db_data_soft.clientes (nome, email, data_cadastro)
values
    ('João Silva', 'joao@exemplo.com', '2025-06-20'),
    ('Maria Oliveira', 'maria@exemplo', '2025-06-21');

insert into
    db_data_soft.pedidos (id_cliente, data_pedido, status)
values
    (1, '2025-06-20', 'Pendente'),
    (1, '2025-06-20', 'Pendente'),
    (2, '2025-06-21', 'Pendente'),
    (2, '2025-06-21', 'Pendente');

select * from db_data_soft.clientes;
select * from db_data_soft.pedidos;
select * from db_data_soft.auditoria_pedidos;

delete from db_data_soft.clientes where id_cliente = 2;

update db_data_soft.pedidos set status = 'Entregue' where id_cliente = 1;

-- exclusão automatizada de pedidos quando o cliente for excluído
create trigger db_data_soft.trg_excluir_pedidos before delete on db_data_soft.clientes for each row begin
delete from db_data_soft.pedidos
where
    id_cliente = old.id_cliente;

end;

-- auditoria de atualizações de pedidos
create trigger db_data_soft.trg_atualizar_pedidos before
update on db_data_soft.pedidos for each row begin
insert into
    db_data_soft.auditoria_pedidos (
        id_pedido,
        id_cliente,
        data_pedido,
        status,
        data_atualizacao
    )
values
    (
        old.id_pedido,
        old.id_cliente,
        old.data_pedido,
        new.status,
        now ()
    );

end;