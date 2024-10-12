class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start,end=[],[]

        for i,j in intervals:
            start.append(i)
            end.append(j)
        
        start.sort()
        end.sort()

        i,j=0,0
        res,groups=0,0
        while i < len(intervals):
            if start[i]<= end[j]:
                groups+=1
                i+=1
            else:
                groups-=1
                j+=1
            res=max(res,groups)
        return res

