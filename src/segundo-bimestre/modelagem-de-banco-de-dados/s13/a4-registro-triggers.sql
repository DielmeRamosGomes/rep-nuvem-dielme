create database if not exists db_data_soft;

create table clientes(
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    data_cadastro date
);

create table pedidos(
    id_pedido int auto_increment primary key,
    id_cliente int not null,
    data_pedido date not null,
    status varchar(20) not null,
    foreign key (id_cliente) references clientes(id_cliente)
);

-- exclusão automatzada de de pedidos quando o cliente for excluído

create trigger trg_excluir_pedidos
before delete on clientes
for each row
begin
    delete from pedidos where id_cliente = old.id_cliente;
end;






