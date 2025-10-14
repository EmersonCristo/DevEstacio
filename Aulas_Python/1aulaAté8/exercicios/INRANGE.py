#range 

for n in range(1, 11):
    print(f"Treinando seu loop, e aqui é o número {n}º da vez.")

# for n in range (1, 101):
    # EXEMPLO: mostre a variável n em um raio de 101, (a variável n vai subindo de número em número até chegar no 101. Já na parte da númeração(1, 101), quer dizer o seguinte, comece pelo número 1 a demonstração de números ao usuário, e finalize ao chegar no 101, lembrando que o número 0 é contado junto aos outros números, e como o código está pedindo para informar do número 1 em diante, o número 0 não ira aparecer.)

soma = 0 
for n in range(1, 11): #contar o n em um raio de 11, começando pelo número 1 
    soma += 1 #adicionar 1 ao soma, enquanto a função contar o n em um raio de 11, começando pelo número 1 

    print(f"A soma total é {soma}") # vai mostrar todas as variações do soma até chegar no número 11

# Usando o range, o computador vai contando o n todas as vezes que ele muda de número em número

frutas = ["banana", "maça", "pera", "uva"]

for f in frutas:
    print(f) #vai ir contando o f na lista de frutas, ou seja subindo 1 por 1, assim contanto todos os itens da lista

# o f do caso acima ou o n das primeiras explicações, é basicamente a variavel que vai sendo atribuido todos os itens da lista, para serem apresentados na tela, ou seja uma variavel que vai sendo resetada até chegar ao ultimo item, e apresentando todo o processo que passou no caminho.

numeros = [5, 8, 2, 9, 0, 1, 3, 4]
for n in numeros:
    if n % 2 != 0: #sempre que chegar um número que o restante da divisão for diferente de 0 continue 
        continue  #O continue funciona como um "PULE", se o resultado por diferente de 0 continue (pule o número da vez).
    print(f"O número {n}º é par")

    