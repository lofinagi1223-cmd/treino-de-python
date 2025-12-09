#Dicionario parece objeto

carro = {"modelo": "Fiat Uno", "ano": 2009}

print(carro["ano"]) #chamar valor

print(carro.keys()) # chaves
print(carro.values()) #valores das chaves
print(carro.items()) # items do dicionario
carro.update({"cor": "prata"})
print(carro)

#////////////////#Conjuntos#

cores1 = {"Vermelho", "Azul", "Amarelo"}
cores2 = {"Roxo", "Azul", "Rosa"}

uniao = cores1 | cores2
print(uniao)

intercesao = cores1 & cores2
print(intercesao)

diferenca = cores1 - cores2
print(diferenca)

diferenca_simetrica = cores1 ^cores2
print(diferenca_simetrica)

cores1.add("Cinza")
print(cores1)

#
#As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e manipular dados em nossos programas. As listas são úteis para coleções ordenadas e mutáveis, as tuplas para coleções ordenadas e imutáveis, os dicionários para armazenar pares de chave valor e os conjuntos para coleções não ordenadas de elementos únicos.
#