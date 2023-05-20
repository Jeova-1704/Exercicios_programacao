# n = int(input())

# for c in range(n):
#     valor = int(input())
#     if valor == 0:
#         print('NULL')
#         continue
#     elif valor % 2 == 0:
#         if valor < 0:
#             print('ODD NEGATIVE')
#         else:
#             print('ODD POSITIVE')
#     elif valor % 2 != 0:
#         if valor < 0:
#             print('EVEN NEGATIVE')
#         else:
#             print('EVE POSITIVE')


n=int(input())
for i in range(n):
    a=int(input())
    if(a<0):
        if(a%2==0):
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif(a>0):
        if(a % 2 == 0):
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif(a==0):
        print("NULL")