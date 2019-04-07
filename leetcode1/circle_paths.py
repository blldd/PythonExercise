# -*- coding:UTF-8 -*-

# Read only region start
class UserMainCode(object):
    @classmethod
    def maxCircles(cls, input1, input2, input3):
        '''
        input1 : int
        input2 : int
        input3 : int

        Expected return type : int
        '''
        # Read only region end
        N = input1
        start = input2
        step= input3
        dp = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if (j + 1) % (i + 1) == 0:
                    dp[i][j] = 1
                    dp[j][i] = 1
                else:
                    continue
        res = 0
        cnt = 0
        idx = start - 1
        while cnt < step:
            next = set()
            for i in range(N):
                if dp[idx][i] == 1:
                    next.add(i)
            if start - 1 in next:
                res += 1
            idx = next.pop()
            cnt += 1
        return res

if __name__ == "__main__":
    print(UserMainCode().maxCircles(3, 2, 4))

