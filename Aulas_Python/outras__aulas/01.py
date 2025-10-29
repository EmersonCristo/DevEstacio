#lista é uma coleção ordenada e mutável. Permite membros duplicados.
lista = ["Carro", True, 2, 2.35] #lista sempre vai abrir e fechar com o []
print(lista)
print(type(lista))
print("-"*40)

#Tupla é uma coleção ordenada e imútavel. Permite membros duplicados.
tupla = ("carro", True, 2,  2.5) #tupla sempre aberta e fechada com ()
print(tupla)
print(type(tupla))
print("-"*40)

# Dicionario é uma coleção ordenada e mutável. Nenhum membro duplicado.
dicionario = {"nome": "carro", "logica": True, "numero": 2, "outronumero": 3.35} #para utilizar o dicionario precisamos utilizar o esquema de chave e valor
print(dicionario)
print(type(dicionario))
print("-"*40)

# Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
conjunto = {"carro", True, 2, 2.35}
print(conjunto)
print(type(conjunto))