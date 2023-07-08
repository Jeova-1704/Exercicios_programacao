animais = {
    ('vertebrado', 'ave', 'carnivoro'): 'aguia',
    ('vertebrado', 'ave', 'onivoro'): 'pomba',
    ('vertebrado', 'mamifero', 'onivoro'): 'homem',
    ('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
    ('invertebrado', 'inseto', 'hematofago'): 'pulga',
    ('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
    ('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
    ('invertebrado', 'anelideo', 'onivoro'): 'minhoca',
}

x = input()
y = input()
z = input()

animal = animais.get((x, y, z))
print(animal)
