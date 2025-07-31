create database if not exists db_recuperacao;

create table if not exists db_recuperacao.clientes (
    id int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    idade int not null
);

create table if not exists db_recuperacao.enderecos(
    id_endereco int auto_increment primary key,
    id_cliente int not null,
    rua varchar(100) not null,
    numero int not null,
    bairro varchar(100) not null,
    cidade varchar(100) not null,
    estado varchar(100) not null,
    foreign key (id_cliente) references db_recuperacao.clientes(id)
);

insert into db_recuperacao.enderecos(rua, numero, bairro, cidade, estado, id_cliente)
    values("Rua A", 123, "Bairro A", "Cidade A", "Estado A", 1);

insert into db_recuperacao.clientes(nome, email, idade)
    values("Bolsonaro", "bolsonaro@exemplo.com", 17);


select * from db_recuperacao.enderecos;
select * from db_recuperacao.clientes;
select nome, email from db_recuperacao.clientes;

update db_recuperacao.clientes set idade = 70
    where id = 2 and email = "bolsonaro@exemplo.com";

update db_recuperacao.clientes set nome = "Dilma Rousseff"
    where id = 1 and email = "robson@exemplo.com";

update db_recuperacao.clientes set email = "dilma@exemplo.com"
    where id = 1;

update db_recuperacao.clientes set idade = 65
    where id = 1 and email = "dilma@exemplo.com";





