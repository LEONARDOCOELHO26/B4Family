import  sqlite3
conn  =  sqlite3 . connect ( 'bank_database.db' )
cursor  =  conn.cursor ()




s_full_name = input("fullname")
s_saldo = 0
s_user = input("user")
s_number = input("numero")
s_password = input("password")
s_comfirm_password = input("comfirme password")
if s_password == s_comfirm_password:
    cursor.execute("""
    INSERT INTO bank_user(full_name,saldo, user,number, password)
    VALUES (?,?,?,?,?)
    """, ( s_full_name,s_saldo,s_number,s_user, s_password))
    conn.commit ()
    print("Data Inserted in the table: ")
    
        # Display columns
    print('\nColumns in user table:')
    data=cursor.execute('''SELECT * FROM bank_user''')
    for column in data.description:
        print(column[0])
        
    # Display data
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


    