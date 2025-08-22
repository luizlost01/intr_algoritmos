#include <stdio.h>

int main() {
    int v[] = {5,2,7,4};

    for(int i = 0; i < 5; i = i + 1) {
        if(v[i] == 5) {
            printf("Existe o Numero 5\n");
        };
    };
}