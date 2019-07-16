# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/16 8:49 PM
@Author  : ddlee
@File    : 523checkSubarraySum.py
"""


class Solution:
    # 超时
    def checkSubarraySum1(self, arr, target):
        l = len(arr)
        if l < 1:
            return False

        for i in range(l):
            for j in range(i + 2, l + 1):
                tmp = sum(arr[i:j])
                if target == tmp:
                    return True

                if target != 0 and tmp % target == 0:
                    return True

        return False

    #
    def checkSubarraySum(self, arr, target):
        l = len(arr)
        if l < 1:
            return False

        dp = [[0 for _ in range(l + 1)] for _ in range(l + 1)]
        for i in range(1, l + 1):
            for j in range(1, l + 1):
                pass

        return dp[-1][-1] == 1

Solution {
    public boolean checkSubarraySum(int[] nums, int k) { if(nums.length<=1){ return false; }else{ if(k==0){ int len=nums.length-1; int[][] dp=new int[len][len]; dp[0][0]=nums[0]+nums[1]; if(dp[0][0]==0){ return true; } for(int i=0;i<len;i++){ for(int j=0;j<=i;j++){ if(i!=j){ dp[i][j]=dp[i-1][j]+nums[i+1];
}else{ dp[i][j]=nums[i]+nums[i+1]; } if(dp[i][j]==0){ return true; } }
} return false; }else{ int len=nums.length-1; int[][] dp=new int[len][len]; dp[0][0]=nums[0]+nums[1]; if(dp[0][0]%k==0){ return true; } for(int i=0;i<len;i++){ for(int j=0;j<=i;j++){ if(i!=j){ dp[i][j]=dp[i-1][j]+nums[i+1];
}else{ dp[i][j]=nums[i]+nums[i+1]; } if(dp[i][j]%k==0){ return true; } }
} return false; } }
} }






if __name__ == '__main__':
    arr = [23, 2, 4, 6, 7]
target = 6
print(Solution().checkSubarraySum(arr, target))
