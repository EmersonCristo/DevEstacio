# Emerson do Carmo Cristo 
#   Turma
#   Tema: Sistema de loja de jogos
#   Turma: VIV0160 / 3002 - Paradigmas de Linguagens de Programação em Python | Terça-feira
#   Data: 28/10/2025

#-------------------SISTEMA ARMAZÉM DE LOJA DE JOGOS 

print("-"*40)

# Os jogos seram armazenados nessa variavel
jogos = []

# Variável que utilizamos para controlar a quantidade e fazer a remoção de jogos 
ultimo_id = 0

# Menu principal
def menu():
    # Opções que vai aparecer para o usuario selecionar 
    print("\n ======MENU DO ARMAZÉM DE JOGOS======")
    print("1 - Cadastrar jogo")
    print("2 - Listar jogos")
    print("3 - Buscar jogo")
    print("4 - Atualizar jogo")
    print("5 - Remover jogo")
    print("6 - Estatísticas")
    print("0 - Sair")

    # Aqui estamos capturando a opção selecionada acima
    opcao = input("Escolha uma opção:")

    # nos retorna a opção selecionada
    return opcao

# 01 -----------------------FUNÇÃO CADASTRAR 
def cadastrar():

    global ultimo_id #vamos usar a variavel global para controlar o id 

    nome = input("Nome do jogo: ").strip() #strip serve para "Limpar os restante do que o usuario escrever"
    plataforma = input("Plataforma (ex: PC, PS5, Xbox): ").strip()
    preco = input("Preço do jogo (R$): ").strip()
    estoque = input("Quantidade em estoque: ").strip()

    # Validação de dados 
    if not nome or not plataforma or not preco.replace('.', '', 1).isdigit() or not estoque.isdigit():
    # Se qualquer uma das opções acima forem True 
        print("❌ Dados inválidos. Verifique nome, plataforma, preço e quantidade.")
        return

    # Convertendo os valores das variaveis 
    preco = float(preco)
    estoque = int(estoque)

    # Fazendo a verificação se aquele jogo e a plataforma já está cadastrado ou não 
    for j in jogos:
        if j["nome"].lower() == nome.lower() and j["plataforma"].lower() == plataforma.lower():
    # acima usamos o .lower para capturar todos os dados que o usuario passar de convertido em letras minusculas
            print("⚠️ Esse jogo já está cadastrado nessa plataforma.")
            return

    # Caso tudo de certo com o cadastro será adicionado um valor a variavel global ultimo_id
    ultimo_id += 1

    # Abaixo utilizamos um dicionario para salvar todos os dados do jogo que o usuario nos enviar 
    novo_jogo = {
        "id": ultimo_id, # a chave já vem pré definida pelo ultimo_id 
        "nome": nome,
        "plataforma": plataforma,
        "preco": preco,
        "estoque": estoque
    }

    # Adicionamos esses dados da variavel novo_jogo dentro da variavel jogos
    jogos.append(novo_jogo)

    print("✅ Jogo cadastrado com sucesso!")

# 02 ---------------------------FUNÇÃO LISTAR

# Essa função é mais simples que a primeira, seu trabalho é somente conferir se tem jogos, se for true, vai mostrar os dados na tela para o usuario
def listar():
    
    if not jogos:
        print("Nenhum jogo cadastrado.")
        return

    # Exibe os jogos em ordem alfabética
    print("\n🎮 LISTA DE JOGOS DISPONÍVEIS:")
    for j in sorted(jogos, key=lambda x: x["nome"].lower()): #sorted nos trás os itens de forma ordenada
        print(f'ID: {j["id"]} | {j["nome"]} ({j["plataforma"]}) | R$ {j["preco"]:.2f} | Estoque: {j["estoque"]}') # Aqui nós imprimimos o resultado já formatando a saida dele


# ---------------------------FUNÇÃO BUSCAR

