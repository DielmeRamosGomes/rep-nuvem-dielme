create database if not exists db_livros;

create table if not exists db_livros.livros(
    id int auto_increment primary key,
    nome varchar(100) not null,
    editora varchar(100) not null,
    ano date not null
);


