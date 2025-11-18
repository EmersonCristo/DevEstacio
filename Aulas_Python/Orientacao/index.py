class NomeDaClasse: #criando uma classe
    def __init__(self, parametro1, parametro2): #aqui estamos criando o executor com o __init__, e o self é ele chamando ele mesmo
        self.parametro1 = parametro1
        self.parametro2 = parametro2

    def metodoExemplo(self):
        print("Metodo Executado")

#class >> define a classe.

#__init__() >> metodo construtor, executado automaticament ao criar o objeto.

#self >> representa o proprio objeto 

#atributos >> caracteristicas do objeto

#metodos >> comportamentos/ações/atividades 

class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        self.notas = [] #lista

    def adicionar_notas(self, nota):
        self.notas.append(nota) #aqui estamos dizendo que iremos adicionar coisas dentro da lista nota 

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def situacao(self):
        media = self.calcular_media()
        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"
        
#CRIANDO OBJETOS 

a1 = Aluno("Emerson", "Engenharia de Software")

a1.adicionar_notas(10)
a1.adicionar_notas(8)
a1.adicionar_notas(9)
print(f"{a1.nome} do curso de ({a1.curso}) - Média: {a1.calcular_media()} - {a1.situacao()}")