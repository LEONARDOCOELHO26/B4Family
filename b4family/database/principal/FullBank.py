import sqlite3
import sqlite3 as sql
import os 
import twilio
import random
import hashlib
from twilio.rest import Client
import keys
import geocoder
from geopy.geocoders import Nominatim
import datetime
client = Client(keys.account_sid, keys.auth_token)
conn  =  sql.connect ( 'database.db' )
cursor  =  conn.cursor ()
cur = conn.cursor()
now = datetime.datetime.now()

def clear_console():
    os.system('cls')
clear_console()

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

while True:
    print("Bem-vindo ao banco B4Famaly")
    print("[1] Login\n [2]cadastro\n [3]Sair")
    inicial = int(input("Digite a opção"))
    if inicial == 1:
        user = input("user: ")
        password = input("password: ")
        password = hashlib.sha256(password.encode()).hexdigest()
        cur.execute(f"SELECT * from bank_user WHERE user='{user}' AND password='{password}'")
        result = cursor.fetchone()
        if not cur.fetchone():
            print("Login failed")
        else:
            #localização e o horario
            
            g = geocoder.ip('me')
            now = datetime.datetime.now()
            geolocator = Nominatim(user_agent="geoapiExercises")
            def city_state_country(coord):
                location = geolocator.reverse(coord, exactly_one=True)
                address = location.raw["address"]
                city = address.get("city", )
                state = address.get('state', )
                country = address.get('country',)
                return city, state, country
            city_bad = str(city_state_country (g.latlng))
            bad_chars = ["(",")","'"]
            test_string = city_bad
            city = ''.join(map(lambda x: x if x not in bad_chars else '', test_string))
            print(city)
            time= f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
            #message
            targetuser = user
            rows = cursor.execute(
                "SELECT number FROM bank_user WHERE user = ?",
            (targetuser,),
            ).fetchall()
            number = str(rows)
            phone_number = "+55" + number[2:13]
            message_sing_in = client.messages.create(
            body=f"{user} a sua conta do B4Family Foi a acessada em {city} ás {time} ",
            from_=keys.twilio_number,
            to=phone_number)

            clear_console()
            cursor.execute(f"SELECT * from bank_user WHERE user='{user}' AND password='{password}'")
            result = cursor.fetchone()
            fullname = result[1]
            limite = 500
            extrato = ""
            numero_saques = 0
            LIMITE_SAQUES = 3
            while True:
                cur.execute (f"SELECT * from bank_user WHERE user='{user}' AND password = '{password}';")
                result = cur.fetchone()
                conta = float(result[6])
                id = result[0]
                saldo = 'R$ {:,.2f}'.format(result[2])
                saldo_float = float(result[2])

                opcao = input(f'''
                ==========banco-sarme==========
                Bem-Vindo de volta {fullname}
                Seu saldo é de {saldo}
                        [1] Depositar
                        [2] Sacar
                        [3] Extrato
                        [4] Sair
                ===============================
                ''')
                if opcao == "1":
                    valor = float(input("Informe o valor do depósito:"))
                    data = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
                    descricao = 'deposito'
                    if valor > 0:
                        cur.execute(f"UPDATE bank_user SET saldo = saldo + {valor} WHERE ID = '{id}';")
                        conn = sqlite3.connect('extrato.db')
                        c = conn.cursor()
                        c.execute("INSERT INTO transacoes VALUES (?,?,?,?)", (conta,data, descricao, valor))
                        conn.commit ()
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
                        conn.commit ()
                        descricao = "saque"
                        data = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
                        c = conn.cursor()
                        c.execute("INSERT INTO transacoes VALUES (?,?,?,?)", (conta,data, descricao, valor))
                        conn.commit ()       
                        numero_saques += 1
                        print(numero_saques)
                    else:
                        print("Operação falhou!O valor Informado é valído") 

                elif opcao == "3":
                    conn = sqlite3.connect('extrato.db')
                    c = conn.cursor()
                    resultado = c.execute(f"SELECT * FROM transacoes where conta = {conta} ORDER BY data DESC ").fetchall()
                    conn.close()
                    print("======================================")
                    for resultado in resultado:
                        print(resultado)
                    print("======================================")
                elif opcao == "4":
                    print("Obrigado por utilizar nossos serviços")
                    break
                else:
                    print("Operação Invalida,Digite novamente a operação")
    elif inicial == 2:
        clear_console()
        s_full_name = input("fullname")
        s_saldo = 0.0
        s_user = input("user")
        s_number = input("numero")
        s_conta = gerar_numero_unico()
        s_password = input("password").encode('utf-8')
        s_password = hashlib.sha256(s_password).hexdigest()

        s_comfirm_password = input("comfirme password").encode('utf-8')
        s_comfirm_password = hashlib.sha256(s_comfirm_password).hexdigest()

        if s_password == s_comfirm_password:
            cursor.execute("""
            INSERT INTO bank_user(full_name,saldo, user,number, password,conta)
            VALUES (?,?,?,?,?,?)
            """, (s_full_name, s_saldo, s_user, s_number, s_password, s_conta))
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
        clear_console()
    elif inicial ==3:
        clear_console()
        print("Obrigado por utilizar nossos serviços ")  
        break

