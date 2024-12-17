class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count=Counter(s)
        maxHeap=[(-ord(c),cnt) for c,cnt in count.items()]
        heapq.heapify(maxHeap)
        res=[]
        while maxHeap:
            char,cnt=heapq.heappop(maxHeap)
            char1=chr(-char)
            cur_cnt=min(cnt,repeatLimit)
            res.append(char1*cur_cnt)

            if cnt-cur_cnt>0 and maxHeap:
                nxtchar,nxtcnt=heapq.heappop(maxHeap)
                nxtchar1=chr(-nxtchar) 
                res.append(nxtchar1) 
                if nxtcnt>1:
                    heapq.heappush(maxHeap,(nxtchar,nxtcnt-1)) 
                heapq.heappush(maxHeap,(char,cnt-cur_cnt))                   

        return ''.join(res)


