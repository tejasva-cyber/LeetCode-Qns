class Solution(object):
    def totalNQueens(self, n):
        # Bind the counter to the class instance to bypass Python 2 closure limitations
        self.count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Forward phase: place the queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # Backtrack phase: remove the queen
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return self.count