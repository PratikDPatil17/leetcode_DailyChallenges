class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''
        n = len(envelopes)
        if n <= 1:
            return n
        
        # asend with width and desend with height
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        # find the longest increasing subsequence
        size = 0
        tails = [0]*n
        
        for _, h in envelopes:
            l, r = 0, size-1
            while l <= r:
                mid = (l+r) // 2
                if tails[mid] >= h:
                    r = mid - 1
                else:
                    l = mid + 1
            
            tails[l] = h
            size = max(size, l+1)
        
        return size