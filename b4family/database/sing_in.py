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
    INSERT INTO user(full_name, user,number, password)
    VALUES (?,?,?,?)
    """, ( s_full_name,s_user, s_password))
    conn.commit ()
    print("Data Inserted in the table: ")
    
        # Display columns
    print('\nColumns in bank_user table:')
    data=cursor.execute('''SELECT * FROM user''')
    for column in data.description:
        print(column[0])
        
    # Display data
    print('\nData in bank_user table:')
    data=cursor.execute('''SELECT * FROM user''')
    for row in data:
        print(row)

else:
    print("as senhas não são iguais")
conn . close ()
if (conn):
    conn.close()
    print("\nThe SQLite connection is closed.")


    