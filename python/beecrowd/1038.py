produtos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
}
prod, quant = map(int, input().split())
valor = 0

for k, v in produtos.items():
    if k == prod:
        valor = quant * v
print(f"Total: R$ {valor:.2f}")
