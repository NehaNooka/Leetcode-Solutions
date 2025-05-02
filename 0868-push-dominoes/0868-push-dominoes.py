class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom=list(dominoes)
        q=deque()
        for i,v in  enumerate(dom):
            if v!='.':
                q.append((i,v))
        while q:
            i,v=q.popleft()
            if v=='L':
                if i>0 and dom[i-1]=='.':
                    dom[i-1]='L'
                    q.append((i-1,'L'))
            else:
                if i+1<len(dom) and dom[i+1]=='.':
                    if i+2<len(dom) and dom[i+2]=='L':
                        q.popleft()
                    else:
                        dom[i+1]='R'
                        q.append((i+1,'R'))
        return ''.join(dom)

        