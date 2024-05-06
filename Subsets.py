class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n_list = []
        res.append([])
        def helper(n):
            if n == len(nums): 
                return
            for i in range(n,len(nums)):
                n_list.append(nums[i])
                res.append(n_list.copy())
                print(n_list)
                helper(i+1)
                n_list.pop()
        helper(0)
        return res


        
