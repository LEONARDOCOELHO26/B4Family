def envio_cadastro():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from keys import emailB4
    from keys import passwordB4

    phone_number = "41992483105"
    email_user = "alfredocoelho16@gmail.com"
    user = "leo"
    # cria o objeto mensagem
    msg = MIMEMultipart()

    # define os detalhes da mensagem, como remetente, destinatário, assunto e corpo da mensagem
    msg['From'] = f"{emailB4}"
    msg['To'] = f'{email_user}'
    msg['Subject'] = 'Seja-Bem vindo ao grupo B4Family'

    corpo = 'esse é apenas um email de comfirmação de criação de conta'
    msg.attach(MIMEText(corpo, 'plain'))

    # estabelece a conexão com o servidor SMTP e loga no servidor com as credenciais do seu email
    servidor_smtp = 'smtp.gmail.com'
    porta_smtp = 587
    usuario = f"{emailB4}"
    senha = f'{passwordB4}'

    server = smtplib.SMTP(servidor_smtp, porta_smtp)
    server.starttls() # define a criptografia TLS
    server.login(usuario, senha)

    # envia a mensagem
    texto_email = msg.as_string()

    server.sendmail(usuario, msg['To'], texto_email)

    server.quit() 
    targetuser = user
    rows = cursor.execute(
                "SELECT number FROM bank_user WHERE user = ?",
    (targetuser,),
            ).fetchall()
    number = str(rows)
    phone_number = "+5541992483105" 
    message_sing_in = client.messages.create(
    body=f"{user} Seja bem vindo ao Banco B4Family ",
    from_=keys.twilio_number,
    to=phone_number)

envio_cadastro()







