// #include <stdio.h>

int main() {
    int idade;

    printf("Digite sua idade:");
    scanf("%d", &idade);
    printf("Hello, World! Conteúdo a mais depois dele.");

    return 0;
}

// int idade = 25; inteiro (números sem casas decimais)
// float altura = 1.75; número decimal de precisão simples
// double peso = 70.567; número decimal de precisão dupla mais preciso que o float
// char incial = 'H'; caractere único (sempre entre aspas simples)

//CONSTANTE
//Constantes são valores que não podem ser alterados durante a execução
//cont float PI = 3.14159;

// ===== SAÍDA DE DADOS =====
// printf("Idade: %d\n", idade);
// printf("Altura: %f\n", altura);
// printf("Peso: %f\n", peso);
// printf("Peso: %.3lf kg\n", peso);
// printf("Inicial: %c\n", inicial);
// printf("Constante PI: %.5f\n", PI);

// // ===== ENTRADA DE DADOS =====

// int numero;
// printf("Digite um numero inteiro: ");
// scanf("%d", &numero);  // o & indica o endereço da variável
// printf("Voce digitou: %d\n", numero);

// ===== ALTERANDO VARIÁVEIS =====

// idade = 30; // posso mudar variáveis
// printf("\nAgora a idade foi alterada para: %d\n", idade);

// PI = 3.14; // ❌ Isso daria erro, pois PI é constante

//Resumo do que aparece no código:

//int → números inteiros

//float → números decimais simples

//double → números decimais com mais precisão

//char → um único caractere

//const → define uma constante (valor fixo, não pode ser alterado)

//printf → mostra informações na tela

//scanf → recebe dados digitados pelo usuário


// Tipo	             Formato	     Observações
// char	             %c	             Um único caractere
// int 	             %d ou %i        Um inteiro (Base d ecimal)
// int 	            %o	             Um inteiro (Base o ctal)
// int	                %x ou %X	     Um inteiro (Base he x adecimal)
// short int	        %hd	             Um s h ort inteiro (Base d ecimal)
// long int	        %ld	             Um l ong inteiro (Base d ecimal)
// unsigned short int	%hu	             Short inteiro positivo
// unsigned int	    %u	             Inteiro positivo
// unsigned long int	%lu	             Long inteiro positivo
// float	            %f ou %e ou %E	 
// double	            %f ou %e ou %E	 