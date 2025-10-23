
// int main(){

//     int idade;
//     printf("Digite sua idade: ");
//     scanf("%d", &idade); // vai escanear oque o usuario digitou e guardar na variavel idade
//     printf("Você tem %d anos. \n", idade);

//     return 0; // lembrando que o return 0, é para dizer que o código foi finalizado sem erros 
// }

//EXERCICIOS 
// FEITO POR MIM

// int main() {

//         char nome;
//         int idade;
//         float altura;

//         printf("Digite seus dados a seguir: \n");
//         scanf("%s", &nome, "%d", &idade, "%f.2", &altura);
//         printf("Seu nome é %s, você tem %d anos de idade, e sua altura é %f");

//         return 0;
// }

// EXEMPLO DO PROFESSOR

int main() {
    
    char nome[30]; // em testo o professor esta definindo o valor maximo de caractéres
    float peso;
    char dataNasc[11];

    printf("Digite seu nome: ");
    scanf("%s", nome); // %s porque é uma string, e nome para já armazenalo no proprio 

    printf("Digite sua data de nascimento: ");
    scanf("%s", &dataNasc); // seguimos a ordem nessa linha, escanear/definindo o estilo da varivavel/ e direcionando o dado digitado para a variavel 

    printf("Digite seu peso: ");
    scanf("%f", &peso);

    printf("\nCadastro realizado!");
    printf("Nome: %s\nData de Nascimento: %s\nPeso: %.1f kg\n", nome, dataNasc, peso);
    // como podemos ver na linha acima as variaveis vem atrás do que vai escrito e são separadas por virgula, temos que seguir a sequencia que desejamos que seja empressa ao usuário, os %s por exemplo, é apenas para formatar a saida dos dados.

    return 0;
}
