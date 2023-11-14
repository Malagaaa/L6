def fib(pn, apn, n):
    print(pn + apn)
    if n > 2:
        fib(pn + apn, pn, n-1)
  
fib(1, 0, 7)
