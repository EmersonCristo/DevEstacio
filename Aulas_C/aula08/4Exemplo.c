#include <stdbool.h> //para conseguir utilizar o tipo booleno, false/true

int main() {
    int idade = 17;
    bool tem_permissao = true; //variavel tem_permissão, está recebendo o valor verdadeiro, definindo a variavel com o Bool não frente

    // Condição: Se (idade é maior ou igual a 18) OU (tem permissão é verdadeiro)
    if (idade >= 18 || tem_permissao == true) {// O || funciona como o OU no caso ou tem idade maior a 18, ou tem_permissão for igual a verdadeiro
        printf("Acesso permitido.\n");
    } else {
        printf("Acesso negado.\n");
    }

    return 0;
}