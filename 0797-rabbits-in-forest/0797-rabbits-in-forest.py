class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count={}
        total=0
        for ans in answers:
            if ans==0: total+=1
            elif ans in count and count[ans]>0: count[ans]-=1
            else:
                total+=ans+1
                count[ans]=ans
        return total