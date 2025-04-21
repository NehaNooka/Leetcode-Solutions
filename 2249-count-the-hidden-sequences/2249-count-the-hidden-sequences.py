class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur_sum,min_sum,max_sum=0,0,0
        for d in differences:
            cur_sum+=d
            min_sum=min(min_sum,cur_sum)
            max_sum=max(max_sum,cur_sum)
        
        return max(0, (upper-lower)- (max_sum-min_sum)+1)
        