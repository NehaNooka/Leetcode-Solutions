class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","")
        res= len(s) % k
        output = s[:res]
        for i in range(res,len(s),k):
            output+=('-'+s[i:i+k])
        
        return output.upper().lstrip("-")

        