// MATRIZ - é uma estrutura de dados composta por diversos elementos do mesmo tipo, organizado em linhas e colunas.

// Na prática ela é um array bidimensional 

// array - Estrutura que armazena múltiplos valores em sequência 

// Deminsão Qauntidade de eixos (1D = vetor, 2D = Matriz, 3D = Cubo).

// Indice - Posição do elemento (sempre começa em 0 em C).

// Linha - conjunto horizontal de elementos 

// Coluna - Conjunto vertical de elementos 

// SINTAXE DE MATRIZ 

// Tipo nome [linhas] [colunas]

int main() {
    int matriz[2][3] = {
        {1, 2, 3}, // Linha 0
        {4, 5, 6}  // Linha 1
    }

    printf("Elementos da matriz: \n");

    for (int i = 0; i < 2; i++) {        //percorre linhas
        for (int j = 0; j < 3; j++){     //percorre colunas 
            printf("%d", matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
};

#include <stdio.h>

int main() {
    int m[3][3];

    printf("Digite os valores da matriz 3x3:\n");

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("m[%d][%d] = ", i, j);
            scanf("%d", &m[i][j]);   // & passa o endereço de memória
        }
    }

    printf("\nMatriz digitada:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            printf("%d ", m[i][j]);
        printf("\n");
    }

    return 0;
}
