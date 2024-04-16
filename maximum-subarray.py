class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_num = nums[0]
        max_num = curr_num
        for i in range(len(nums) - 1):
            if curr_num < nums[i+1] and curr_num < 0:
                curr_num = nums[i+1]
            else:
                curr_num += nums[i+1]
            max_num = max(curr_num, max_num)
        return max_num
        
