#include <stdio.h>

int main() {
    int a = 8;
    int v[] = {6,2,8,1};
    int tamanho = 3;
    
    for(int i = 0; i < tamanho; i = i + 1) {
        if(v[i] == a) {
            printf("o valor encontrado esta na posição %i", i);
        }
    }
}