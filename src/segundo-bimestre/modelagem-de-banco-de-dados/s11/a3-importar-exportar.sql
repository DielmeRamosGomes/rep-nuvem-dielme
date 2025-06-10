create database if not exists db_tech_dynamics;

CREATE TABLE db_tech_dynamics.produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(100) not null,
    preco DECIMAL(10,2) not null,
    estoque INT not null
);

-- Importando dados do arquivo CSV para a tabela produtos
load data infile 'D:\programas-no-visual-studio-code\\NodeJs\\rep-local-dielme\\src\\segundo-bimestre\\modelagem-de-banco-de-dados\\s11\\produtos.csv'
    into table db_tech_dynamics.produtos
        fields terminated by ','
            lines terminated by '\n'
                ignore 1 lines
                    (nome_produto, preco, estoque);

-- Exportando dados da tabela produtos para um arquivo CSV
select nome_produto, preco, estoque
    into outfile 'D:\programas-no-visual-studio-code\\NodeJs\\rep-local-dielme\\src\\segundo-bimestre\\modelagem-de-banco-de-dados\\s11\\produtos_exportados.csv'
        fields terminated by ','
            enclosed by ""
                lines terminated by '\n'
                    from db_tech_dynamics.produtos;

-- Exportando dados da tabela produtos para um arquivo xml
select 
    concat(
        '<produto>',
            '<id_produto>', id_produto, '</id_produto>',
            '<nome_produto>', nome_produto, '</nome_produto>',
            '<preco>', preco, '</preco>',
            '<estoque>', estoque, '</estoque>',
        '</produto>'
    ) as xml_output
        from db_tech_dynamics.produtos
            into outfile 'D:\programas-no-visual-studio-code\\NodeJs\\rep-local-dielme\\src\\segundo-bimestre\\modelagem-de-banco-de-dados\\s11\\produtos_exportados.xml';


select * from db_tech_dynamics.produtos;



