class Solution:
    def minSwaps(self, s: str) -> int:
        close,max_close=0,0

        for c in s:
            if c=="[":
                close-=1
            else:
                close+=1
            max_close=max(max_close,close)
        
        return (max_close+1)//2




        