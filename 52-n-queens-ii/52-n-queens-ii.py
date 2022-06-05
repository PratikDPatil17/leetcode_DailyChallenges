class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        def helper(row = 0, diag1 = set(), diag2 = set(), column = set()):
            if row == n:
                self.count += 1
            for col in range(n):
                if row - col not in diag1 and row + col not in diag2 and col not in column:
                    helper(row + 1, diag1.union({row - col}), diag2.union({row + col}), column.union({col}))
        helper()
        return self.count