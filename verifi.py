senhaUsuario = "Emerson"

senha = " " #Dev criou uma variavel vazia para guardar a senha 

while senha != senhaUsuario:
        senha = input("Informe sua senha: ") #Dev pediu para o usuario digitar a senha que ira entrar no lugar do vazio na varial senha.
        
        if senha == senhaUsuario:
                print("Acesso Liberado!")
                break
        else:
                print("Senha incorreta!")
                break