"""
Welcome to the Adder REPL.
??? a gets 1
??? input b
Enter a value for b: 2
??? c gets a
??? c adds b
??? print a
a equals 1
??? print b
b equals 2
??? print c
c equals 3
??? print z
z is undefined.
??? print 32
32
??? blerg
Syntax error.
??? 23 gets z
Syntax error.
??? quit
Goodbye.
"""

# a = "b"
# print a.isalpha()

d = dict()
a_input = raw_input("Welcome to the Adder REPL.\n??? ").strip()
while a_input != "quit":
    if len(a_input.split(" ")) > 1 and a_input.split(" ")[1] == "gets":
        # print a_input.split(" ")[0]
        # print a_input.split(" ")[-1]
        if a_input.split(" ")[-1].isdigit() and a_input.split(" ")[0].isalpha():
            d[a_input.split(" ")[0]] = int(a_input.split(" ")[-1])
        elif a_input.split(" ")[-1].isalpha() and a_input.split(" ")[0].isalpha():
            d[a_input.split(" ")[0]] = d[a_input.split(" ")[-1]]
        else:
            print "Syntax error."
        a_input = raw_input("??? ").strip()
        continue
    if a_input.split(" ")[0] == "input":
        var = a_input.split(" ")[1]
        a_input = raw_input("Enter a value for b: ").strip()
        d[var] = int(a_input)
        a_input = raw_input("??? ").strip()
        continue
    if len(a_input.split(" ")) > 1 and a_input.split(" ")[1] == "adds":
        d[a_input.split(" ")[0]] += d[a_input.split(" ")[-1]]
        a_input = raw_input("??? ").strip()
        continue
    if a_input.split(" ")[0] == "print":
        var = a_input.split(" ")[1]
        if var.isdigit():
            print var
        elif var in d:
            print var + " equals " + str(d[var])
        else:
            print var + " is undefined."
        a_input = raw_input("??? ").strip()
        continue
    else:
        print "Syntax error."
        a_input = raw_input("??? ").strip()
        continue
print "Goodbye."

















"""
print "hello"

input_list = "1 3 4 2 1 2 1 3; 4 4 2 4 3 2 4 4 3 1 3"
res = input_list.split(";")
print res

print list(res[0])

d = dict()
print d
print type(d)

for i in list(res[0]):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

res = [i for i in d.keys() if d[i] > 1 ]
print res
"""