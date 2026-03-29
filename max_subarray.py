class Solution(object):
    def maxSubArray(self, nums):
        
        total = 0 
        result = nums[0]

        for n in nums:

            if total < 0:
            
                total = 0 
            
            total += n 
            result = max (result , total)

        return result
        