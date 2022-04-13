tabelaDePrecos = {"Produto 1": ["NORMAL", 150, 10],
                  "Produto 2": ["ESPECIAL", 100, 4],
                  "Produto 3": ["NORMAL", 288, 1]}


def CalculoCarrinho(carrinho):
    frete = 0
    valor_total = 0

    for produto in carrinho:
        if produto[0] == "Produto 1":
            frete = 15

        if tabelaDePrecos[produto[0]][2] >= produto[1]:
            if tabelaDePrecos[produto[0]][0] == "ESPECIAL":
                valor_total += (tabelaDePrecos[produto[0]][1] * produto[1]) * 1.07
            else:
                valor_total += tabelaDePrecos[produto[0]][1] * produto[1]
        else:
            print("Sem estoque para o item " + produto[0])

    if frete == 0:
        frete = 5

    valor_total += frete
    if valor_total > 200:
        valor_total = valor_total * 0.9

    print(valor_total)

"""carrinho: item, quantidade"""
carrinho = (("Produto 1", 2), ("Produto 2", 4), ("Produto 3", 1))

CalculoCarrinho(carrinho)
