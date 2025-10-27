#include <stdio.h>

int main() {
    int m[2][3];
    int m_lin = 2;
    int m_col = 3;


    for (int i = 0; i < m_lin; i++) {
        for (int j = 0; j < m_col; j++) {
            printf("Digite o elemento na posição [%d][%d]: ", i, j);
            scanf("%d", &m[i][j]);
        }
    }
    
    printf("\nMatriz preenchida:\n");
    for (int i = 0; i < m_lin; i++) {
        for (int j = 0; j < m_col; j++) { 
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}