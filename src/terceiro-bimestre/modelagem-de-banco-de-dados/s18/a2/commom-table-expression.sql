create database db_analytics;

create table if not exists db_analytics.funcionarios(
    id_func int auto_increment primary key,
    nome varchar(100) not null,
    id_supervisor int not null 
);

create table if not exists db_analytics.vendas(
    id_venda int auto_increment primary key,
    id_func int not null,
    valor_venda decimal(10, 2) not null,
    data_venda date not null,
    foreign key (id_func) references db_analytics.funcionarios(id_func) 
);

create procedure if not exists db_analytics.add_funcionario(af_nome varchar(100), af_id_supervisor int)
    begin
        insert into db_analytics.funcionarios(nome, id_supervisor)
            values(af_nome, af_id_supervisor); 
    end;

call db_analytics.add_funcionario("Carlos", 2);
call db_analytics.add_funcionario("Claudio", 3);
call db_analytics.add_funcionario("Ana", 4);
call db_analytics.add_funcionario("Maria", 5);
call db_analytics.add_funcionario("Roberto", 1);

select * from db_analytics.funcionarios;

create procedure if not exists db_analytics.add_vendas(av_id_func int, av_valor_venda decimal(10, 2), av_data_venda date)
    begin
        insert into db_analytics.vendas(id_func, valor_venda, data_venda)
            values(av_id_func, av_valor_venda, av_data_venda);
    end;

call db_analytics.add_vendas(1, 4000.00, "2025-09-15");
call db_analytics.add_vendas(1, 3000.00, "2025-09-14");
call db_analytics.add_vendas(1, 5000.00, "2025-09-13");
call db_analytics.add_vendas(1, 6000.00, "2025-09-12");
call db_analytics.add_vendas(1, 7000.00, "2025-09-10");
call db_analytics.add_vendas(1, 8000.00, "2025-09-09");
call db_analytics.add_vendas(1, 9000.00, "2025-09-08");
call db_analytics.add_vendas(1, 2000.00, "2025-09-07");
call db_analytics.add_vendas(1, 1000.00, "2025-09-06");
call db_analytics.add_vendas(2, 1000.00, "2025-09-05");
call db_analytics.add_vendas(2, 2000.00, "2025-09-04");

select * from db_analytics.vendas;

create view if not exists db_analytics.total_vendas_func as
    with total_vendas as (
        select v.id_func, sum(v.valor_venda) as total
            from db_analytics.vendas v
                group by v.id_func
    )
    select f.nome, tv.total
        from db_analytics.funcionarios f
            join total_vendas tv on f.id_func = tv.id_func;

select * from db_analytics.total_vendas_func;