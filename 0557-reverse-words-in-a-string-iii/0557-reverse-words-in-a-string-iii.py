class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        for c in range(len(s)):
            s[c] = s[c][::-1]
        return ' '.join(s)
        