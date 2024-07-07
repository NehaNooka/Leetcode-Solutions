class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        rem=0
        while (numBottles+rem) >= numExchange:
            newBottles=(numBottles+ rem)//numExchange 
            rem=(numBottles+ rem)%numExchange 
            res+=newBottles 
            numBottles=newBottles       
        return res






        