    //CASO COM AND 
    //And ou E, é representado com o &&
int main() {
    float media = 8.5;
    int frequencia = 90; // Em percentual
 
    // Condição: Se (média >= 7.0) E (frequência >= 75)
    if (media >= 7.0 && frequencia >= 75) {
        printf("Aluno APROVADO! Parabéns!\n");
    } else {
        printf("Aluno REPROVADO. É necessário verificar notas ou faltas.\n");
    }
   
    // Testando um cenário reprovado (média boa, mas falta)
    media = 9.0;
    frequencia = 60;
   
    printf("\n--- Novo Teste ---\n");
    if (media >= 7.0 && frequencia >= 75) {
        printf("Aluno APROVADO! Parabéns!\n");
    } else {
        // Esta será a saída, pois a segunda condição (frequência) é falsa.
        printf("Aluno REPROVADO. É necessário verificar notas ou faltas.\n");
    }
 
    return 0;
}

    //UTILIZANDO OS 2 EXEMPLOS

    int main() {
    int a = 10, b = 3;
 
    printf("(a > 5 && b < 5): %d\n", (a > 5 && b < 5)); //a maior que 5 e b menor que 5
    printf("(a > 5 || b > 5): %d\n", (a > 5 || b > 5)); //a maior que 5 OU b é menor que 5 
    printf("!(a == 10): %d\n", !(a == 10)); // a NÃO é diferente de b, a resposta vai dar true, porque está dentro das chaves, ou seja, a não é diferente está certo, os dois tem em si o mesmo valor 10
    return 0;
}