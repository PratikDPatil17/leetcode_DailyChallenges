class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        
        N = len(nums)
        
        l,r = N,0
        
        for i,n in enumerate(nums):
            if nums[i] != nums2[i]:
                l = min(l,i)
                r = max(r,i)
                
        if l == N: return 0
        return r-l+1
    
        