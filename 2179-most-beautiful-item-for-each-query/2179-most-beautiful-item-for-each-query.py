class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key= lambda x:x[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        cur_max=0
        ans=[0]*len(queries)
        i=0
        for idx, q in sorted_queries:
            while i<len(items) and items[i][0]<=q:
                cur_max=max(cur_max,items[i][1])
                i+=1
            ans[idx]=cur_max
        return ans
        