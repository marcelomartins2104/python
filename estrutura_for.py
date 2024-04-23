texto = input("Digite um texto de até duas linhas: ")
qtde_letras = 0
qtde_digitos = 0
for caractere in texto:
    if caractere.isalpha():
        qtde_letras += 1
    elif caractere.isdigit():
        qtde_digitos += 1
print(f"Seu texto possui {qtde_letras} letras e {qtde_digitos} dígitos.")