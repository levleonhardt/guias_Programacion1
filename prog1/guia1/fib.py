#La sucesión de Fibonacci {f_n} se define como el resultado de la suma de los dos números anteriores, partiendo de 0, 1
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()
fib(100000)

#El primer método funciona, el segundo NO FUNCIONA. ¿Por qué?

def fib2(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a = b
        b= a + b
    print()

print("\n ||----------|| Segundo método ||----------||\n")

fib2(100000)