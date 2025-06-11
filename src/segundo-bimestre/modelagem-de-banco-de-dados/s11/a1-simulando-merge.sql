create database if not exists bd_simulando_merge;

create table if not exists bd_simulando_merge.produtos (
    produto_id int auto_increment primary key,
    nome varchar(50) not null,
    quantidade int not null
);

create table if not exists bd_simulando_merge.inventario (
    produto_id int primary key,
    nome varchar(50) not null,
    quantidade int not null,
    foreign key (produto_id) references bd_simulando_merge.produtos(produto_id)
);

insert into bd_simulando_merge.produtos (nome, quantidade) values
('Produto C', 30),
('Produto D', 40);

insert into bd_simulando_merge.inventario (produto_id, nome, quantidade) values
(1, 'Produto C', 30),
(2, 'Produto D', 40);

select * from bd_simulando_merge.produtos;
select * from bd_simulando_merge.inventario;

/* Simulando o MERGE com INSERT ... ON DUPLICATE KEY UPDATE (upsert)*/
insert into bd_simulando_merge.inventario (produto_id, nome, quantidade)
    values (1, 'Produto A', 35), (2, 'Produto B', 45)
        on duplicate key update
            quantidade = values(quantidade), nome = values(nome);

/* Deletar registros que não estão na tabela de origem */
DELETE i FROM bd_simulando_merge.inventario i
    LEFT JOIN bd_simulando_merge.produtos p ON i.produto_id = p.produto_id
        WHERE p.produto_id IS NULL;

