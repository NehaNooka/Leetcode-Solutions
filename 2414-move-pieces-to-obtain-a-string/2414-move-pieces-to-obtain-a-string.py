class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start)!=len(target) or start.count('L')!=target.count('L') or start.count('R')!=target.count('R'): return False
        s,t=0,0
        start+='!'
        target+='!'
        while s<len(start) and t<len(target):
            while s<len(start) and start[s]=='_': s+=1
            while t<len(target) and target[t]=='_':t+=1
            c=start[s]
            if c!=target[t] or (c=='L' and s<t) or (c=='R' and s>t): return False
            s+=1
            t+=1
        return True
            


        