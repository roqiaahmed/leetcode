class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_s = set()
        j = 0
        max_num = 0

        for i in range(len(s)):

            while s[i] in l_s:
                l_s.remove(s[j])
                j +=1

            l_s.add(s[i])

            max_num = max(len(l_s), max_num)

        return max_num
