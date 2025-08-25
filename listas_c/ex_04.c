#include <stdio.h>

int main() {
    int np = 0;
    int ni = 0;
    int v[6] = {1, 4, 6, 5, 8, 2};
    int tamanho = sizeof(v) / sizeof(v[0]);

    for(int i = 0; i < tamanho; i = i + 1) {
        if(v[i] % 2 == 0) {
            np++;
        }
        else {
            ni++;
        }
    }
    printf("%d,%d", np,ni);
}