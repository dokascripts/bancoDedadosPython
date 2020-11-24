import sqlite3

try:

    banco = sqlite3.connect('primeirobanco.db')

    cursor = banco.cursor()

    cursor.execute("DELETE from pessoas WHERE idade = 16")

    banco.commit() 
    banco.close()
    print("os dados foram excluidos com sucesso!")

except sqlite3.Error as erro:
    print("Houve um erro ao excluir os dados",erro)