def isItATriangle(a, b, c):
    # Verificăm condiția pentru a reprezenta laturile unui triunghi
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False
def isRightTriangle(a, b, c):
    # Verificăm dacă triunghiul este dreptunghic
    laturi = [a, b, c]
    laturi.sort()  # Sortăm laturile în ordine crescătoare

    # Verificăm teorema lui Pitagora pentru triunghi dreptunghic
    if laturi[0]**2 + laturi[1]**2 == laturi[2]**2:
        return True
    else:
        return False

# Exemple de apelare a ambelor funcții
print(isItATriangle(1, 1, 1))  # Ar trebui să returneze True
print(isItATriangle(1, 1, 3))  # Ar trebui să returneze False

print(isRightTriangle(3, 4, 5))  # Ar trebui să returneze True (triunghi dreptunghic)
print(isRightTriangle(1, 2, 3))  # Ar trebui să returneze False (triunghi ne-dreptunghic)