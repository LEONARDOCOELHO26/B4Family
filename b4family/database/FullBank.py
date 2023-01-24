import sqlite3 as sql
import os 
import twilio
from twilio.rest import Client
import keys
client = Client(keys.account_sid, keys.auth_token)

def clear_console():
    os.system('cls')
clear_console()

while True:
    print("Bem-vindo ao banco B4Famaly")
    print("[1] Login\n [2]cadastro\n [3]Sair")
    inicial = int(input("Digite a opção"))
    if inicial == 1:
        conn  =  sql.connect ( 'bank_database.db' )
        cursor  =  conn.cursor ()
        cur = conn.cursor()
        user = input("user")
        password = input("password")
        statement = f"SELECT * from bank_user WHERE user='{user}' AND password = '{password}';"
        cur.execute(statement)
        if not cur.fetchone():
            print("Login failed")
        else:
            #message
            targetuser = user
            rows = cursor.execute(
                "SELECT number FROM bank_user WHERE user = ?",
            (targetuser,),
            ).fetchall()
            number = str(rows)
            phone_number = "+55" + number[2:13]
            print(rows)
            print(phone_number)
            message_sing_in = client.messages.create(
            body="a sua conta do B4Family Foi a acessada",
            from_=keys.twilio_number,
            to=phone_number)

            clear_console()
            menu = '''
        ==========banco-sarme==========
                [1] Depositar
                [2] Sacar
                [3] Extrato
                [4] Sair
        ===============================
        '''
        print("Bem-vindo de volta",user)
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
    elif inicial == 2:
        clear_console()
        import  sqlite3
        conn  =  sqlite3 . connect ( 'bank_database.db' )
        cursor  =  conn.cursor ()
        s_full_name = input("fullname")
        s_user = input("user")
        s_number = input("numero")
        s_password = input("password")
        s_comfirm_password = input("comfirme password")
        if s_password == s_comfirm_password:
            cursor.execute("""
            INSERT INTO bank_user(full_name, user, number, password)
            VALUES (?,?,?,?)
            """, ( s_full_name,s_user,s_number, s_password))
            conn.commit ()

            ##send a message comfirm
            phone_number = "+55" + s_number
            client.messages.create(
            body="Obrigado por se cadastrar no B4Family",
            from_=keys.twilio_number,
            to=phone_number)

                # Display columns
            print('\nColumns in bank_user table:')
            data=cursor.execute('''SELECT * FROM bank_user''')
            for column in data.description:
                print(column[0])
                
            print('\nData in user table:')
            data=cursor.execute('''SELECT * FROM bank_user''')
            for row in data:
                print(row)

        else:
            print("as senhas não são iguais")
        conn . close ()
        if (conn):
            conn.close()
            print("\nThe SQLite connection is closed.")
        clear_console()
    elif inicial ==3:
        clear_console()
        print("Obrigado por utilizar nossos serviços ")  
        break

