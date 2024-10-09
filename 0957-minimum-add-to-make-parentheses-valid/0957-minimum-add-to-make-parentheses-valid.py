class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count,stack=0,[]
        for c in s:
            if c=="(":
                stack.append(c)
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)