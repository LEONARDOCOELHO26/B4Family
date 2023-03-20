import re
number_correct = r"^\s?\d{2}[- ]?\d{5}[- ]?\d{4}$"
cpf_correct = r"^\s?\d{3}[. ]?\d{3}[. ]?\d{3}[- ]?\d{2}$"
email_regex = r"[^@]+@[^@]+\.[^@]+"
name_regex = r'^[a-zA-Z]+\s'

s_full_name = input("fullname")
s_email = input("email")
s_user = input("user")
s_number = input("numero")
cpf = input("cpf")


'''if s_full_name.isalpha() and re.match(email_regex, s_email) and re.match(cpf_correct, cpf) and re.match(number_correct, s_number):
    print(f"E verdadeiro{s_full_name}")
else:
    print(f"{s_full_name} não é verdadeira")'''





def validations():
    if re.match(name_regex, s_full_name):
        if re.match(email_regex, s_email):
            if re.match(cpf_correct, cpf):
                if re.match(number_correct, s_number):
                    validation = "True"
                else:
                    print(f"Phone number '{s_number}' é invalido")
            else:
                print(f"CPF '{cpf}' é invalido")
        else:
            print(f"Email '{s_email}' é invalido")
    else:
        print(f"Full name '{s_full_name}' deve conter apenas letras")


validations()
if validation == "True":
    print("cadastro feito")
else:
    print("cadastro invalido")





