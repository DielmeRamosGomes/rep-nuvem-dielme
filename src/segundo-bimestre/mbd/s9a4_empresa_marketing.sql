CREATE TABLE bd_empresa_marketing.Campanhas (
    id_campanha INT PRIMARY KEY,
    nome_campanha VARCHAR(100),
    data_inicio DATE,
    data_fim DATE
);

CREATE TABLE bd_empresa_marketing.Anuncios (
    id_anuncio INT PRIMARY KEY,
    id_campanha INT,
    nome_anuncio VARCHAR(100),
    cliques INT,
    impressoes INT,
    FOREIGN KEY (id_campanha) REFERENCES Campanhas(id_campanha)
);

CREATE TABLE bd_empresa_marketing.Clientes (
    id_cliente INT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE bd_empresa_marketing.Interacoes (
    id_interacao INT PRIMARY KEY,
    id_anuncio INT,
    id_cliente INT,
    data_interacao DATE,
    tipo_interacao VARCHAR(50),
    FOREIGN KEY (id_anuncio) REFERENCES Anuncios(id_anuncio),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

INSERT INTO bd_empresa_marketing.Campanhas (id_campanha, nome_campanha, data_inicio, data_fim) VALUES
(1, 'Campanha de Verão', '2024-01-15', '2024-03-15'),
(2, 'Campanha de Inverno', '2024-06-01', '2024-08-01'),
(3, 'Campanha de Outono', '2024-09-01', '2024-11-01');

INSERT INTO bd_empresa_marketing.Anuncios (id_anuncio, id_campanha, nome_anuncio, cliques, impressoes) VALUES
(1, 1, 'Anuncio Verão 1', 1200, 5000),
(2, 1, 'Anuncio Verão 2', 1500, 7000),
(3, 2, 'Anuncio Inverno 1', 1000, 4000),
(4, 2, 'Anuncio Inverno 2', 800, 3500),
(5, 3, 'Anuncio Outono 1', 500, 2000);

INSERT INTO bd_empresa_marketing.Clientes (id_cliente, nome_cliente, email) VALUES
(1, 'João Silva', 'joao@email.com'),
(2, 'Maria Oliveira', 'maria@email.com'),
(3, 'Carlos Santos', 'carlos@email.com');

INSERT INTO bd_empresa_marketing.Interacoes (id_interacao, id_anuncio, id_cliente, data_interacao, tipo_interacao) VALUES
(1, 1, 1, '2024-01-20', 'clique'),
(2, 1, 2, '2024-01-21', 'compartilhamento'),
(3, 2, 1, '2024-01-25', 'clique'),
(4, 3, 3, '2024-06-05', 'clique'),
(5, 4, 2, '2024-06-10', 'clique'),
(6, 5, 1, '2024-09-15', 'clique');

-- 1) análise de indexação 
SELECT 
    c.nome_campanha, 
    a.nome_anuncio, 
    COUNT(i.id_interacao) AS total_interacoes
FROM 
    Campanhas c
JOIN 
    Anuncios a ON c.id_campanha = a.id_campanha
JOIN 
    Interações i ON a.id_anuncio = i.id_anuncio
WHERE 
    c.data_inicio >= '2024-01-01' 
    AND c.data_fim <= '2024-12-31'
GROUP BY 
    c.nome_campanha, a.nome_anuncio;

/* Identifique as colunas que poderiam se beneficiar de 
indexação para otimizar a consulta.
Crie os índices apropriados e justifique sua escolha. */

-- resposta
 /*A consulta filtra a tabela Campanhas nas colunas 
 data_inicio e data_fim. Criar um índice composto nessas 
 duas colunas pode otimizar a filtragem, especialmente 
 quando a 
 consulta abrange um grande intervalo de datas.*/
CREATE INDEX idx_campanhas_data ON Campanhas(data_inicio, data_fim);

/* Embora a coluna id_campanha seja uma chave estrangeira e 
já tenha um índice associado à chave primária de Campanhas, 
a consulta faz um JOIN entre as tabelas Anuncios e Campanhas 
usando essa coluna. Então, um índice separado pode ajudar 
a acelerar a busca de anúncios para uma campanha específica.*/

CREATE INDEX idx_anuncios_id_campanha ON Anuncios(id_campanha);

/* A coluna id_anuncio é usada no JOIN entre as tabelas Anuncios e Interacoes. Um índice sobre essa coluna ajudará a 
acelerar o JOIN e a contagem de interações por anúncio.*/
CREATE INDEX idx_interacoes_id_anuncio ON Interacoes(id_anuncio);

