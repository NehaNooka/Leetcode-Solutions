class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks)<k: return 0

        l=0
        res=float('inf')
        op=0
        for r in range(len(blocks)):
            if blocks[r]=='W': op+=1
            while (r-l+1)==k:
                res=min(res,op)
                if blocks[l]=='W':
                    op-=1
                l+=1
        return res

        