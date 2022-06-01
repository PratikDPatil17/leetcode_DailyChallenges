class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumt = []
        sumt.append(nums[0])
        for i in range(1, len(nums)):
            x = sumt[-1] + nums[i]
            
            sumt.append(x)
            
        return sumt

        