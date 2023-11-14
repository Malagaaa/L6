def factorial (nr):
    if nr == 0 or nr == 1:
        print (1)
        return 1
    else:
        P = nr * factorial(nr - 1)
        print (P)
        return P
       
     
#numar = int(input("Introduceti un nr !"))
factorial(5)
