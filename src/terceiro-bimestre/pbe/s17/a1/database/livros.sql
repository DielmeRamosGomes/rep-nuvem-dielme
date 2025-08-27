create database if not exists db_livros;

create table if not exists db_livros.livros(
    id int auto_increment primary key,
    nome varchar(100) not null,
    editora varchar(100) not null,
    ano date not null
);

create procedure if not exists db_livros.add_livro(al_nome varchar(100), al_editora varchar(100), al_ano date)
    begin
        insert into db_livros.livros(nome, editora, ano) 
            values (al_nome, al_editora, al_ano);
    end;

create view if not exists db_livros.mostrar_livros as
    select * from db_livros.livros;

select * from db_livros.mostrar_livros;

