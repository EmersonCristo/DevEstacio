#include <stdio.h>

int main() {
    for (int linha = 1; linha <= 3; linha++) {
        for (int coluna = 1; coluna <= 3; coluna++) {
            printf("%d ", linha * coluna);
        }
        printf("\n");
    }
    return 0;
}