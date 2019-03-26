import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# userInput = input("please write a phone number:")
# print(isPhoneNumber(userInput))

phoneNumRegex = re.compile(r'\d\d\d\d\d')
# userInput = input("please input a phone number, and it will check true or false.")
# mo = phoneNumRegex.match(userInput)
# # mo = phoneNumRegex.findall(userInput)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)-(\d\d+)-(\d\d\d)-(\d\d\d-\d\d\d\d)-(\d\d)')
mo = phoneNumRegex.search('415-555-4242-12-415-555-4242-12.')
phoneNum = "021-38282810"
# print("mo.group(1):")
# print(mo.group(1))
# print("mo.group(2):")
# print(mo.group(2))
# print("mo.group(0):")
# print(mo.group(0))
# print("mo.group():")
# print(mo.group())
# print("mo.groups():")
# print(mo.groups())
# g1, g2, g3,g4,g5,g6 = mo.groups()
# print("g1:")
# print(g1)
# print("g2:")
# print(g2)
#
#
import re
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey asdlfasdjflak;s.')
# print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
# print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')   #Batman Batmobile Batcopter Batbat
mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))
# batRegex = re.compile(r'Bat(wo)?man')   #Batman   Batwoman
# mo1 = batRegex.search('The Adventures of Batwoman')  #
# print(mo1.group())
batRegex = re.compile(r'Bat(wo)*man')   #Batman   Batwoman  Batwowoman   Batwowowowowowowowoman
mo1 = batRegex.search('The Adventures of Batwowowowowowowowowoman')  #
# print(mo1.group())

batRegex = re.compile(r'Bat(wo)+man')   #Batwoman  Batwowoman   Batwowowowowowowowoman
mo1 = batRegex.search('The Adventures of Batwoman')  #
# print(mo1.group())

batRegex = re.compile(r'Bat(wo){2,}man')   #Batwoman  Batwowoman   Batwowowowowowowowoman
mo1 = batRegex.search('The Adventures of Batwowowoman')  #
# print(mo1.group())

xmasRegex = re.compile(r'\d+\s\w{9}')
a = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(a)

vowelRegex = re.compile(r'[aeiouAEIOU]')
a = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(a)

vowelRegex = re.compile(r'[^aeiouAEIOU]')
a = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(a)

beginsWithHello = re.compile(r'^Hello')
a = beginsWithHello.search('Hello world!')
# print(a)

atRegex = re.compile(r'.at')
a = atRegex.findall('The ,at cat in the hat sat on the flat mat.')
print(a)

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')


"""
800-420-7240
415-863-9900
415-863-9950

021-186-2181-7985
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
"""


