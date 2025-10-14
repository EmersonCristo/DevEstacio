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
print(f"O resultado da soma é {resultado}")