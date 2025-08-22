#include <stdio.h>

int main() {
    int v[6] = {5, 4, 6, 3, 2, 1};
    int tamanho = sizeof(v) / sizeof(v[0]);
    for(int i = 0; i < tamanho; i = i + 1) {
        printf("%d ", v[i]);
    }
    printf("\n");
}