lista_nomes = ["Gabriel", "Danny", "Arthur", "João"]
print(lista_nomes)

lista_nomes.append("Fernando")
print(lista_nomes)

lista_nomes.insert(0, "Lázaro")
print(lista_nomes)

outra_lista = ["Marcelo", "Clécio"]
lista_nomes.extend(outra_lista)
print(lista_nomes)

lista_nomes.remove("Danny")
print(lista_nomes)

lista_nomes.pop(0)
print(lista_nomes)
lista_nomes.pop()
print(lista_nomes)

del lista_nomes[1]
print(lista_nomes)

for nome in lista_nomes:
    print(nome)

lista_nomes.clear()
print(lista_nomes)