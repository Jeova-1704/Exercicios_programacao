a = int(input())
b = int(input())
c = int(input())

print(f'A = {a}, B = {b}, C = {c}, ')
print(f'A = {a:>10}, B = {b:>10}, C = {c:>10}, ')
print(f'A = {a:010d}, B = {b:010d}, C = {c:010d}, ')
print(f'A = {a:<10}, B = {b:<10}, C = {c:<10}, ')


# or

a = int(input())
b = int(input())
c = int(input())

print('A = %d, B = %d, C = %d' % (a, b, c))
print('A = %10.0d, B = %10d, C = %10d' % (a, b, c))
print('A = %s, B = %s, C = %s' % (str(a).zfill(10), str(b).zfill(10), str(c).zfill(10)))
print('A = {:<10}, B = {:<10}, C = {:<10}'.format(a, b, c))