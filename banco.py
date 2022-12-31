import sqlite3

caminho = 'agenda_usuarios.db'

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect(caminho)
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(30),
        idade VARCHAR(4),
        cidade VARCHAR(14),
        telefone VARCHAR(14),
        email VARCHAR(30)
        );
        """)
        self.conexao.commit()
        c.close()
        return 'Tabela criada com sucesso'

tb = Banco()
tb.createTable()
