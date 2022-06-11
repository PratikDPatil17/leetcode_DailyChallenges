class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        toremove = sum(nums) - x
        if toremove < 0:
            return -1
        
        longest_removal = -1
        left = 0
        
        for right in range(N):
            toremove -= nums[right]
            while toremove < 0:
                toremove += nums[left]
                left += 1
                
            if toremove == 0:
                longest_removal = max(longest_removal, right-left+1)
                
        return N - longest_removal if longest_removal != -1 else -1
            