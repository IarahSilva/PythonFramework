-- SQLite
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL,
    estoque INTEGER
);

INSERT INTO produtos (nome, preco, estoque)
VALUES
('Mouse Gamer', 120.00, 25),
('Monitor 24 Polegadas', 899.90, 10),
('Headset Bluetooth', 199.90, 18),
('Webcam Full HD', 149.90, 12),
('Notebook i5', 3499.90, 8),
('Notebook i7', 4899.90, 5),
('SSD 240GB', 179.90, 30),
('SSD 480GB', 299.90, 20),
('HD Externo 1TB', 349.90, 14),
('Memória RAM 8GB', 159.90, 22),
('Memória RAM 16GB', 299.90, 16),
('Placa de Vídeo RTX 4060', 2499.90, 6),
('Fonte 600W', 289.90, 11),
('Gabinete Gamer', 399.90, 9),
('Mouse Pad Grande', 59.90, 40),
('Cadeira Gamer', 1199.90, 7),
('Impressora Multifuncional', 799.90, 8),
('Roteador Wi-Fi 6', 459.90, 13),
('Switch 8 Portas', 189.90, 15),
('Caixa de Som Bluetooth', 229.90, 17),
('Microfone USB', 279.90, 10),
('Smartphone Android', 1899.90, 12),
('Tablet 10 Polegadas', 1299.90, 9),
('Smartwatch', 599.90, 18),
('Carregador Portátil', 99.90, 35),
('Cabo HDMI 2m', 29.90, 50),
('Adaptador USB-C', 49.90, 28),
('Cooler para Notebook', 89.90, 21),
('Leitor de Cartão', 39.90, 30),
('Pen Drive 64GB', 44.90, 45);

-- Consultar tudo
SELECT * FROM produtos;

-- Consultar Filtro
SELECT * FROM produtos WHERE preco < 100.00;

-- Ordenar Resultados em ordem Crescente ou Decrescente
SELECT * FROM produtos ORDER BY preco DESC;

-- Alterar Informações
UPDATE produtos SET preco = 230.00 WHERE nome = 'Teclado Mecânico';

--Deletar Linha
DELETE FROM produtos WHERE id = 1;

--Adicionar Nova Coluna
ALTER TABLE produtos ADD COLUMN categoria TEXT;

-- Deletar todos os dados
DELETE FROM produtos;

-- Excluir Tabela(DROP)
DROP TABLE produtos;