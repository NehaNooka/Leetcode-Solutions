class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0
        for word in words:
            flag=True
            word=set(word)
            for c in word:
                if c not in allowed:
                    flag=False
                    break
            res= res+1 if flag==True else res
        return res        