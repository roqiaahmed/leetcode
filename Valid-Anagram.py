class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s = {}
        l_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            l_s[s[i]] = l_s.get(s[i],0)+1
            l_t[t[i]] = l_t.get(t[i],0)+1
        
        return l_s == l_t
