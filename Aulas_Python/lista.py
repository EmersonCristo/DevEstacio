minha_lista = [10, 20, 30, 40, 50, "Emerson", "Dragão", "Carro"]

print(minha_lista[5]) #vai trazer o elemento de indice 0, lembrando que o computador conta o 0 como elemento contavel 

#normalmente utilizada para guardar dados 
#esses dados podem ser alterados 

minha_lista[1] = "Caraxes"
print(minha_lista)

#podemos adicionar elementos na lista sem mexer nela diretamente 
#ctrl + Z não funciona se alterar os dados 

minha_lista.append(60) #o elemento vai para o final da fila 
print(minha_lista)

#podemos remover os dados da lista 
minha_lista.remove(50)
print(minha_lista)
