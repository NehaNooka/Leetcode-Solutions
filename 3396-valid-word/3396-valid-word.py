class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False

        vowels=set('aeiou')
        v,co=0,0
        for c in word:
            if c.isalpha():
                if c.lower() in vowels: v+=1
                else: co+=1
            elif not c.isdigit(): return False
        return v>=1 and co>=1

        