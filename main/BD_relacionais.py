import sqlite3

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
"""

cursor.execute(create_table)
conn.commit()

produto = ('Camisa', 19.99, 50)
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES(?,?,?)"
cursor.execute(inserir_produto, produto)
conn.commit()


selecionar_produtos = "SELECT * FROM Produtos"
cursor.execute(selecionar_produtos)

novo_preco = 23.99
produto_id = 3
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
conn.execute(atualizar_preco, (novo_preco, produto_id))
conn.commit()
produtos = cursor.fetchall()
produto_id = 3
excluir_produto = "DELETE FROM Produtos WHERE id = ?"
cursor.execute(excluir_produto, (produto_id,))
conn.commit()



for p in produtos:
    print(p)