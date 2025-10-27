#include <stdio.h>

int main() {
    int v[6] = {11, 22, 33, 44, 55, 66};
    int tamanho = sizeof(v) / sizeof(v[0]);

    int r[tamanho];
    for (int i = 0; i < tamanho; i++) {
        r[i] = v[tamanho - 1 - i];
    }
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", r[i]);
    }
    printf("\n");
}
