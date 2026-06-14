-- SQLite
CREATE TABLE ativos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag TEXT NOT NULL,
    status TEXT DEFAULT 'Operacional',
    criticidade TEXT,
    horas_uso INTEGER
);

--INSERT INTO ativos (tag, criticidade, horas_uso) VALUES 
--('MOT-001', 'Alta', 1200), ('MOT-002', 'Média', 800),
--('INV-001', 'Alta', 450), ('SEN-001', 'Baixa', 1500),
--('PLC-001', 'Alta', 200), ('VLV-001', 'Média', 3000),
--('MOT-003', 'Alta', 50), ('SEN-002', 'Baixa', 900),
--('INV-002', 'Média', 1100), ('PLC-002', 'Alta', 350),
--('MOT-004', 'Baixa', 5000), ('SEN-003', 'Média', 200),
--('VLV-002', 'Alta', 150), ('MOT-005', 'Média', 700),
--('PLC-003', 'Alta', 10), ('SEN-004', 'Baixa', 2500),
--('INV-003', 'Alta', 600), ('MOT-006', 'Baixa', 4000),
--('VLV-003', 'Média', 850), ('SEN-005', 'Alta', 100);

CREATE TABLE manutencao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tecnico TEXT,
    data_servico TEXT,
    custo REAL,
    tipo TEXT
);

--INSERT INTO manutencao (tecnico, data_servico, custo, tipo) VALUES 
--('Ricardo', '2026-01-10', 500.00, 'Preventiva'), ('Alice', '2026-01-12', 1200.00, 'Corretiva'),
--('Ricardo', '2026-01-15', 300.00, 'Preventiva'), ('Marcos', '2026-01-16', 2500.00, 'Corretiva'),
--('Alice', '2026-01-18', 450.00, 'Preventiva'), ('Ricardo', '2026-01-20', 1500.00, 'Corretiva'),
--('Marcos', '2026-01-22', 600.00, 'Preventiva'), ('Alice', '2026-01-25', 900.00, 'Corretiva'),
--('Ricardo', '2026-01-28', 550.00, 'Preventiva'), ('Marcos', '2026-01-30', 3000.00, 'Corretiva'),
--('Alice', '2₀₂₆-₀₂-₀₁', 4₀₀.₀₀, 'Preventiva'), ('Ricardo', '2₀₂₆-₀₂-₀₃', 18₀₀.₀₀, 'Corretiva'),
--('Marcos', '2026-02-05', 700.00, 'Preventiva'), ('Alice', '2026-02-08', 2200.00, 'Corretiva'),
--('Ricardo', '2026-02-10', 350.00, 'Preventiva'), ('Marcos', '2026-02-12', 4000.00, 'Corretiva'),
--('Alice', '2026-02-14', 650.00, 'Preventiva'), ('Ricardo', '2026-02-16', 1100.00, 'Corretiva'),
--('Marcos', '2026-02-18', 800.00, 'Preventiva'), ('Alice', '2026-02-20', 2800.00, 'Corretiva');



-- DQL: Soma de custos corretivos
--SELECT SUM(custo) AS Total_Corretivas 
--FROM manutencao 
--WHERE tipo = 'Corretiva';

-- 1. Excluir tabela existente
--DROP TABLE ativos;

-- 2. Recriar com nova estrutura
CREATE TABLE ativos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag TEXT NOT NULL UNIQUE,
    setor TEXT, -- Coluna nova
    status TEXT DEFAULT 'Operacional',
    criticidade TEXT,
    horas_uso INTEGER
);

-- 3. Inserir (adaptando o INSERT anterior com o setor)
--INSERT INTO ativos (tag, setor, criticidade, horas_uso) VALUES ('MOT-001', 'Produção', 'Alta', 1200);

-- Comando para gerar os dados da exportação
--SELECT tag, setor, horas_uso 
--FROM ativos 
--WHERE horas_uso > 1000;

-- Query para o relatório
--SELECT tecnico, data_servico, custo 
--FROM manutencao 
--WHERE custo > 2000 
--ORDER BY custo DESC;

-- Ação no Notion:
-- Crie uma base de dados no Notion e cole os resultados copiados do VS Code.