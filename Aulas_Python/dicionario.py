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