alta = {
    "Tarefa01": " ",
    "Tarefa02": " ",
    "Tarefa03": " ",
}
media = {
    "Tarefa01": " ",
    "Tarefa02": " ",
    "Tarefa03": " ",
}
baixa = {
    "Tarefa01": " ",
    "Tarefa02": " ",
    "Tarefa03": " ",
}

tafn1 = input("Qual tarefa deseja adicionar?: ")

#Professor

alta = []
media = []
baixa = []

for i in range(5):
  print(f"Tarefa {i+1}")
  descricao = input("Descrição da Tarefa: ")
  prioridade = input("Prioridade (alta, media, baixa): ").lower()

  if prioridade == "alta":
    alta.append(descricao)
  elif prioridade == "media":
    media.append(descricao)
  elif prioridade == "baixa":
    baixa.append(descricao)
  else:
    print("Prioridade inválida. Tarefa não adicionada!")
  print()

print("Tarefas por Prioridade:")
print("Alta:", alta)
print("Média:", media)
print("Baixa:", baixa)




