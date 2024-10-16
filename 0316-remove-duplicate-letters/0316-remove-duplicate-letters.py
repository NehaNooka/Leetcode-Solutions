class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        pos={value:i for i,value in enumerate(s)}
        res=[]
        seen=set()

        for i,val in enumerate(s):
            if val not in seen:
                while res and val<res[-1] and i<pos[res[-1]]:
                    seen.discard(res.pop())
                seen.add(val)
                res.append(val)

        return ''.join(res)
        