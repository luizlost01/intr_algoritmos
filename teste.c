#include <stdio.h>


int main() {
    int m[2][3] = {{4,5,6}, {7,8,9}};

    int m_linha = 2;
    int m_col = 3;

    for(int i = 0; i < m_linha; i++) {
        for(int j = 0; j < m_col; j++) {
            printf("[%i]", m[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}