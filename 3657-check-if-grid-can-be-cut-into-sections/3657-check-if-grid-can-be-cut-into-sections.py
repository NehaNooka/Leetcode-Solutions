class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x=[(r[0],r[2]) for r in rectangles] #(x1,x2)
        y=[(r[1],r[3]) for r in rectangles] #(y1,y2)

        x.sort()
        y.sort()

        def helper_count(intervals):
            count=0
            prev_end=-1
            for start,end in intervals:
                if prev_end<=start:
                    count+=1
                prev_end=max(prev_end,end)
            return count
        

        return max(helper_count(x),helper_count(y)) >=3




        