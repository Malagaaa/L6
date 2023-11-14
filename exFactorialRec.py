#Scrieți un program care să definească și să utilizeze o funcție pentru determinarea valorii factoriale a unui număr.

def factorial (nr):
    if nr == 0 or nr == 1:
        return 1
    else:
        return nr * factorial(nr - 1)
    
numar = int(input("Introduceti un nr !"))
for i in range (numar + 1):
    rezultat = factorial(i)
    print(f"Factorialul lui {i} este {rezultat}")
