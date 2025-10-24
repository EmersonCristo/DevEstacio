
def somar(n1, n2):
    resultado = n1 + n2
    print(f"A soma entre {n1} e {n2} é igual a {resultado}") #aqui deixamos todo o modelo pronto 

somar(10, 50) #aqui mandamos os argumentos, para ser utilizado dentro da função acima 

#NO CASO SE QUISERMOS RETORNAR O VALOR APENAS DE RESULTADO QUE É UMA VARIAVEL LOCAL, PRECISAMOS USAR O RETURN

def somar(n1, n2):
    resultado = n1 + n2
    return resultado #estamos mandando a maquina armazenar o valor de resultado em algum local, para se necessario utiliza-lo novamente assim iremos atribuir o valor em outra variavel, assim como no exemplo abaixo.

resultado_da_soma = somar(5, 5)
resultado_outra_soma = somar (7, 10)
print(f"Fizemos duas somas, a primeira resultando em {resultado_da_soma}, e a segunda resultando em {resultado_outra_soma}")

# SEM O RETURN NÃO SERIA POSSIVEL OBTER OS DADOS DE AMBAS AS VARIAVEIS 
# O RETURN APLICA O VALOR DA FUNÇÃO DENTRO DA VARIAVEL "ELE ESTÁ SALVANDO OS VALORES DENTRO DAS VARIAVEIS"


#OUTRO EXEMPLO

def saudacao(nome):
    print(f"Prazer {nome}")

saudacao("Emerson")


#OUTRO EXEMPLO

def somar_lista(*numeros): #com esse * chamamos isso de tupla, e isso quer dizer que damos liberdade ao usuário para colocar quantos dados ele quiser
    resultado = 0
    for numero in numeros: #para casa numero em numeros
        resultado += numero #vai ir somando resultado com o próximo número que vier
    return resultado #retornando o valor a maquina 

soma_da_lista = somar_lista(6, 2, 3, 5)
print(f"O resultado final é {soma_da_lista}")


#OUTRO EXEMPLO 

def calcular_media(*numeros):
    qtd = len(numeros) #o len é para calcular a quantidade de dados que temos dentro de determinada variavel 
    soma = 0 # a soma inicia em 0
    for numero in numeros: #contamos de numero em numero 
        soma += numero # soma começa com 0, e vai somando a cada número que passa
    media = soma / qtd # a média é a divisão da soma pela quantidade de numeros
    return media # guardamos o resultado da variavel media na maquina para se necessario utiliza-lo mais tarde

resultado = calcular_media(7, 2, 4, 9)
print(f"A média é {resultado}")


#OUTRO EXEMPLO

def informacoes_pessoais(**informacoes): # aqui criamos um dicionario 
    for chave, valor in informacoes.items(): #sempre que formos mostrar de item por item em dicionarios precisamos adicionar o .items, caso não adicionemos o .items, vai retornar o dicionario inteiro para o usuario

#O DICIONARIO É FORMADO POR CHAVE E VALOR, ASSIM SE QUISERMOS DAR O PRINT EM SEUS ITEMS DE UM POR UM TEMOS QUE FAZER O SEGUINTE EXEMPLO A SEGUIR
        print(f"{chave}: {valor}")

informacoes_pessoais(nome="Emerson", idade = 24, inscritos = 55, videos = 0)


#EXEMPLO CONTAGEM REGRESSIVA 

def contagem_regrassiva(numero):
    while True:
        print(numero)
        numero -= 1
        if numero <= 0:
            break #lembrando que quando tem a repetição while and true, precisamos de um break para parar a função

contagem_regrassiva(10)

#MESMO EXEMPLO UTILIZANDO O FOR

def contagem_regressiva(numero):
    for i in range(numero, 0, -1): #para cada i no range, da variavel numero, menor numero 0, somando ao -1 MAIS OU MENOS ISSO KKKJJ
        print(i)

contagem_regressiva(10)