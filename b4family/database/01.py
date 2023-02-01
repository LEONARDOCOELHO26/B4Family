import sqlite3
import hashlib

# Criação da conexão com o banco de dados
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Criação da tabela de usuários, se ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

def register_user(username, password):
    # Criptografia da senha
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Armazenamento do usuário e da senha criptografada no banco de dados
    cursor.execute("""
    INSERT INTO users (username, password)
    VALUES (?, ?)
    """, (username, password_hash))
    conn.commit()

def login(username, password):
    # Criptografia da senha fornecida pelo usuário
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Verificação da existência do usuário e da senha no banco de dados
    cursor.execute("""
    SELECT * FROM users
    WHERE username=? AND password=?
    """, (username, password_hash))
    user = cursor.fetchone()

    # Retorno do resultado da verificação
    if user:
        return True
    else:
        return False

# Exemplo de uso
register_user("johndoe", "password123")
print(login("johndoe", "password123")) # True
print(login("johndoe", "wrongpassword"))

