"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(10000):
    print(fibonacci(i))

"""


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

def test():
    print(11111111111111111111111111111111)

for i in fab(10000):
    print(i)