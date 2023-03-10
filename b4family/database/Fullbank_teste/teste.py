
import sqlite3
import datetime
now = datetime.datetime.now()

def gerador_de_extrato():
                        from reportlab.lib.pagesizes import letter
                        from reportlab.pdfgen import canvas
                        data = f"{now.day}-{now.month}-{now.year}"
                        pdf_name = f'extrato{data}.pdf'
                        pdf = canvas.Canvas(pdf_name, pagesize=letter)
                        pdf.setFillColorRGB(0.9,0.9,0.1)
                        pdf.setFont("Helvetica", 16)
                        pdf.setFillColorRGB(0, 0, 0)
                        data = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
                        pdf.drawString(50, 750, "-------------------------------------Extrato Bancário-------------------------------------")
                        conn = sqlite3.connect('extrato.db')
                        c = conn.cursor()
                        resultado = c.execute(f"SELECT * FROM transacoes WHERE conta = {conta} ORDER BY data DESC ").fetchall()
                        conn.close()
                        pdf.drawString(100, 730, f"conta:{conta}")
                        pdf.drawString(400, 730, f"Data:{data}")
                        pdf.drawString(50, 715, "------------------------------------------------------------------------------------------------")

                        y = 700  # starting position for transactions
                        for transacao in resultado:
                            pdf.setFillColorRGB(0,0,0)
                            pdf.drawString(60, y, str(transacao[0]))   # id
                            pdf.drawString(130, y, str(transacao[1]))  # data
                            pdf.drawString(280, y, str(transacao[2]))  # descricao
                            if str(transacao[2]) == "saque":
                                pdf.setFillColorRGB(1,0,0)
                                pdf.drawString(430, y, f"-R${'{:,.2f}'.format(transacao[3]).replace(',', '#').replace('.', ',').replace('#', '.')}")      # valor
                            else:
                                pdf.setFillColorRGB(0,0,0)
                                pdf.drawString(430, y, f"R${'{:,.2f}'.format(transacao[3]).replace(',', '#').replace('.', ',').replace('#', '.')}")      # valor
                            y -= 20
                        pdf.drawString(250, 30, "10/03/2023")
                        pdf.drawString(150, 10, "Obrigado!Por Usar os serviços da B4Family.")
                        pdf.showPage()
                        pdf.save()

escolha = input("você gostaria de imprimir o extrato?S/N")
if escolha == "S" or "s":
    gerador_de_extrato()
else:
    print("oK")








