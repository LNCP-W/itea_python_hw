# def max_sum(a, b, c):
#     x = [a, b, c]
#     x.sort()
#     max_sum = sum(x[1:3])
#     return max_sum


def max_sum(a, b, c):
    x = [a, b, c]
    x.remove(min(x))
    return sum(x)


print(max_sum(5, 1, 7))
