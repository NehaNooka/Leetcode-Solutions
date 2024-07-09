class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans=0
        temp=0
        for [x,y] in customers:
            if x> temp:
                temp=x+y
            else:
                temp+=y
            ans+=temp-x
        
        return ans/len(customers)
        