conta_pagou = conta
conta_recebe = input("Digite a conta")
valor = input('insira o valor do pix')
if valor > saldo:
    print("Operação falhou! você excedeu seu saldo")
elif valor > "0":
    data = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
    query = f"SELECT * FROM bank_user WHERE conta = '{conta_recebe}'"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        descricao_recebe = "pix recebido"
        print("dinheiro depositado")
        cur.execute(f"UPDATE bank_user SET saldo = saldo + {valor} WHERE conta = {conta_recebe};")
        conn.commit ()
        cur.execute("INSERT INTO transacoes VALUES (?,?,?,?)", (conta_recebe,data, descricao_recebe, valor))
        conn.commit()
        descricao_pagou = "pix enviado"
        cur.execute(f"UPDATE bank_user SET saldo = saldo - {valor} WHERE ID = {id};") 
                                    
        cur.execute("INSERT INTO transacoes VALUES (?,?,?,?)", (conta_pagou,data, descricao_pagou, valor))
        conn.commit() 
    else:
        print(f"A conta {conta_recebe} não existe no banco de dados.")







