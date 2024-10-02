class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_set=sorted(set(arr))
        arr_count={ele:rank+1 for rank,ele in enumerate(arr_set)}
        res=[arr_count[ele] for ele in arr]
        return res


            
            

        