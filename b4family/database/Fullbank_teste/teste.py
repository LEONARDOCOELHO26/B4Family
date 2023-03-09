import random
import sqlite3

def gerar_numero_unico():
    conexao = sqlite3.connect('nome_do_banco_de_dados.db')
    cursor = conexao.cursor()

    # Gerar um número aleatório entre 10000 e 99999
    numero = random.randint(10000, 99999)

    # Verificar se o número já existe na tabela
    while True:
        cursor.execute('SELECT COUNT(*) FROM numeros_gerados WHERE numero = ?', (numero,))
        if cursor.fetchone()[0] == 0:
            break
        else:
            numero = random.randint(10000, 99999)

    # Inserir o número na tabela
    cursor.execute('INSERT INTO numeros_gerados (numero) VALUES (?)', (numero,))
    conexao.commit()

    return numero

