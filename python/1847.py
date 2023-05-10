def inverno(a, b, c):
    if(a > b):
        if c > b:
            return ':)'
        else:
            if(b-c < a-b):
                return ':)'
            else:
                return ':('
    elif(a < b):
        if c < b:
            return ':('
        else:
            if(b-c > a-b):
                return ':('
            else:
                return ':)'
    else:
        if c > a:
            return ':)'
        else:
            return ':('
 
a, b, c = map(int, input().split())
humor = inverno(a, b, c)
print(humor)

    