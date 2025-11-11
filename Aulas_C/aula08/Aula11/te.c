// Um vetor é uma estrutura de dados homogênea, ou seja, armazenar vários valores do mesmo tipo em uma única váriável, acessados por índices.

#include <stdio.h>

int main() {

    int numeros[5] = {10, 20, 30, 40, 50};

    printf("O primeiro elemento é: %d\n", numeros[0]);
    printf("O último elemento é: %d\n", numeros[4]);

    return 0;
}

int main() {

// tipos de inicialização    
int vetor2[3]; // declaração vazia
int vetor[11] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; //inicialização direta
int valores[5] = {1, 2}; // inicialização parcial
printf("%d", vetor[10]);

return 0;
}

int main() {

    int v[3] = {5, 10, 15};

    printf("v[1] = %d\n", v[1]);
    v[1] = 20; // altera o segundo elemento
    printf("v[1] = %d\n", v[1]);

return 0;
}

int main() {
    int numeros[5];

    for (int i = 0; i < 5; i++) {
        printf("Digite o número %d: ", i + 1);
        scanf("%d", &numeros[i]);
    }

    printf("\nVocê digitou:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numeros[i]);
    }

    return 0;
}

int main () {
    char nomes[7][50]; //numero máximo e tamanha máximo
    int i;

    for (i = 0; i < 7; i++) {
        printf("Digite um nome %d:", i + 1);
        scanf("%49s", nomes[i]);
    }

    printf("\nVocê digitou:\n");
    for (int i = 0; i < 7; i++) {
        printf("%s\n ", numeros[i]);
    }

    return 0;
}

//Código do professor 

#define LIMITE_FRASES 4
#define TAM_MAXIMO 60

int main() {
    char banco_frases[LIMITE_FRASES][TAM_MAXIMO];
    int contador;

    printf("--- Insira as entradas ---\n");

    for (contador = 0; contador < LIMITE_FRASES; contador++) {
        printf("Entre com a entrada #%d: ", contador + 1);
        scanf("%59s", banco_frases[contador]);
    }

    printf("\n--- Entradas registradas ---\n");

    for (contador = 0; contador < LIMITE_FRASES; contador++) {
        printf("Entrada #%d: %s\n", contador + 1, banco_frases[contador]);
    }

    return 0;
}

// média 

int main() {
    float notas[4];
    float soma = 0;

    for (int i = 0; i < 4; i++) {
        printf("Digite a nota %d: ", i + 1);
        scanf("%f", &notas[i]);
        soma += notas[i];
    }

    printf("Média = %.2f\n", soma / 4);
    return 0;
}

//Esse código eu não mandei para o professor pois fiz com AI

int main() {
    // Declaração das variáveis
    int numeros[10];       // Vetor que pode armazenar até 10 números inteiros
    int quantidade;        // Variável para guardar quantos números o usuário vai digitar
    int i;                 // Variável de controle usada nos laços de repetição
    int maior, menor;      // Variáveis que armazenarão o maior e o menor número digitado

    // Pede ao usuário quantos números ele deseja digitar (limite máximo de 10)
    printf("Quantos numeros voce deseja digitar (maximo 10)? ");
    scanf("%d", &quantidade); // Lê o valor digitado e armazena em 'quantidade'

    // Verifica se o número digitado é válido (entre 1 e 10)
    if (quantidade > 10 || quantidade <= 0) {
        // Caso o usuário digite um número fora do intervalo permitido
        printf("Quantidade invalida! Digite um valor entre 1 e 10.\n");
        return 1; // Encerra o programa com código de erro (1 indica algo incorreto)
    }

    // Loop para ler os números digitados pelo usuário
    for (i = 0; i < quantidade; i++) {
        // Mostra qual número está sendo solicitado (por exemplo: "Digite o 1º numero")
        printf("Digite o %dº numero: ", i + 1);

        // Lê o número digitado e armazena na posição correspondente do vetor 'numeros'
        scanf("%d", &numeros[i]);
    }

    // Inicializa as variáveis 'maior' e 'menor' com o primeiro número digitado
    // Isso serve de ponto de partida para as comparações seguintes
    maior = menor = numeros[0];

    // Loop para percorrer todos os números e encontrar o maior e o menor
    for (i = 1; i < quantidade; i++) {
        // Verifica se o número atual é maior que o maior encontrado até agora
        if (numeros[i] > maior) {
            maior = numeros[i]; // Atualiza o valor de 'maior'
        }

        // Verifica se o número atual é menor que o menor encontrado até agora
        if (numeros[i] < menor) {
            menor = numeros[i]; // Atualiza o valor de 'menor'
        }
    }

    // Exibe os resultados na tela para o usuário
    printf("\nO maior numero digitado foi: %d\n", maior);
    printf("O menor numero digitado foi: %d\n", menor);

    // Retorna 0 indicando que o programa terminou corretamente
    return 0;
}

//código professor guardar maior número, e menor número 

int main() {
    int v[5];
    int maior, menor;

    // Leitura dos valores digitados pelo usuário
    for (int i = 0; i < 5; i++) {
        printf("Digite o %dº número: ", i + 1);
        scanf("%d", &v[i]);
    }

    // Inicializa maior e menor com o primeiro valor digitado
    maior = v[0];
    menor = v[0];

    // Percorre o vetor para encontrar maior e menor
    for (int i = 1; i < 5; i++) {
        if (v[i] > maior)
            maior = v[i];
        if (v[i] < menor)
            menor = v[i];
    }

    printf("\nMaior número: %d\n", maior);
    printf("Menor número: %d\n", menor);

    return 0;
}

//soma de vetor

int somaVetor(int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++)
        soma += v[i];
    return soma;
}

int main() {
    int v[4] = {10, 20, 30, 40};
    printf("Soma = %d\n", somaVetor(v, 4));
    return 0;
}

//mesmo exemplo de cima, porém, multiplicando 

int somaVetor(int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++)
        soma *= v[i];
    return soma;
}

int main() {
    int v[4] = {10, 20, 30, 40};
    printf("Multiplicação = %d\n", somaVetor(v, 4));
    return 0;
}


