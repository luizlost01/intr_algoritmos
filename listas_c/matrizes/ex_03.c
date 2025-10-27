#include <stdio.h>

int main(){
    #define M_LINHA 2
    #define M_COLUNA 3
    int m[M_LINHA][M_COLUNA] = {{1,2,3}, {4,5,6}};

    int n[M_LINHA][M_COLUNA] = {{},{}};

    for(int i = 0; i < M_LINHA; i ++) {
        for(int j = 0; j < M_COLUNA; j++) {
            n[i][j] = 0;
        }
    }

    for(int i = 0; i < M_LINHA; i++) {
        for(int j = 0; j < M_COLUNA; j++) {
            n[i][j] = m[i][j];
            printf("[%i]", n[i][j]);        
        }
    }
}