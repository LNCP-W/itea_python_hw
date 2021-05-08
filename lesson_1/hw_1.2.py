def fibo(x):
    z=0
    a=1
    z=b=0
    for i in range(x):
        z=a+b
        a=b
        b=z
    return z
print(fibo(10))