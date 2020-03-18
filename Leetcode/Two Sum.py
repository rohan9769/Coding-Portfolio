
class Solution:
    def twoSum(self,nums,target):
        compliments = {}
        result = []
        for index,nums in enumerate(nums):
            if compliments.get(nums) is None:
                compliments[target-nums] = index
            else:
                result=[compliments[nums],index]
        return result

s = Solution()
print(s.twoSum([2,3,4,5,6],11))