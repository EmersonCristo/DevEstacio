# Você está desenvolvendo um sistema de RH para cadastrar funcionários de uma empresa. Cada funcionário tem:

# Nome
# Cargo
# Salário

# Faça um programa que:

# Cadastre 3 funcionários em um dicionário, onde a chave é o nome e o valor é outro dicionário com o cargo e o salário.

# Permita consultar o salário de um funcionário pelo nome.

# Calcule e exiba a média salarial da empresa.

#FEITO PELO PROFESSOR 

#dicionário principal
funcionario = {}

#cadastrar os funcionários
for i in range(3):
  nome = input(f"Nome do funcionário {i+1}: ")
  cargo = input(f"Cargo do funcionário {i+1}: ")
  salario = float(input(f"Salário do funcionário {i+1}: "))

  funcionario[nome] = {
      "cargo": cargo,
      "salario": salario
  }
  print()

#consulta
consulta = input("Digite o nome de um funcionário para consultar seu salário: ")
if consulta in funcionario:
  print(f"O salário de {consulta} é de R${funcionario[consulta]['salario']}")
else:
  print("Funcionário não encontrado.")

total_salario = sum(dados["salario"] for dados in funcionario.values())
media_salario = total_salario / len(funcionario)
print(f"A média salarial da empresa é de R${media_salario:.2f}")