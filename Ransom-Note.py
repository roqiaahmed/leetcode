class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dice = {}

        for i in magazine:
            dice[i] = dice.get(i,0) + 1
        
        for i in ransomNote:
            if i in dice and dice[i] > 0:
                dice[i] -= 1
            else:
                return False
        
        return True
            
        
