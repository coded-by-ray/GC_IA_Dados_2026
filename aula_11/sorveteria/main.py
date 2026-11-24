import random

cardapio = {
    "tradicionais": {
        "chocolate": 5.00,
        "baunilha": 4.50,
        "morango": 3.00
    },
    "especiais": {
        "flocos": 9.00
    }
}


brindes = ["Canudo", "Copo personalizado", "Gelo", "Badge"]


def mostrar_cardapio():
    print("-- CARDÁPIO --")

    for categoria, sabores in cardapio.items():
        print(f"\n{categoria.upper()}")

        for sabor, preco in sabores.items():
            print(f"{sabor}, R$ {preco:.2f}")

def sabor_do_dia():
    sabores_disponiveis = []

    for sabores in cardapio.values():
        sabores_disponiveis.extend(sabores.keys())

    sabor = random.choice(sabores_disponiveis)

    print(f"\nSabor do dia: {sabor}")

def cadastrar_sabor():
    categoria = input("Categoria (tradicionais/especiais): ").strip().lower()

    if categoria not in cardapio:
        print("Categoria inválida!")
        return

    sabor = input("Digite o novo sabor: ").strip().lower()

    if not sabor or sabor == "fechar":
        print("Sabor inválido!")
        return

    for sabores in cardapio.values():
        if sabor in sabores:
            print("Sabor já cadastrado!")
            return

    try:
        preco = float(input("Digite o preço: R$ ").replace(",", "."))

        if preco <= 0:
            print("O preço deve ser maior que zero!")
            return

        cardapio[categoria][sabor] = preco
        print(f"{sabor} cadastrado com sucesso!")

    except ValueError:
        print("Preço inválido!")

def fazer_pedido():
    total = 0
    pedido = []

    while True:
        sabor = input("\nEscolha o sabor (digite 'fechar' para sair): ").strip().lower()

        if sabor == "fechar":
            break

        preco = None

        for sabores in cardapio.values():
            preco = sabores.get(sabor)

            if preco is not None:
                break

        if preco is not None:
            total += preco
            pedido.append(sabor)
            print(f"{sabor} adicionado!")
        else:
            print("Sabor não está no cardápio")

    return pedido, total

def promocao_do_dia(total):
    descontos = [5, 10, 15]

    desconto = random.choice(descontos)

    valor_desconto = total * (desconto / 100)

    total_final = total - valor_desconto

    return desconto, total_final

def mostrar_resumo(pedido, total):
    print("\n-- RESUMO DO PEDIDO --")

    contador = {}

    for sabor in pedido:
        contador[sabor] = contador.get(sabor, 0) + 1

    for sabor, quantidade in contador.items():
        print(f"- {sabor}: {quantidade}x")

    desconto, total_final = promocao_do_dia(total)

    print(f"Subtotal: R$ {total:.2f}")
    print(f"Desconto do dia: {desconto}%")
    print(f"Total a pagar: R$ {total_final:.2f}")

    if total > 20:
        brinde = random.choice(brindes)
        print(f"Parabéns! Você ganhou: {brinde}")


opcao = input("Deseja cadastrar um novo sabor? (s/n): ").strip().lower()

if opcao == "s":
    cadastrar_sabor()

mostrar_cardapio()

sabor_do_dia()

pedido, total = fazer_pedido()

mostrar_resumo(pedido, total)