

def fab(n):
    if n == 0 or n == 1:
        return 1
    return fab(n-1) + fab(n-2)

res = fab(5)
print res

# 1 1 2 3 5 8
# 5--> 3 4
# 3 --> 1 2
