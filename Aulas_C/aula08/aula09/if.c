// #include <stdio.h> USADO PARA CODIFICAR EM C NO VS, PORÉM, PRECISO REINSTALAR E CORRIGIR O ERRO E ESTÁ DANDO 

int main() {
    int idade;
    printf("Digite sua idade: ");
    scanf("%d", &idade);

    if (idade >= 18) {
        printf("Você é maior de idade. \n");

        return 0;
    }
}

// EXERCICIO DE GRAUS

int main() {
    int temperatura;
    printf("Qual a temperatura atual?: ");
    scanf("%d", &temperatura);

    if (temperatura <= 20) {
        printf("Coloque seu bobojaco e sua touca, porque faz menos de 20graus em SP AHHAH AAAHAHH");
    } else {
        printf("Tempo tranquilo, use uma camiseta ou regata XD");
    }
}

//ESTRUTURA ENCADEADA 

int main() {
    float nota;
    printf("Digite a nota do aluno: ");
    scanf("%f", &nota);

    //ESTRUTURA ENCADEADA É QUANDO TEMOS VARIAS POSSIVEIS SAIDA DE DADOS, COMO O EXEMPLO A SE SEGUIR 
    if (nota >= 9) {
        printf("Excelente nota! \n");
    } else if (nota >= 7) {
        printf("Bom desempenho. \n");
    } else if (nota >= 5) {
        printf("Em recuperação. \n");
    } else {
        printf("Reprovado. \n");
    }

    return 0;
}

//EXERCICIO DE ESTRUTURA ENCADEADE

int main() {
    int a;
    int b;
    
    printf("Digite o um número: ");
    scanf("%d", &a);

    printf("Digite o outro número: ");
    scanf("%d", &b);

    if (a > b) {
        printf("O número que você digitou %d, é maior que o número que você digitou %d", a, b);
    } else if (b > a) {
        printf("O número que você digitou %d, é maior que o número que você digitou %d", b, a);
    } else if (a == b) {
        printf("Você digitou dois números igual meu nobre, ta tirando? É os D VIDA!");
    } else {
        prinft("Leia novamente, e faça de novo, you is burro brow?????");
    }
}

//PODEMOS DEIXAR ESSE CÓDIGO DE UMA FORMA MAIS "RÁPIDA", FAZENDO O USUARIO DIGITAR OS 2 DADOS DE UMA ÚNICA VEZ

int main() {
    int a, b;
    
    printf("Digite dois números (separados por espaço): ");
    scanf("%d %d", &a, &b); // assim podemos já escanear e atribuir as duas á suas respectivas variaveis


    if (a > b) {
        printf("O número que você digitou %d, é maior que o número que você digitou %d", a, b);
    } else if (b > a) {
        printf("O número que você digitou %d, é maior que o número que você digitou %d", b, a);
    } else if (a == b) {
        printf("Você digitou dois números igual meu nobre, ta tirando? É os D VIDA!");
    } else {
        prinft("Leia novamente, e faça de novo, you is burro brow?????");
    }
}