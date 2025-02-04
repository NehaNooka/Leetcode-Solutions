class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipLeft,skipRight=s[l+1:r+1],s[l:r]
                return (skipLeft==skipLeft[::-1] or skipRight==skipRight[::-1])
            l+=1
            r-=1
        return True


        