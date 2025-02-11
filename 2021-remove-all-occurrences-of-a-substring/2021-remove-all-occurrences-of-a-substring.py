class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        partL=len(part)
        for c in s:
            stack.append(c)
            if len(stack)>=partL and ''.join(stack[-partL:])==part:
                del(stack[-partL:])
        return ''.join(stack)
        