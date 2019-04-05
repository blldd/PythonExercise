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


def archer(n, nums):
    # todo

    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(i - 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
    for i in dp:
        print(i)
    return dp[-1][-1]
"""
#include <bits/stdc++.h>
using namespace std;
int a[1010];
int dp[1010][1010];
int dfs(int l, int r){

    if(dp[l][r] != -1)return dp[l][r];
    if(l == r)return dp[l][r] = 1;
    if(r - l == 1){
        return dp[l][r] = (a[l] == a[r] ? 1 : 2);
    }
    int ans = 10086;
    for(int k = l; k < r; k++){
        ans = min(ans, dfs(l, k) + dfs(k + 1, r));
    }
    if(a[l] == a[r])
        ans = min(ans, dfs(l + 1, r - 1));
    //printf("%d %d %d\n", l, r, ans);
    return dp[l][r] = ans;
}

int main(){
    memset(dp, -1, sizeof(dp));
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    printf("%d\n", dfs(0, n - 1));
}
"""


#
# if __name__ == '__main__':
#     print(archer(5, [1, 4, 3, 1, 5]))
