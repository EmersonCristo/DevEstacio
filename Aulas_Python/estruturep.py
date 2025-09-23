#Estruturas de repetição 

# while sempre funciona com uma condição

condicao = 1

while condicao <= 10: #enquanto condicao for menor ou igual a 5
    print("Contador", condicao)
    condicao = condicao + 1 # a cada contagem o contador recebe mais 1 enquanto for menor que 5
    #condicao += 1
    #condicao ++


#for é utilizado quando temos noção de quantas vezes queremos que determinada função se repita 

for i in range (0, 11): #o i dentro do range é para ir contando de unidade em unidade de 0 a 11 lembrando que o zero é elemento contavel 
    print("Contador", i)

palavra = "Python"
for letra in palavra: #vai separar as letras em linhas
    print(letra)

frutas = ["maça", "Uva", "Pessêgo", "Banana"]
for fruta in frutas: #vai separar as frutas em linhas
    print(fruta)

#Break é Parar
    for i in range(1, 10): #de ínicio era pra contar do 1 ao 11
        if i == 5: #se a varial chegar ao número 5
            break #quebre o código
        print(i)

for i in range(1, 6):
    if i == 3: #se chegar ao 3
        continue # vai continuar, porém, o 3 é cortado
    print(i)

    #quando tem um for dentro de outro for, o python vai executar o que está dentro primeiro 

    #tomar cuidado pois o código pode ficar pesado

for i in range (1, 4):
    for j in range (1, 4):
        print(f"i={i}, j={j}")

