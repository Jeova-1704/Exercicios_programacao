I, J = [1, 0]

while I <= 9:
    J = 7
    for c in range(3):
        print(f'I={I} J={J}')
        J -= 1
    I += 2
