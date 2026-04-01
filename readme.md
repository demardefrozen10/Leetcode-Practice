# 416: Partition Sum

Note: basically check if the sum is divisible by 2, if not then there's no way you can partition it into TWO subsets, if so, then we use DP where dp[i] repersents whether or not we can make a sum of dp[i] with nums[i].
