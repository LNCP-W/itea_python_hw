# функция генератор для факториала

def fact_gen(n):
    fact, next_num = 1, 1
    while next_num <=  n:
        yield fact
        next_num += 1
        fact *= next_num

a = fact_gen(4)
print(next(a))
print(next(a))
print(next(a))

for i in fact_gen(20):
    print(i)


