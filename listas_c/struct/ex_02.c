#include <stdio.h>

typedef struct {
    int quantidade;
    float custo;
    char nome[20];

} produto;

void imprime_produto(produto produto_p) {
    printf("Quantidade %d Preço %.2f Produto %s\n", produto_p.quantidade, produto_p.custo, produto_p.nome);
}

int main() {
    produto a = {120, 0.10, "porca"};
    produto b = {80, 0.20, "parafuso"};

    imprime_produto(a);
    imprime_produto(b);
}
