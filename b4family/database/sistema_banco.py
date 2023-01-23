import os
import  sqlite3
conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn.cursor ()


user =cursor.execute('''SELECT user FROM bank_user''')

menu = '''
==========banco-sarme==========
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
===============================
'''
print("Bem-vindo",user)
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"
        
        else:
            print ("Operação falhou")
    
    elif opcao == "2":

        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! você excedeu seu saldo")
        elif excedeu_limite:
            print("Operação falhou! você excedeu o limite ")
        elif excedeu_saques:
            print("Operação falhou! você excedeu o limite diario")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"         
            numero_saques += 1
            print(numero_saques)
        else:
            print("Operação falhou!O valor Informado é valído") 

    elif opcao == "3":
        print("======================================")
        print("Nâo foi ralizada nenhuma movimentação." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("======================================")
    elif opcao == "4":
        print("Obrigado por utilizar nossos serviços")
        break
    else:
        print("Operação Invalida,Digite novamente a operação")




    
    
