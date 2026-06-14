import sqlite3

# Conectando (ou criando) o banco de dados
conn = sqlite3.connect('sistema_vendas.db')
cursor = conn.cursor()

# Criando a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT,
    valor REAL,
    data TEXT,
    vendedor TEXT
)
''')

# Lista de 20 vendas para inserção automática
dados_vendas = [
    ('Sensor Laser', 450.0, '2026-04-01', 'Marcos'),
    ('CLP Siemens', 2800.0, '2026-04-02', 'Alice'),
    ('Cabo Ethernet 10m', 85.0, '2026-04-02', 'Ricardo'),
    ('Inversor CFW500', 1200.0, '2026-04-03', 'Marcos'),
    ('HMI Touch', 1500.0, '2026-04-05', 'Alice'),
    ('Relé de Segurança', 320.0, '2026-04-06', 'Ricardo'),
    ('Fonte 24VDC', 210.0, '2026-04-07', 'Marcos'),
    ('Motor de Passo', 400.0, '2026-04-08', 'Alice'),
    ('Driver Motor', 600.0, '2026-04-10', 'Ricardo'),
    ('Botão Emergência', 45.0, '2026-04-11', 'Marcos'),
    ('Torre Sinalizadora', 180.0, '2026-04-12', 'Alice'),
    ('Contator 220V', 120.0, '2026-04-14', 'Ricardo'),
    ('Disjuntor Motor', 95.0, '2026-04-15', 'Marcos'),
    ('Encoder Rotativo', 750.0, '2026-04-16', 'Alice'),
    ('Acoplador Óptico', 35.0, '2026-04-17', 'Ricardo'),
    ('Cabo Manga 4 vias', 12.0, '2026-04-18', 'Marcos'),
    ('Termopar Tipo J', 55.0, '2026-04-19', 'Alice'),
    ('Controlador PID', 890.0, '2026-04-20', 'Ricardo'),
    ('Válvula Solenóide', 240.0, '2026-04-21', 'Marcos'),
    ('Pressostato', 310.0, '2026-04-22', 'Alice')
]

# Inserindo os dados
cursor.executemany('INSERT INTO vendas (produto, valor, data, vendedor) VALUES (?, ?, ?, ?)', dados_vendas)

conn.commit()
conn.close()
print("Banco de dados criado e populado com sucesso!")