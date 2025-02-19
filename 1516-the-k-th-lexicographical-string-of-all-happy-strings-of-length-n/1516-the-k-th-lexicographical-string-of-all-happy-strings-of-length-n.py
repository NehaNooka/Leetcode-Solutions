class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total=3*(2**(n-1))
        res=[]
        choices="abc"
        left,right=1,total

        for i in range(n):
            cur=left
            part_size= (right-left+1)//len(choices)

            for c in choices:
                if k in range(cur,cur+part_size):
                    res.append(c)
                    left,right=cur,cur+part_size
                    choices='abc'.replace(c,'')
                    break
                cur+=part_size
        return ''.join(res)
        