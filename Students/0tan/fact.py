
def fact(x):
    sum=1
    for i in range(1, x):
        if i<x:
            sum *= i
        else:
            break
    print(sum)

fact(5)