class Solution:
    def countVowelStrings(self, n: int) -> int:
        def backtrack(n, vowelCnt):
            if n == 0:
                return 1
            
            res = 0
            
            for currVowel in range(vowelCnt, 5):
                res += backtrack(n-1, currVowel)
                    
            return res
        
        return backtrack(n, 0)
        
        