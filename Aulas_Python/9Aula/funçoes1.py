# def é utilizado para chamar uma função 

def saudacao():
    print("Seja bem vindo!!")

# dentro desses parenteses () vai um parametro 

def saudacao_1(nome):
    print(f"Seja bem vindo {nome}")

saudacao_1("Emerson\n") #podemos associar um dado a uma variavel mesmo após ela já ter sido chamada antes, como nesse mesmo exemplo 

def apresentar(nome, idade = 18): #função criada com idade já definida
    print(f"Nome: {nome} \nIdade: {idade}\n")

apresentar("Caio") #uma chamada para a função com o valor padrão adicionando Caio dentro da variavel nome
apresentar("Ana", 25) #sobreescrevendo o padrão com esses novos valores
apresentar(idade = 30, nome = "João") #nomeando argumentos 

def soma (a, b): #adicionando os parametros a e b 
    return a + b #informando para retorna ao usuario os valores de a + o valor de b

resultado = soma(110, 20)   #adicionando os valores de a(110) e b(20)
print(f"O resultado da soma é {resultado}\n")

# Variavel global utilizada durante todo o código 
# Variavel local usada apenas na função 

x = 10 #global

def mostrar():
    x = 5 #local
    print("Dentro da função: ", x)

# local
mostrar()
print(f"Fora da função: {x}\n",)

#utilizando o * para somar varios itens

def somar(*numeros):
    total = sum(numeros) #total recebe sumatorio de números 
    print(f"Soma = {total}\n")

somar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #passando os numeros que serao utilizados para realizar a função acima 

# Mais um exemplo 

def exibir_info(**dados): #informando que serão varios dados 
    for chave, valor in dados.items(): #usando o for para informar que os itens dentro do dicionario dados.items, serão do tipo chave e valor 
        print(f"{chave}: {valor}\n") #printando na tela a chave e o valor

exibir_info(nome="Caio", idade=25, Cidade="São Paulo") #nessa linha estou definindo quais serao as chaves e os valores 

#funções em uma unica linha utilizamos o lambda

quadrado = lambda x: x ** 2 #quadrado recebe x, e o x: x ** 2, o lambda é somente para dizer que essa função será realizada
print(quadrado(5)) #aqui estamos atribuindo o 5 ao valor de x

#itens ordenados com lambda

nomes = ["Ricardo", "Caio", "Pedro"]
ordenados = sorted(nomes, key=lambda x: len(x)) #sorted para organizar os itens, lambda para transformar tudo em uma função em uma única linha
print(ordenados)

# docstring é comentar o código
#criar funções longas não é uma boa prática 
#todo bom desenvolvedor tem uma pasta com suas principais funções 

def calcular_area(base, altura):
    "Calcular a área de um triângulo"
    return base * altura / 2

print(calcular_area(10, 2))