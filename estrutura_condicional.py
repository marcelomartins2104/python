nome_paciente = str(input("Digite seu nome inteiro: ").title().strip())
idade_paciente = int(input("Digite sua idade: "))
print("Agora vamos calcular o seu IMC!")
altura = float(input("Primeiro, digite sua altura (em metros): ").replace(",","."))
peso = float(input("Agora, digite seu peso (com casa decimal): ").replace(",","."))
calculo_imc = peso / altura**2
if calculo_imc < 18.5:
    print(f"A classificação de {nome_paciente}, de {idade_paciente} anos, é: \033[37mMAGREZA\033[0m")
elif calculo_imc >= 18.5 and calculo_imc < 25:
    print(f"A classificação de {nome_paciente}, de {idade_paciente} anos, é: \033[32mNORMAL\033[0m")
elif calculo_imc >= 25 and calculo_imc < 30:
    print(f"A classificação de {nome_paciente}, de {idade_paciente} anos, é: \033[30mSOBREPESO\033[0m")
elif calculo_imc >= 30 and calculo_imc < 35 and idade_paciente >= 15:
    print(f"A classificação de {nome_paciente}, de {idade_paciente} anos, é: \033[35mOBESIDADE GRAU 1\033[0m")
elif calculo_imc >= 35 and calculo_imc < 40 and idade_paciente >= 15:
    print(f"A classificação de {nome_paciente}, de {idade_paciente} anos, é: \033[36mOBESIDADE GRAU 2\033[0m")
elif calculo_imc > 40 and idade_paciente >= 15:
    print(f"A classificação de {nome_paciente}, de {idade_paciente} anos, é: \033[33mOBESIDADE GRAU 3\033[0m")
elif calculo_imc > 30 and idade_paciente < 15:
    print(f"A classificação de {nome_paciente}, de {idade_paciente} anos, é: \033[1;31mOBESIDADE INFANTIL\033[0m")
print(F"""O cálculo do IMC é feito da seguinte forma:
(peso) {peso} / (altura²) {altura}² = (IMC) {calculo_imc:.2f}""")