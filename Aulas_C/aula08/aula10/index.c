#include <stdio.h>

// for (inicialização, condição, incremento) 
    // bloco de comandos

int main() {
    for (int i = 1; i <= 5; i++) {
        printf("Numero: %d\n", i);
    }
    return 0;
}

// MESMO SISTEMA SÓ QUE AO CONTRARIO 

int main() {
    for (int i = 10; i >= 1; i--) {
        printf("Numero: %d\n", i);
    }
    return 0;
}

//EXERCICIO DA AULA SUBINDO DE 2 EM 2

// CÓPIA DE OUTROS ALUNOS 

int main() {

    for (int i = 0; i <= 30; i+=2) {
        printf("Número: %d\n", i);
    }
    return 0;
}

int main() {
    int n, soma = 0;
    printf("Digite um número: ");
    scanf("%d", &n);

    for (int i = 1; i <=n; i++) {
        soma += i; // soma = soma + i
    }

    printf("A soma de 1 até %d é %d", n, soma);
    return 0;
}

// EXERCICIO 

int main() {
    int i, inicio, fim;

    printf("Digite o valor inicial: ");
    scanf("%d", &inicio);

    printf("Digite o valor final: ");
    scanf("%d", &fim);

    for (i = inicio; i <= fim; i++) {
        printf("%d\n", i);
    }
    return 0;
}

// EXERCICIO PARTE 2

int main() {
    int i, inicio, fim;

    printf("Digite o valor inicial: ");
    scanf("%d", &inicio); 

    printf("Digite o valor final: ");
    scanf("%d", &fim);

    printf("\nIniciando a contagem...\n");

    if (inicio <= fim) {

        printf("Contando de forma crescente:\n");
        for (i = inicio; i <= fim; i++) {
            printf("%d\n", i);
        }
    
    } else {
        printf("Contando de forma decrescente:\n");
    for (i = inicio; i >= fim; i--) {
            printf("%d\n", i);
        }
    }

    return 0;
}
