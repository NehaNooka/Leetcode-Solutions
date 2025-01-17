class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first=last=0
        for n in derived:
            if n==1:
                last=~last
        return first==last


        