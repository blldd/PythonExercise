# -*- coding:utf-8 -*-

"""

"""


class Solution:
    def gcd(self, num1, num2):
        # write code here
        if num1 == num2:
            return num1
        if num2 > num1:
            return self.gcd(num2, num1)
        else:
            if num1 & 1 == 0 and num2 & 1 == 0:
                return self.gcd(num1 >> 1, num2 >> 1) << 1
            elif num1 & 1 == 0 and num2 & 1 == 1:
                return self.gcd(num1 >> 1, num2)
            elif num1 & 1 == 1 and num2 & 1 == 0:
                return self.gcd(num1, num2 >> 1)
            else:
                return self.gcd(num2, num1 - num2)


if __name__ == '__main__':
    num1 = 100
    num2 = 200
    print(Solution().gcd(num1, num2))
