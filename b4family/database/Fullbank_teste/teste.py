import sqlite3
import sqlite3 as sql
import datetime

conta = int(input("conta"))
password = int(input("password"))

if conta == 123 and password == 123 or conta == 1234 and password == 1234:
    while True:
        # Conecta ao banco de dados
        conn = sqlite3.connect('extrato.db')
        c = conn.cursor()
        now = datetime.datetime.now()
        data = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
        descricao = input("Descricao: ")
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0:
            extrato += f"depósito: R$ {valor:.2f}\n"
            cur.execute(f"UPDATE bank_user SET saldo = saldo + {valor} WHERE ID = '{id}';")
            c.execute("INSERT INTO transacoes VALUES (?,?,?,?)", (conta,data, descricao, valor))
            conn.commit ()
        else:
            print ("Operação falhou")

        # Insere a transacao na tabela "transacoes"
        

        conn.commit()
        conn.close()


        # Conecta ao banco de dados
        conn = sqlite3.connect('extrato.db')
        c = conn.cursor()
        resultado = c.execute(f"SELECT * FROM transacoes where conta = {conta} ORDER BY data DESC ").fetchall()
        conn.close()
        for resultado in resultado:
            print(resultado)
        continua = input("Continuar (s/n)?")

        if continua == 'n':
            break
else:
    print("essa conta não existe")

