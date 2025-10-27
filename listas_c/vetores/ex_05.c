#include <stdio.h>


int main() {
    int v[5] = {1, 2, 3, 4, 5};
    int tamanho = sizeof(v[0]) / sizeof(v);

     for(int i = 6; i >= tamanho; i = i - 1) {
        printf("%d\n", v[i]);
     }

}