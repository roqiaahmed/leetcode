class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def rec(num):
            if len(comb) == k:
                res.append(comb.copy())
                # print(res)
                return
            for i in range(num, n + 1):
                comb.append(i)
                rec(i + 1)
                comb.pop()   
        rec(1)
        return res
