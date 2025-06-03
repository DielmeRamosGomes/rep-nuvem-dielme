create database if not exists bd_empresa_logistica;

use bd_empresa_logistica;

create table
    if not exists veiculos (
        id_veiculo int auto_increment primary key,
        modelo varchar(50) not null,
        ano int not null,
        capacidade_carga decimal(10, 2) not null
    );

create table
    if not exists entregas (
        id_entrega int auto_increment primary key,
        id_veiculo int not null,
        data_entrega date not null,
        cidade varchar(50) not null,
        peso_entrega decimal(10, 2) not null,
        foreign key (id_veiculo) references veiculos (id_veiculo)
    );

insert into
    veiculos (modelo, ano, capacidade_carga)
values
    ('Furgão', 2020, 2.00),
    ('Caminhão', 2018, 10.00),
    ('Van', 2019, 3.00),
    ('Carro', 2021, 1.00),
    ('Caminhonete', 2022, 4.00);

insert into
    entregas (id_veiculo, data_entrega, cidade, peso_entrega)
values
    (1, '2024-08-01', 'São Paulo', 8.00),
    (2, '2024-08-03', 'Rio de Janeiro', 12.00),
    (3, '2024-08-05', 'Brasília', 2.50),
    (1, '2024-08-06', 'Belo Horizonte', 9.50),
    (1, '2024-08-07', 'Salvador', 11.00),
    (4, '2024-08-10', 'São Paulo', 13.50),
    (2, '2024-08-12', 'Brasília', 2.00);

insert into entregas (id_veiculo, data_entrega, cidade, peso_entrega)
values(1, '2024-08-15', 'São Paulo', 5.5);

select
    *
from
    bd_empresa_logistica.veiculos;

select
    *
from
    bd_empresa_logistica.entregas;

/*3) Agrupar entregas por cidade com peso total de entregas acima de 15 toneladas (usando HAVING)*/
SELECT
    cidade,
    SUM(peso_entrega) AS total_peso
FROM
    bd_empresa_logistica.entregas
GROUP BY
    cidade
HAVING
    total_peso > 15.00;

/* 4) Identificar veículos com entregas acima de 10 toneladas no total (usando HAVING)*/
SELECT
    v.modelo,
    sum(e.peso_entrega) AS total_peso_entregas
FROM
    bd_empresa_logistica.veiculos v
    JOIN bd_empresa_logistica.entregas e ON v.id_veiculo = e.id_veiculo
GROUP BY
    v.modelo
HAVING
    total_peso_entregas > 10.0;

--soma todas as entregas da cidade de São Paulo por veiculo
SELECT v.modelo, SUM(peso_entrega) AS total_peso_sao_paulo
    FROM veiculos v 
        join entregas e on v.id_veiculo = e.id_veiculo
            WHERE e.cidade = 'São Paulo'
                GROUP BY v.modelo;

