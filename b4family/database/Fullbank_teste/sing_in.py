import re
import sqlite3
import random
import hashlib

# define a function to generate a unique bank account number
def gerar_numero_unico():
    conexao = sqlite3.connect('testedatabase.db')
    cursor = conexao.cursor()
    numero = random.randint(10000, 99999)
    
    while True:
        cursor.execute('SELECT COUNT(*) FROM bank_user WHERE conta = ?', (numero,))
        if cursor.fetchone()[0] == 0:
            break
        else:
            numero = random.randint(10000, 99999)

    # insert the new account number into the table and commit changes
    cursor.execute('INSERT INTO bank_user(conta) VALUES(?)', (numero,))
    conexao.commit()
    return numero

# define a function to validate user inputs for creating a new bank account
def validar_entrada(s_full_name, s_email, s_user, s_number, s_cpf, s_password):
    EXPRESSAO_REGULAR_NUMERO_TELEFONE = r"^\s?\d{2}[- ]?\d{5}[- ]?\d{4}$"
    EXPRESSAO_REGULAR_CPF = r"^\s?\d{3}[. ]?\d{3}[. ]?\d{3}[- ]?\d{2}$"
    EXPRESSAO_REGULAR_EMAIL = r"[^@]+@[^@]+\.[^@]+"
    EXPRESSAO_REGULAR_NOME = r'^[a-zA-Z]+\s'
    EXPRESSAO_REGULAR_SENHA = r'^[A-Za-z0-9@#$%^&+=]{8,}$'

    if not all(re.match(expressao_regular, s) for expressao_regular, s in ((EXPRESSAO_REGULAR_NOME, s_full_name), (EXPRESSAO_REGULAR_EMAIL, s_email), (EXPRESSAO_REGULAR_CPF, s_cpf), (EXPRESSAO_REGULAR_NUMERO_TELEFONE, s_number))):
        motivos = []
        if not re.match(EXPRESSAO_REGULAR_NOME, s_full_name):
            motivos.append("O nome completo deve conter apenas letras.")
        if s_email and not re.match(EXPRESSAO_REGULAR_EMAIL, s_email):
            motivos.append("Formato de endereço de email inválido.")
        if s_cpf and not re.match(EXPRESSAO_REGULAR_CPF, s_cpf):
            motivos.append("Formato de CPF inválido.")
        if s_password and not re.match(EXPRESSAO_REGULAR_SENHA, s_password):
            motivos.append("A senha não contém os requisitos mínimos.")
        if not re.match(EXPRESSAO_REGULAR_NUMERO_TELEFONE, s_number):
            motivos.append("Formato de número de telefone inválido.")
        if motivos:
            raise ValueError(" ".join(motivos))
    return True

# prompt user for input and create new bank account if inputs are valid
escolha = input("Digite 1 para criar nova conta: ")

if escolha == "1":
    s_full_name = input("Digite o seu nome completo: ")
    s_email = input("Digite o seu endereço de email: ")
    s_user = input("Digite o nome de usuário: ")
    s_number = input("Digite o seu número de telefone: ")
    s_cpf = input("Digite o seu CPF: ")
    s_password = input("Digite a sua senha: ")
    s_comfirm_password = input("Confirme a sua senha: ")
    
    # validate user inputs
    try:
        validar_entrada(s_full_name, s_email, s_user, s_number, s_cpf, s_password)
        s_conta = gerar_numero_unico()
        s_password_cript = hashlib.sha256(s_password.encode('utf-8')).hexdigest()
    # insert the new user account details into the bank_user table
        with sqlite3.connect('testedatabase.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO bank_user(full_name, saldo, email, user, number, password, conta, CPF) VALUES(?,?,?,?,?,?,?,?)""",
                        (s_full_name, 0.0, s_email, s_user, s_number, s_password_cript, s_conta, s_cpf))
            conn.commit()
        
        print('Conta criada com sucesso! Seu número de conta é: ', s_conta)
    except ValueError as e:
        print(e)
        exit()
        
    # encrypt the user's password using SHA-256 hashing
    
    
    # generate a unique account number using the gerar_numero_unico function
    



    







