class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([c for c in reversed(s.split())])
        