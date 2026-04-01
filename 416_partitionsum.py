class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        dp = [False] * (target + 1)

        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                if dp[j - nums[i]] == True:
                    dp[j] = True
        
        return dp[target]
