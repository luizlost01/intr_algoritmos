#include <stdio.h>

int main() {
    #define M_LINHA 2
    #define M_COLUNA 3
    int aux[3] = {};

    int m[M_LINHA][M_COLUNA] = {{1,2,3},{4,5,6}};
    

    for(int i = 0; i < M_LINHA; i++) {
        for(int j = 0; j < M_COLUNA; j++) {
            aux[j] = m[i][j];
        }
    }

}