class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq=Counter(digits)
        res=[]
        for num in range(100,1000,2): #102%10
            parts=[num//100, (num//10)%10, num%10]
            count=Counter(parts)
            if all(freq[d]>=count[d] for d in count):
                res.append(num)
        return res
        