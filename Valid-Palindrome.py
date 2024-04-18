class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""

        for i in s:
            if i.isalpha() or i.isnumeric():
                alpha += i.lower()
        print(alpha)
        return alpha == alpha[::-1]
