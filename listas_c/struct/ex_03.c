#include <stdio.h>

typedef struct {
    int quantidade;
    float custo;
    char nome[20];

} produto;

float valor_produto(produto produto_p) {
    return produto_p.custo * produto_p.quantidade;
}

void imprime_produto(produto produto_p) {
    printf("Quantidade %d Preço %.2f Produto %s\n", produto_p.quantidade, produto_p.custo, produto_p.nome);
}

int main() {
    produto a = {120, 0.10, "porca"};
    produto b = {80, 0.20, "parafuso"};
    float valor_a = valor_produto(a);
    float valor_b = valor_produto(b);
    float resultado = valor_a + valor_b;

    imprime_produto(a);
    imprime_produto(b);
    printf("valor total %.2f\n", resultado);
}
