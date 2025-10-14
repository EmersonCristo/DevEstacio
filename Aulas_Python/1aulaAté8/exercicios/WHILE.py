# WHILE na tradução significa enquanto 

contador = 0

#simples

while contador <= 8: #enquanto o contador for menor que 8, adicione mais 1 ao contador 
    print(f"O contador está no número {contador}º")
    contador += 1 #adicione mais 1 ao contador 

#WHILE É MAIS UTILIZADO QUANDO NÃO TEMOS CERTEZA DE QUANDO O LOOPING VAI SER EXECUTADO, O FOR É MAIS PARA QUANDO TEMOS NOÇÃO DE QUANTAS VEZES SERA

while True: #isso é um código infinito, pois sempre será verdade
    numero = int(input("Digite um número par: "))
    if numero % 2 == 0: #se o número divido por 2, for igual a 0
        print("Você digitou um número par.")
        break #Parar o código, porque ele é infinito 
    else:
        print("Você digitou um número impar.")
        break #Parar o código, porque ele é infinito 

print("Fim do programa") #esse print está fora do looping ou seja, só sera executado quando o looping acabar 


