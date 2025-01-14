class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res=[0]*len(A)
        C=set()
        for i in range(len(A)):
            C.add(A[i])
            C.add(B[i])
            res[i]=2*(i+1) - len(C)
        return res