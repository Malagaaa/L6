
def factorial(nr):
    for i in range(1, nr+1):
        if i == 0 or i == 1:
            rezultat = 1
        rezultat = rezultat * i
        print(f"Factorialul lui {i} este {rezultat}")

    
 
numar = int(input("Introduceti un nr !"))   
factorial(numar)