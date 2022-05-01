class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def bs(ip):
            stack = []
            for i in ip:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()
                    
            return "".join(stack)
        
        return bs(s) == bs(t)
                
        
        