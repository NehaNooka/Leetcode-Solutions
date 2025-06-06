class Solution:
    def robotWithString(self, s: str) -> str:
        freq=Counter(s)
        st,res=[],[]

        def min_char():
            for i in range(26):
                ch=chr(ord('a')+i)
                if freq[ch]>0:
                    return ch
            return 'a'
        
        for ch in s:
            st.append(ch)
            freq[ch]-=1
            while st and st[-1]<=min_char():
                res.append(st.pop())
            
        while st:
            res.append(st.pop())

        return ''.join(res)
        