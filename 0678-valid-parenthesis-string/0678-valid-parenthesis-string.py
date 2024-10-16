class Solution:
    def checkValidString(self, s: str) -> bool:
        leftCheck=rightCheck=0
        for c in s:
            if c=="(" or c=="*":
                leftCheck+=1
            else:
                leftCheck-=1
            if leftCheck <0:
                return False
            
        for c in reversed(s):
            if c==")" or c=="*":
                rightCheck+=1
            else:
                rightCheck-=1
            if rightCheck <0:
                return False
                
        return True