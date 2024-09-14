class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ele = max(nums) # find the maximum element

        res = 0 # intialize the result variablbe

        temp = 0 # a temporary variable for counting the maxlength subarray

        for i in nums:
            if i == max_ele:
                temp+=1
            else:
                temp = 0
            res = max(res,temp)
        return res # returning the result