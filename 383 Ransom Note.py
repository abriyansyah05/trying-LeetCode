from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ab_ransom = Counter (ransomNote)
        ab_maga = Counter (magazine)
        
        for i in ab_ransom:
            if ab_ransom[i] > ab_maga[i]:
                return False
        return True