class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        ans = ""
        
        # stack will contain - stack[[char, count]]
        #stack = [[a,2],[b,3].......]
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1 
            else:
                stack.append([char, 1])
                
            if stack[-1][1] == k:
                stack.pop()
                
        
        # convert stack to string
        for char, count in stack:
            ans += (char*count)
        print (ans)    
        return ans