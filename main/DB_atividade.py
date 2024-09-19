import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Contatos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        numero TEXT
    )""")

dados_exemplo = [
    ('João', 'joao@email.com', '1111-2222'),
    ('Maria', 'maria@email.com', '3333-4444'),
    ('José', 'jose@email.com', '5555-6666'),
    ('Carla', 'carla@email.com', '7777-8888')
]

cursor.executemany("INSERT INTO Contatos(nome, email, numero) VALUES (?,?,?)", dados_exemplo)
conn.commit()

cursor.execute("SELECT * FROM Contatos")
contatos = cursor.fetchall()

novo_numero = '4002-8922'
contato_id = 2

cursor.execute("UPDATE Contatos SET numero = ? WHERE id = ?", (novo_numero, contato_id))
conn.commit()

id_para_excluir = 1
cursor.execute("DELETE FROM Contatos WHERE id=?", (id_para_excluir,))
conn.commit()

print("Contatos:")
for c in contatos:
    print(c)

