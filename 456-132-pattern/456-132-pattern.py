class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        
        currMin = nums[0]
        
        for curr in nums:
            while stack and stack[-1][0] <= curr:
                stack.pop()
                
            if stack and curr < stack[-1][0] and stack[-1][1] < curr:
                return True
            
            stack.append([curr,currMin])
            currMin = min(currMin, curr)
            
        return False