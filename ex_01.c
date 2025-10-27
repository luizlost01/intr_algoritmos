#include <stdio.h>

int main() {
    char nome[100];
    printf("Digite Seu Nome: ");
    scanf("%99s", nome);
    printf("Hello %s", nome);
}