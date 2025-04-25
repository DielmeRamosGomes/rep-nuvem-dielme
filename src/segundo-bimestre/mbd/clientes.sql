create database bd_clientes;

create table if not exists clientes(
    id int auto_increment primary key,
    nome varchar(100) not null,
    idade int not null
);

insert into clientes(cliente_id, cliente_nome, cliente_idade)
    values(default, "Carlos", 23);

select * from clientes;
select cliente_nome, cliente_idade from clientes;






