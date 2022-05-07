class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # stack will contain = [top,minLeft]
        stack = []
        
        currMin = nums[0]
        
        # try to compare minLeftToStack < curr < stackTop 
        for curr in nums[1:]:
            #make sure your stack is strictly increasing from bottom so pop other and keep highest valur at top.
            while stack and stack[-1][0] <= curr:
                stack.pop()
                
            if stack and curr < stack[-1][0] and stack[-1][1] < curr:
                return True
            
            stack.append([curr,currMin])
            currMin = min(currMin, curr)
            
        return False