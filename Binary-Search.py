class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r_x = len(nums) - 1
        l_x = 0

        while l_x <= r_x:
            mid = (r_x + l_x) // 2 
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l_x = mid + 1
            else:
                r_x = mid - 1
        return -1

        
