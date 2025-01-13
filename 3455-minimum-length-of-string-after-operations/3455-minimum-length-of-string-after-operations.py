class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
        count=Counter(s)
        if n<3 or max(count.values())<3: return n
        for v in count.values():
            while v>=3:
                v-=2
                n-=2
        return n
        