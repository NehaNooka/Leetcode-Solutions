class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        m={}
        for n in nums:
            i=str(n)
            temp=""
            for s in i:
                temp+=str(mapping[int(s)])
            m[n]=int(temp)
        nums.sort(key=lambda n: (m[n],nums))
        return nums



        