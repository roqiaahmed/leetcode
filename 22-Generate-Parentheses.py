class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        w_praket = []
        def wellParentheses(left,right):
            if left == n and right == n:
                res.append("".join(w_praket))
                return

            if left < n:
                w_praket.append("(")
                wellParentheses(left+1,right)
                w_praket.pop()

            if right < left:
                w_praket.append(")")
                wellParentheses(left,right+1)
                # w_praket.pop()
        
        wellParentheses(0,0)
        return res
