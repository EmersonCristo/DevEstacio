// #include <iostream>
// #include <stdIo>

int main() {
 
char nome[30];
//float compra;
//float desconto;
float resultado, desconto = 0;
int qtdProdutos, i;
float valorProduto, total = 0;
 
printf("\n\n------Bem vindo ao Magazine TendTudo!!!-----\n\n ");
 
printf("\n----------------------------------------------\n");
 
printf("\nVerifique aqui o seu desconto!!! \n");
 
printf("\nDigite o seu nome: \n");
scanf("%s", nome);
 
printf("\n----------------------------------------------\n");
 
//printf("\nDe quanto foi sua compra? \n");
//scanf("%f", &compra);
 
printf("\nQuantos produtos você comprou? ");
scanf("%d", &qtdProdutos);
 
for (i = 1; i <= qtdProdutos; i++) {
    printf("Digite o valor do produto %d: R$ ", i);
    scanf("%f", &valorProduto);
    total += valorProduto;
}
   
if (total > 300) {
    desconto = total * 0.10;
   
} else if (total > 200) {
    desconto = total * 0.05;
   
} else if (total > 100) {
    desconto = total * 0.02;
   
} else {
    desconto = 0;
}
    resultado = total - desconto;
 
    printf("\n----------------------------------------------\n");
    printf("Cliente: %s\n", nome);
    printf("Total da compra: R$ %.2f\n", total);
 
    printf("\n----------------------------------------------\n");
   
    if (desconto > 0) {
        printf("Parabéns %s!\n", nome);
        printf("Valor da compra: R$ %.2f\n", total);
        printf("Desconto aplicado: R$ %.2f\n", desconto);
        printf("Valor final a pagar: R$ %.2f\n", resultado);
    } else {
        printf("Olá %s!\n", nome);
        printf("Infelizmente, sua compra não atingiu o valor mínimo para desconto.\n");
        printf("Valor total da compra: R$ %.2f\n", total);
    }
    printf("\n----------------------------------------------\n");
 
    printf("\nObrigado por comprar no Magazine TendTudo!\n");
 
    printf("\n----------------------------------------------\n");
 
    return 0;
 
}