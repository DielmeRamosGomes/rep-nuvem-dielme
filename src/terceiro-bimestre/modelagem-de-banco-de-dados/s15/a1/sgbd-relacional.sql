create database if not exists db_tech_solutions;

create table
    if not exists db_tech_solutions.clientes (
        id int auto_increment primary key,
        nome varchar(100) not null,
        email varchar(100) not null unique,
        senha varchar(100) not null
    );

create table
    if not exists db_tech_solutions.produtos (
        id int auto_increment primary key,
        nome varchar(100) not null,
        descricao varchar(255),
        preco_unitario decimal(5, 2) not null
    );

create table
    if not exists db_tech_solutions.vendas (
        id int auto_increment primary key,
        cliente_id int not null,
        data_venda datetime not null,
        foreign key (cliente_id) references db_tech_solutions.clientes (id)
    );

create table
    if not exists db_tech_solutions.item_venda (
        id int auto_increment primary key,
        produto_id int not null,
        venda_id int not null,
        quantidade int not null,
        foreign key (venda_id) references db_tech_solutions.vendas (id),
        foreign key (produto_id) references db_tech_solutions.produtos (id)
    );

create table
    if not exists db_tech_solutions.endereco (
        id int auto_increment primary key,
        cliente_id int not null,
        rua varchar(100) not null,
        numero varchar(10) not null,
        cidade varchar(50) not null,
        estado varchar(50) not null,
        cep varchar(10) not null,
        foreign key (cliente_id) references db_tech_solutions.clientes (id)
    );

create procedure if not exists db_tech_solutions.adicionar_cliente (
    in ac_nome varchar(100),
    in ac_email varchar(100),
    in ac_senha varchar(100)
) begin
insert into
    db_tech_solutions.clientes (nome, email, senha)
values
    (ac_nome, ac_email, ac_senha);

end;

call db_tech_solutions.adicionar_cliente ('Dielme Ramos', 'dielme@exemplo.com', '123456');

select
    *
from
    db_tech_solutions.clientes;

create procedure if not exists db_tech_solutions.adicionar_produto (
    in ap_nome varchar(100),
    in ap_descricao varchar(255),
    in ap_preco_unitario decimal(5, 2)
) begin
insert into
    db_tech_solutions.produtos (nome, descricao, preco_unitario)
values
    (ap_nome, ap_descricao, ap_preco_unitario);

end;

call db_tech_solutions.adicionar_produto ('Cadeira', 'Cadeira Gamer', 500.00);

select
    *
from
    db_tech_solutions.produtos;

create procedure if not exists db_tech_solutions.realizar_venda (in rv_cliente_id int, in rv_data_venda datetime) begin
insert into
    db_tech_solutions.vendas (cliente_id, data_venda)
values
    (rv_cliente_id, rv_data_venda);

end;

call db_tech_solutions.realizar_venda (1, '2025-08-05 10:00:00');

call db_tech_solutions.realizar_venda (1, '2025-08-06 11:00:00');

select
    *
from
    db_tech_solutions.vendas;

create procedure if not exists db_tech_solutions.adicionar_item_venda (
    in aiv_produto_id int,
    in aiv_venda_id int,
    in aiv_quantidade int
) begin
insert into
    db_tech_solutions.item_venda (produto_id, venda_id, quantidade)
values
    (aiv_produto_id, aiv_venda_id, aiv_quantidade);

end;

call db_tech_solutions.adicionar_item_venda (1, 1, 2);

call db_tech_solutions.adicionar_item_venda (2, 1, 3);

select
    *
from
    db_tech_solutions.item_venda;

create procedure if not exists db_tech_solutions.adicionar_endereco (
    in ae_cliente_id int,
    in ae_rua varchar(100),
    in ae_numero varchar(10),
    in ae_cidade varchar(50),
    in ae_estado varchar(50),
    in ae_cep varchar(10)
) begin
insert into
    db_tech_solutions.endereco (cliente_id, rua, numero, cidade, estado, cep)
values
    (
        ae_cliente_id,
        ae_rua,
        ae_numero,
        ae_cidade,
        ae_estado,
        ae_cep
    );

end;

call db_tech_solutions.adicionar_endereco (
    1,
    'Rua Exemplo',
    '123',
    'Cidade Exemplo',
    'Estado Exemplo',
    '12345-678'
);

call db_tech_solutions.adicionar_endereco (
    1,
    'Avenida Teste',
    '456',
    'Outra Cidade',
    'Outro Estado',
    '87654-321'
);

select
    *
from
    db_tech_solutions.endereco;

create procedure if not exists db_tech_solutions.obter_vendas_por_cliente (in ovpc_cliente_id int) begin
select
    v.id as venda_id,
    v.data_venda,
    c.nome as cliente_nome,
    i.quantidade,
    p.nome as produto_nome,
    p.preco_unitario
from
    db_tech_solutions.vendas v
    join db_tech_solutions.clientes c on v.cliente_id = c.id
    join db_tech_solutions.item_venda i on v.id = i.venda_id
    join db_tech_solutions.produtos p on i.produto_id = p.id
where
    c.id = ovpc_cliente_id;

end;

call db_tech_solutions.obter_vendas_por_cliente (1);

create procedure if not exists db_tech_solutions.soma_total_de_uma_venda (in aux_venda_id int) begin
select
    v.id as venda_id,
    
    sum(i.quantidade * p.preco_unitario) as total
from
    db_tech_solutions.vendas v
    join db_tech_solutions.item_venda i on v.id = i.venda_id
    join db_tech_solutions.produtos p on i.produto_id = p.id
where
    v.id = aux_venda_id
group by
    total desc;

end;