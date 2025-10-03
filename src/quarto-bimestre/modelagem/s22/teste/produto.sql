create database if not exists db_estoque;

create table if not exists db_estoque.produtos(
    id int auto_increment primary key,
    nome varchar(100) not null,
    imagem varchar(600) not null
);

create procedure if not exists db_estoque.add_produto(
    ap_nome varchar(100),
    ap_imagem varchar(600)
)
begin
    insert into db_estoque.produtos(nome, imagem)
        values(ap_nome, ap_imagem);
end;

call db_estoque.add_produto("Computador01", "src\quarto-bimestre\modelagem\s22\teste\assets\pc01.jpg");

select * from db_estoque.produtos;
