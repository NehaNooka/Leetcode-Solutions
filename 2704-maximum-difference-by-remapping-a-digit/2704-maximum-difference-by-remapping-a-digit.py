class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        maxStr=s

        for c in s:
            if  c!='9':
                maxStr= s.replace(c,'9')
                break
        minStr=s
        for c in s:
            if c!='0':
                minStr= s.replace(c,'0')
                break

        return int(maxStr)-int(minStr)

        