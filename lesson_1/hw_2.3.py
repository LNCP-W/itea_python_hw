def max_sum(a,b,c):
    x=[a,b,c]
    x.sort()
    max_sum=sum(x[1:3])
    return max_sum

print(max_sum(3,1,7))