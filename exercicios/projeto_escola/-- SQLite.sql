-- SQLite
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
);


--INSERT INTO alunos (nome, sobrenome, idade, curso) VALUES ('Lucas', 'Oliveira', 19, 'Automação'),
 --('Mariana', 'Santos', 21, 'Desenvolvimento'),('Pedro', 'Almeida', 20, 'Automação'),('Beatriz', 'Lima', 22, 'Mecatrônica'),('Gabriel', 'Ferreira', 19, 'Desenvolvimento'),('Julia', 'Costa', 23, 'Automação'),('Rafael', 'Pereira', 20, 'Mecatrônica'),('Larissa', 'Rodrigues', 21, 'Desenvolvimento'),('Thiago', 'Souza', 19, 'Automação'),('Isabela', 'Gomes', 22, 'Desenvolvimento'),('Mateus', 'Martins', 20, 'Automação'),('Fernanda', 'Araújo', 24, 'Mecatrônica'),('Bruno', 'Cardoso', 21, 'Desenvolvimento'),('Camila', 'Melo', 19, 'Automação'),('Vinícius', 'Teixeira', 22, 'Mecatrônica'),('Letícia', 'Ribeiro', 20, 'Desenvolvimento'),('Diego', 'Carvalho', 23, 'Automação'),('Amanda', 'Pinto', 21, 'Mecatrônica'),('Igor', 'Cavalcanti', 19, 'Desenvolvimento'),('Bárbara', 'Barbosa', 22, 'Automação');


--SELECT * FROM alunos;

CREATE TABLE disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_materia TEXT,
    carga_horaria INTEGER,
    professor TEXT,
    area_tecnica TEXT
);

--INSERT INTO disciplinas (nome_materia, carga_horaria, professor, area_tecnica) VALUES 
--('Lógica de Programação', 80, 'Carlos Silva', 'TI'),
--('Eletricidade Industrial', 120, 'Roberto Souza', 'Elétrica'),
--('Instrumentação', 60, 'Marta Rocha', 'Automação'),
--('Banco de Dados', 40, 'Carlos Silva', 'TI'),
--('Sistemas Digitais', 60, 'Ana Paula', 'Eletrônica'),
--('Python Estruturado', 80, 'Carlos Silva', 'TI'),
--('CLP Avançado', 100, 'Marcos Lima', 'Automação'),
--('Pneumática', 40, 'João Pedro', 'Mecânica'),
--('Redes Industriais', 60, 'Marta Rocha', 'Automação'),
--('Desenvolvimento Web', 80, 'Ana Paula', 'TI'),
--('Robótica', 100, 'Marcos Lima', 'Mecatrônica'),
--('Eletrônica de Potência', 80, 'Roberto Souza', 'Elétrica'),
--('Cálculo Técnico', 40, 'João Pedro', 'Geral'),
--('Segurança em Eletricidade', 20, 'Roberto Souza', 'Elétrica'),
--('Interface IHM', 40, 'Marta Rocha', 'Automação'),
--('Estrutura de Dados', 60, 'Carlos Silva', 'TI'),
--('Comandos Elétricos', 100, 'Roberto Souza', 'Elétrica'),
--('Microcontroladores', 80, 'Ana Paula', 'Eletrônica'),
--('Sensores Industriais', 40, 'Marcos Lima', 'Automação'),
--('Gestão de Projetos', 40, 'João Pedro', 'Geral');

--SELECT * FROM disciplinas;

CREATE TABLE salas_aula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_sala INTEGER,
    bloco TEXT,
    capacidade INTEGER,
    tipo_laboratorio TEXT
);

--INSERT INTO salas_aula (numero_sala, bloco, capacidade, tipo_laboratorio) VALUES 
--(101, 'Bloco A', 30, 'Teoria'),
--(102, 'Bloco A', 25, 'Informática'),
--(103, 'Bloco A', 20, 'Automação'),
--(201, 'Bloco B', 30, 'Teoria'),
--(202, 'Bloco B', 25, 'Informática'),
--(203, 'Bloco B', 15, 'Eletrônica'),
--(204, 'Bloco B', 20, 'Elétrica'),
--(301, 'Bloco C', 40, 'Auditório'),
--(302, 'Bloco C', 20, 'Mecânica'),
--(303, 'Bloco C', 20, 'Mecatrônica'),
--(104, 'Bloco A', 30, 'Teoria'),
--(105, 'Bloco A', 25, 'Informática'),
--(205, 'Bloco B', 20, 'Automação'),
--(206, 'Bloco B', 25, 'Informática'),
--(304, 'Bloco C', 20, 'Pneumática'),
--(305, 'Bloco C', 20, 'Robótica'),
--(106, 'Bloco A', 30, 'Teoria'),
--(207, 'Bloco B', 25, 'Informática'),
--(208, 'Bloco B', 15, 'Eletrônica'),
--(306, 'Bloco C', 20, 'Automação');

--SELECT * FROM salas_aula;

-- 1. Alunos de Automação
SELECT * FROM alunos WHERE curso = 'Automação';

-- 2. Disciplinas de TI
SELECT * FROM disciplinas WHERE area_tecnica = 'TI';

-- 3. Salas do Bloco B
SELECT * FROM salas_aula WHERE bloco = 'Bloco B';


-- 1. Seleção específica de colunas de alunos
SELECT nome, sobrenome FROM alunos WHERE idade > 22;

-- 2. Seleção específica de disciplinas
SELECT nome_materia, professor FROM disciplinas WHERE carga_horaria = 80;

-- 3. Seleção específica de salas
SELECT numero_sala, tipo_laboratorio FROM salas_aula WHERE bloco = 'Bloco C';
