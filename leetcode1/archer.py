# -*- coding:UTF-8 -*-
import sys


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


def dfs(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if l == r:
        dp[l][r] = 1
        return dp[l][r]
    if r - l == 1:
        dp[l][r] = 1 if nums[l] == nums[r] else 2
        return dp[l][r]

    ans = sys.maxsize
    for k in range(l, r):
        ans = min(ans, dfs(l, k) + dfs(k + 1, r))
    if nums[l] == nums[r]:
        ans = min(ans, dfs(l + 1, r - 1))
    dp[l][r] = ans
    return dp[l][r]


if __name__ == '__main__':
    n = 5
    nums = [1, 4, 3, 1, 5]
    dp = [[-1 for j in range(n)] for i in range(n)]
    print(dfs(0, n - 1))
    for i in dp:
        print(i)
    # print(archer(n, nums))

"""
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
"""
