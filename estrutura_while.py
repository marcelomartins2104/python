soma = 0
cont = 0
maior = 0
menor = 11
while True:
    numero = float(input("Digite a nota (ou digite '99' para cancelar): "))
    if numero == 99:
        break
    elif numero < 0 or numero > 10:
        print("Digite um valor válido.")
        continue
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    cont += 1
media = soma / cont
print(f"""A média dos números é: {media:.1f}
O maior número é o {maior} e o menor número é o {menor}.""")