def remainder(big, small):
    temp = big - small
    if temp >= small:
        big = temp
        remainder(big, small)
    elif temp < 0:
        print(big)
    else:
        print(temp)





big = input("please input a big number\n")
small = input("please input a small number\n")

result = remainder(int(big), int(small))


# 100-9=91-9=82-9=73-9=64-9=55-9=46-9=37-9=28-9=19-9=10-9=1