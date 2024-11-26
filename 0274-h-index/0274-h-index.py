class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        paper_count=[0]*(n+1)

        for c in citations:
            paper_count[(min(n,c))]+=1
        
        h=n
        paper=paper_count[h]

        while paper<h:
            h-=1
            paper+=paper_count[h]
        
        return h

