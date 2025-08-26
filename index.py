print("Olá mundo!")

# format com {}
nome = "João"
idade = 24
print("Nome: {}, idade: {}" .format(nome, idade))

# f - string
print(f"{nome} terá {idade+5} anos em 5 anos")

# separador e fim
print("A", "B", "C", sep=" - ", end=" .\n")

#ADIÇÃO: X + Y = X+Y | C = A + B
#SUBTRAÇÃO: X - Y = X-Y | C = A - B
#MULTIPLICAÇÃO: X x Y | C = A * B
#DIVISÃO: X / Y | C = A / B
#PEGAR O RESULTADO INTEIRO DA DIVISÃO: C = A // B
#PEGAR O RESTO DA DIVISÃ0  C = A % B
#MODIFICA O VALOR PARA NEGATIVO  C = -A
#POTÊNCIA  DE A ELEVADO A B C = A ** B

a, b =14, 5
print("a+b = ", a+b) 
print("a-b = ", a-b) 
print("a*b = ", a*b) 
print("a/b = ", a/b) 
print("a//b = ", a//b)
print("a**b = ", a**b) 

#ORDEM DE PRECEDÊNCIA
# 1 () 

# 2 ** 

# 3 * /  //  %

# 4 + -

a = 10
b = 10.5
c = "python"
d = True 
e = [1, 2 ,3]

print(type(a), type(b), type(c), type(d), type(e))

grau = float(input("Quantos graus está fazendo em SP?"))

Fah = (grau * 9/5) + 32
Kel = (grau - 32) * 5/9

print(f"Está fazendo {grau} em SP")
print(f"Em fahrenheit é {Fah}")
print(f"Em Kelvin é {Kel}")