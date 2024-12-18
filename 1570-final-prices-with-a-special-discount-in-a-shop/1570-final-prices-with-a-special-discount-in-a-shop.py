class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        idxStack=[]
        res=prices[:]
        for i,v in enumerate(prices):
            while idxStack and prices[idxStack[-1]]>=v:
                res[idxStack.pop()]-=v
            idxStack.append(i)
        return res

        '''
        #Brute Force Approach
        res=[]
        for i in range(len(prices)):
            flag=False
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    res.append(prices[i]-prices[j])
                    flag=True
                    break
            if flag==False:
                res.append(prices[i])
        return res
        '''

        