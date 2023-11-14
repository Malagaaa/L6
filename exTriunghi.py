#Scrieți un program în care să definiți și să apelați o funcție care verifică dacă teri numere pot reprezenta laturile unui triunghi.
#Info: se cunoaște regula că pentru a reprezenta laturile unui triunghi suma oricăror două laturi trebuie să fie mai mare strict decât cea de-a treia latură
#Exemplu apelare:
#print(isItATriangle(1, 1, 1))
#print(isItATriangle(1, 1, 3))
def isItATriangle(a, b, c):
    # Verificăm condiția pentru a reprezenta laturile unui triunghi
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

# Exemple de apelare a funcției
print(isItATriangle(1, 1, 1))  # True
print(isItATriangle(1, 1, 3))  # False