def buscar():
    """Busca jogos pelo nome (busca parcial)."""
    termo = input("Digite parte do nome do jogo: ").strip().lower() # nos pedimos um dado que esteja no dicionario que criamos, formatamos esse dado e atribuimos ele a variavel termo

    # Cria lista com resultados que contêm o termo
    encontrados = [j for j in jogos if termo in j["nome"].lower()] #aqui recebemos os dados do usuario e os formatamos para futuramente fazer a verificação

    #Iremos mostrar o resultado aos usuarios
    if encontrados:
        print("\n🔎 Resultados da busca:")
        for j in encontrados:
            #Se achar algo vai printar a lista completa do jogo 
            print(f'ID: {j["id"]} | {j["nome"]} ({j["plataforma"]}) | R$ {j["preco"]:.2f} | Estoque: {j["estoque"]}')
    else:
        print("❌ Nenhum jogo encontrado.")


# ---------------------------FUNÇÃO ATUALIZAR 

def atualizar():
    
    #Aqui perguntamos ao usuario qual o id do produto que ele está procurando
    try: #try e except é uma forma de perguntar um dado ja formantando a resposta se algo der errado
        id_busca = int(input("Digite o ID do jogo para atualizar: "))
    except ValueError: #se algo der errado
        print("❌ ID inválido.")
        return #retorna a função ao inicio 

    # Procura o jogo correspondente ao ID
    for j in jogos:
        if j["id"] == id_busca:
            print(f"Editando '{j['nome']}'...")

            novo_nome = input("Novo nome (Enter para manter): ").strip()
            nova_plataforma = input("Nova plataforma (Enter para manter): ").strip()
            novo_preco = input("Novo preço (Enter para manter): ").strip()
            novo_estoque = input("Nova quantidade (Enter para manter): ").strip()
            #caso o usuario passar dados novos, nós salvamos os mesmo em suas respectivas variaveis já formatados em minusculo

            # Atualiza apenas os campos informados
            if novo_nome:
                j["nome"] = novo_nome
            if nova_plataforma:
                j["plataforma"] = nova_plataforma
            if novo_preco.replace('.', '', 1).isdigit():
                j["preco"] = float(novo_preco)
            if novo_estoque.isdigit():
                j["estoque"] = int(novo_estoque)
            #salvando os valores novos, (se digitados) dentro do dicionario

            print("✅ Jogo atualizado com sucesso!")

            return

    # Caso o ID não exista
    print("❌ Jogo não encontrado.")

    # ---------------------------FUNÇÃO REMOVER

    def remover():
        try:
            # Basicamente a mesma coisa que a função acima 
            id_busca = int(input("Digite o ID do jogo para remover: "))
        except ValueError:
            print("❌ ID inválido.")
            return

        # aqui logicamente trocamos de atualizar os dados 
        for j in jogos:
            if j["id"] == id_busca:
                jogos.remove(j) # E removemos da memoria qualquer dado que for encontrado se os mesmo forem similares aos digitados
                print("🗑️ Jogo removido com sucesso!")
                return

        print("❌ Jogo não encontrado.")

# ---------------------------
# Função: estatisticas()
# ---------------------------
def estatisticas():
    #informações de jogos
    if not jogos:
        print("Nenhum jogo cadastrado.")
        return

    # Abaixo viram o nossos calculos de jogos 
    total_jogos = len(jogos) #numero de jogos unidade
    total_estoque = sum(j["estoque"] for j in jogos) #soma o número do estoque com o de todos os jogos 

    # Exibe os resultados
    print("\n📊 ESTATÍSTICAS DO ARMAZÉM:")
    print(f"Total de títulos cadastrados: {total_jogos}")
    print(f"Total de unidades em estoque: {total_estoque}")

#----------------------------FUNÇÃO PRINCIPAL

def main():
    # Aqui é nossa base para controlar o sistema
    while True:
        # guardamos o valor que o usuario digitou nessa varial para saber com quais das funções devemos seguir 
        opcao = menu()

        if opcao == "1":
            cadastrar() #se o usuario digitou 1 disparar função
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            atualizar()
        elif opcao == "5":
            remover()
        elif opcao == "6":
            estatisticas()
        elif opcao == "0":
            print("Saindo do sistema... 👋")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

main()


