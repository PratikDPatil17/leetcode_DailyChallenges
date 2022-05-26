class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        count = 0
        for i in s:
            print(i)
            if i == "1":
                count+=1
        return count