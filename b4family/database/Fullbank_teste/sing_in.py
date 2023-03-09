import hashlib
import sqlite3
import random

import random
import sqlite3

def gerar_numero_unico():
    conexao = sqlite3.connect('teste_database.db')
    cursor = conexao.cursor()
    numero = random.randint(10000, 99999)
    while True:
        cursor.execute('SELECT COUNT(*) FROM bank_user WHERE conta = ?', (numero,))
        if cursor.fetchone()[0] == 0:
            break
        else:
            numero = random.randint(10000, 99999)

    # Inserir o número na tabela
    conexao.commit()
    return numero

conn = sqlite3.connect('teste_database.db')
cursor = conn.cursor()

s_full_name = input("fullname")
s_saldo = 0.0
s_user = input("user")
s_number = input("numero")

s_password = input("password").encode('utf-8')
s_password = hashlib.sha256(s_password).hexdigest()

s_comfirm_password = input("comfirme password").encode('utf-8')
s_comfirm_password = hashlib.sha256(s_comfirm_password).hexdigest()
conta = gerar_numero_unico()

if s_password == s_comfirm_password:
    cursor.execute("""
    INSERT INTO bank_user(full_name,saldo, user,number, password,conta)
    VALUES (?,?,?,?,?,?)
    """, (s_full_name, s_saldo, s_user, s_number, s_password, conta))
    conn.commit()
    print("Data Inserted in the table: ")

    # Display columns
    print('\nColumns in user table:')
    data = cursor.execute('''SELECT * FROM bank_user''')
    for column in data.description:
        print(column[0])

    # Display data
    print('\nData in user table:')
    data = cursor.execute('''SELECT * FROM bank_user''')
    for row in data:
        print(row)

    
else:
    print("as senhas não são iguais")

conn.close()
if (conn):
    conn.close()
    print("\nThe SQLite connection is closed.")


    