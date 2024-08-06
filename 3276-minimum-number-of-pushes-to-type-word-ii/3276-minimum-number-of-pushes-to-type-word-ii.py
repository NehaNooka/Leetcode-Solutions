class Solution:
    def minimumPushes(self, word: str) -> int:
        counts=[0]*26
        for c in word:
            counts[ord(c)-ord('a')]+=1
        counts.sort(reverse=True)

        res=0
        for i,cnt in enumerate(counts):
            if cnt>0:
                res+= cnt * (1+i//8)
                i+=1
            else:
                break
        return res
        