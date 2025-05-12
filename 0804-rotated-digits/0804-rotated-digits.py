class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotMap={'0':'0', 
        '1':'1', 
        '2':'5',
        '5':'2', 
        '6':'9', 
        '8':'8', 
        '9':'6'}
        res=0
        def rotDig(st):
            res=''
            for c in st:
                if c not in rotMap: return None
                res += rotMap[c]
            return int(res)

        for i in range(1,n+1):
            if rotDig(str(i)) is not None and  i != rotDig(str(i)):
                res+=1
        return res

        