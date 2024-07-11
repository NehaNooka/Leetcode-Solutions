class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        

        for c in s:
            if c ==")":
                temp=[]
                while stack[-1]!="(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            
            else:
                stack.append(c)
        
        return ''.join(stack)
        

        