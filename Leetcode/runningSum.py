# Leetcode 1480: Running sum of 1D Array

from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
s = Solution()
s.runningSum([1,2,3,4])
