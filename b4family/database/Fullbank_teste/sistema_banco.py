import os
import  sqlite3 as sql

'''cursor.execute("""
    INSERT INTO bank_user(full_name,saldo, user,number, password)
    VALUES (?,?,?,?,?)
    """, ( s_full_name,s_saldo,s_number,s_user, s_password))
conn.commit ()'''

conn  =  sql.connect ( 'teste_database.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()
import hashlib
import sqlite3 as sql

conn = sql.connect('teste_database.db')
cursor = conn.cursor()

user = input("user: ")
password = input("password: ")
password = hashlib.sha256(password.encode()).hexdigest()

cursor.execute(f"SELECT * from bank_user WHERE user='{user}' AND password='{password}'")
result = cursor.fetchone()

if not result:
    print("Login failed")
else:
    print("Login successful")
    id = result[0]
    full_name = result[1]
    saldo = result[2]
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

while True:
    cur.execute (f"SELECT * from bank_user WHERE user='{user}' AND password = '{password}';")
    result = cur.fetchone()
    id = result[0]
    saldo = 'R$ {:,.2f}'.format(result[2])
    saldo_float = float(result[2])
    opcao = input(f'''
==========banco-sarme==========
Bem-Vindo de volta {full_name}
Seu saldo é de {saldo}
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
===============================
''')

    if opcao == "1":
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0:
            extrato += f"depósito: R$ {valor:.2f}\n"
            cur.execute(f"UPDATE bank_user SET saldo = saldo + {valor} WHERE ID = '{id}';")
            conn.commit ()
        else:
            print ("Operação falhou")
    
    elif opcao == "2":

        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo_float

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! você excedeu seu saldo")
        elif excedeu_limite:
            print("Operação falhou! você excedeu o limite ")
        elif excedeu_saques:
            print("Operação falhou! você excedeu o limite diario")

        elif valor > 0:
            extrato += f"Saque: R$ {valor:.2f}\n"
            cur.execute(f"UPDATE bank_user SET saldo = saldo - {valor} WHERE ID = '{id}';")  
                   
            numero_saques += 1
            print(numero_saques)
        else:
            print("Operação falhou!O valor Informado é valído") 

    elif opcao == "3":
        print("======================================")
        print("Nâo foi ralizada nenhuma movimentação." if not extrato else extrato)
        print(f"Saldo: {saldo}")
        print("======================================")
    elif opcao == "4":
        print("Obrigado por utilizar nossos serviços")
        break
    else:
        print("Operação Invalida,Digite novamente a operação")




    
    
