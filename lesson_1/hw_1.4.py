flag = True
sum_x = 0

while flag:
    x = (input('Введите строку чисел через пробел ').split())
    for i in x:
        try:
            i = int(i)
            sum_x = sum_x + int(i)
        except ValueError:
            print(sum_x)
            flag = False
            break
    if not flag:
        break
    else:
        print(sum_x)
