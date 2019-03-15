
str = "1\t2\t3\t"
a = str.strip().split("\t")
with open('data.txt', 'w') as f:
    for s in a:
        f.write("%s\t" % (s))
