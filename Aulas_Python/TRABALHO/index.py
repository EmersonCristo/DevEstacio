# =========================================================
# SISTEMA DE BIBLIOTECA
# Autor: Seu Nome
# Objetivo: Gerenciar cadastro de livros (cadastrar, listar,
# buscar, atualizar, remover) usando listas e dicionários.
# =========================================================

# Lista principal de registros (aqui ficam todos os livros)
livros = []

# Variável para gerar IDs únicos para cada livro
ultimo_id = 0


# ---------------------------
# Função: menu()
# ---------------------------
def menu():
    """Exibe o menu e retorna a opção escolhida pelo usuário."""
    # Exibe as opções do menu na tela
    print("\n=== MENU ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Atualizar livro")
    print("5 - Remover livro")
    print("6 - Estatísticas")
    print("0 - Sair")

    # Captura a escolha do usuário
    opcao = input("Escolha uma opção: ")

    # Retorna a opção para o programa principal
    return opcao


# ---------------------------
# Função: cadastrar()
# ---------------------------
def cadastrar():
    """Cadastra um novo livro, validando entradas e evitando duplicatas."""
    # Declara que vamos usar a variável global ultimo_id
    global ultimo_id

    # Pede os dados do livro ao usuário
    titulo = input("Título do livro: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()

    # Valida os campos: não podem estar vazios e o ano deve ser um número
    if not titulo or not autor or not ano.isdigit():
        print("❌ Dados inválidos. Verifique os campos.")
        return  # Sai da função sem cadastrar

    # Verifica se o livro já foi cadastrado (evita duplicatas)
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            print("⚠️ Livro já cadastrado.")
            return

    # Incrementa o ID automaticamente
    ultimo_id += 1

    # Cria um novo dicionário com os dados do livro
    novo_livro = {
        "id": ultimo_id,
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano)
    }

    # Adiciona o dicionário à lista principal
    livros.append(novo_livro)

    # Mensagem de sucesso
    print("✅ Livro cadastrado com sucesso!")


# ---------------------------
# Função: listar()
# ---------------------------
def listar():
    """Lista todos os livros cadastrados, ordenados por título."""
    # Verifica se há livros cadastrados
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    # Exibe os livros na tela, ordenados pelo título (ordem alfabética)
    print("\n📚 LISTA DE LIVROS:")
    for livro in sorted(livros, key=lambda x: x["titulo"].lower()):
        print(f'ID: {livro["id"]} | {livro["titulo"]} - {livro["autor"]} ({livro["ano"]})')


# ---------------------------
# Função: buscar()
# ---------------------------
def buscar():
    """Busca livros pelo título (busca parcial)."""
    # Pede parte do título ao usuário
    termo = input("Digite parte do título: ").strip().lower()

    # Cria uma lista com os livros que contêm o termo buscado
    encontrados = [l for l in livros if termo in l["titulo"].lower()]

    # Se encontrou algum livro, mostra na tela
    if encontrados:
        print("\n🔎 Resultados da busca:")
        for l in encontrados:
            print(f'ID: {l["id"]} | {l["titulo"]} - {l["autor"]} ({l["ano"]})')
    else:
        # Caso contrário, mostra mensagem de erro
        print("❌ Nenhum livro encontrado.")


# ---------------------------
# Função: atualizar()
# ---------------------------
def atualizar():
    """Atualiza os dados de um livro pelo ID."""
    try:
        # Tenta converter o ID digitado em número inteiro
        id_busca = int(input("Digite o ID do livro para atualizar: "))
    except ValueError:
        # Se o usuário digitar algo que não seja número, mostra erro
        print("❌ ID inválido.")
        return

    # Percorre todos os livros cadastrados
    for livro in livros:
        # Quando encontra o ID desejado
        if livro["id"] == id_busca:
            print(f"Editando '{livro['titulo']}'...")

            # Pede novos dados, permitindo deixar campos vazios (para manter os antigos)
            novo_titulo = input("Novo título (ou Enter para manter): ").strip()
            novo_autor = input("Novo autor (ou Enter para manter): ").strip()
            novo_ano = input("Novo ano (ou Enter para manter): ").strip()

            # Atualiza somente se o usuário digitou algo novo
            if novo_titulo:
                livro["titulo"] = novo_titulo
            if novo_autor:
                livro["autor"] = novo_autor
            if novo_ano.isdigit():
                livro["ano"] = int(novo_ano)

            print("✅ Livro atualizado com sucesso!")
            return  # Sai da função após atualizar

    # Caso o ID não seja encontrado
    print("❌ Livro não encontrado.")


# ---------------------------
# Função: remover()
# ---------------------------
def remover():
    """Remove um livro pelo ID."""
    try:
        # Solicita o ID e tenta converter para número
        id_busca = int(input("Digite o ID do livro para remover: "))
    except ValueError:
        # Caso o valor não seja numérico
        print("❌ ID inválido.")
        return

    # Percorre a lista para encontrar o livro
    for livro in livros:
        if livro["id"] == id_busca:
            # Remove o livro da lista
            livros.remove(livro)
            print("🗑️ Livro removido com sucesso!")
            return

    # Caso o ID não seja encontrado
    print("❌ Livro não encontrado.")


# ---------------------------
# Função: estatisticas()
# ---------------------------
def estatisticas():
    """Exibe estatísticas básicas do acervo."""
    # Se não houver livros, mostra aviso
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    # Calcula estatísticas básicas
    total = len(livros)  # Total de livros
    anos = [l["ano"] for l in livros]  # Lista com os anos de cada livro

    # Exibe resultados
    print("\n📈 ESTATÍSTICAS:")
    print(f"Total de livros: {total}")
    print(f"Ano mais antigo: {min(anos)}")
    print(f"Ano mais recente: {max(anos)}")
    print(f"Média dos anos: {sum(anos)/total:.1f}")


# ---------------------------
# Função principal: main()
# ---------------------------
def main():
    """Controla o fluxo principal do programa."""
    # Laço principal: roda até o usuário escolher sair
    while True:
        # Mostra o menu e pega a opção
        opcao = menu()

        # Chama a função correspondente à opção
        if opcao == "1":
            cadastrar()
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
            # Encerra o programa
            print("Saindo do sistema... 👋")
            break
        else:
            # Opção inválida
            print("❌ Opção inválida. Tente novamente.")


# ---------------------------
# Execução do programa
# ---------------------------
# Este bloco garante que o programa só será executado
# se for rodado diretamente (não importado como módulo).
if __name__ == "__main__":
    main()
