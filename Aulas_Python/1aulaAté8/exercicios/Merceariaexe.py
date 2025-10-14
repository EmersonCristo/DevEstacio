#Você está desenvolvendo um sistema simples de controle de estoque para uma mercearia. Crie uma lista com 5 produtos disponíveis na loja.
#Depois:

#Adicione um novo produto à lista.
#Remova um produto que está no estoque.
#Mostre a lista final com todos os produtos disponíveis.

frutas = ["Morango", "Uva", "Banana", "Maça", "Pera"]
print(frutas)

frutas.append("Amora")
print(frutas)

frutas.remove("Morango")
print(frutas)

#MELHOR FORMA DE FAZER O CÓDIGO CÓDIGODOPAULO

#produtos = ["Arroz", "Feijão", "Feijao", "Biscoito", "Café"]

# print("Produtos disponíveis no estoque:", produtos)


# acao = input("Você deseja adicionar um produto ou remover? (informe 'A = adicionar' ou 'R = remover'): ")

# if acao == "A":
#     novo_produto = input("Digite o nome do produto que deseja adicionar: ")
#     produtos.append(novo_produto)
#     print(f"{novo_produto} produto adicionado com sucesso!")

# elif acao == "R":
#     produto_remover = input("Digite o nome do produto que deseja remover: ")
#     if produto_remover in produtos:
#         produtos.remove(produto_remover)
#         print(f"{produto_remover} foi removido com sucesso!")
#     else:
#         print("Produto não encontrado na lista.")

# else:
#     print("Opção inválida! Tente novamente")


# print("Produtos disponiveis em estoque(ATUALIZADO):", produtos)
