class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for c in s:
            if c=="B" or c=="D":
                if stack and  c=="B" and stack[-1]=="A":
                    stack.pop()
                elif stack and  c=="D" and stack[-1]=="C":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)   
        return len(stack)

        