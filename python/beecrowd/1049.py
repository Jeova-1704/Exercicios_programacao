# animal = input()

# if animal == "vertebrado":
#     animal = input()
#     if animal == 'ave':
#         animal = input()
#         if animal == 'carnivoro':
#             print('aguia')    
#         elif animal == 'onivoro':
#             print('pomba')
#     elif animal == 'mamifero':
#         animal = input()
#         if animal == 'onivoro':
#             print('homem')    
#         elif animal == 'herbivoro':
#             print('vaca')        

# elif animal == 'invertebrado':
#     animal = input()
#     if animal == 'inseto':
#         animal = input()
#         if animal == 'hematofago':
#             print('pulga')    
#         elif animal == 'herbivoro':
#             print('largata')
#     elif animal == 'anelideo':
#         animal = input()
#         if animal == 'hematofago':
#             print('sanguessuga')    
#         elif animal == 'onivoro':
#             print('minhoca') 


x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    animal = 'aguia'
if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    animal = 'pomba'

if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    animal = 'homem'

if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    animal = 'vaca'

if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    animal = 'pulga'

if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    animal = 'lagarta'

if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    animal = 'sanguessuga'

if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    animal = 'minhoca'

print(animal)