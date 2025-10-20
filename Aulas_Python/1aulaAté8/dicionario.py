aluno = {
    "Nome": "Maria",
    "Idade": 20,
    "Curso": "Engenharia",
}

#elemento dicionario, meio que uma variavel com varios dados 

print(aluno)

#podemos buscar direto na chave

print(aluno["Nome"])

#alterando dados 

aluno["Idade"] = 21
print

#adicionando elementos ao dicionario 
#não podemos modificar as chaves

aluno["Nota"] = 9.5
print(aluno)

#também podemos remover os elementos 

del aluno["Curso"]
print(aluno)

# quando vai utilizar o for em um dicionario é necessário utilizar o .item no final, para o mesmo trazer os dados do dicionario para a tela 

dados = {"Nome":"Lan Code", "Inscritos":5000, "Categoria":"Programação"}

for c, v in dados.items():
    print(f"{c}: {v}")

#quando se vai utilizar o for em dicionario para buscar apenas 1 dos 2 items, chave ou valores a semantica muda 

#quando se vai fazer com os valores se faz assim 
for v, in dados.values():
    print(f"{v}")

#quando se vai fazer só com as chaves se faz assim 
for c, in dados.keys(): #keys, em inglês chaves ddddddddddddd
    print(f"{c}")
