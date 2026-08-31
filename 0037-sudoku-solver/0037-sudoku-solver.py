class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # 1. State Initialization: Map the board once.
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)
                    
        # 2. Backtracking via pointer advancement, not full board rescanning.
        def solve(idx):
            # If we've filled all empty cells, the board is solved.
            if idx == len(empty_cells):
                return True
                
            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + c // 3
            
            for n in "123456789":
                # O(1) state validation using hash sets
                if n not in rows[r] and n not in cols[c] and n not in boxes[box_idx]:
                    # Forward Phase: Apply the state
                    board[r][c] = n
                    rows[r].add(n)
                    cols[c].add(n)
                    boxes[box_idx].add(n)
                    
                    if solve(idx + 1):
                        return True
                        
                    # Backtrack Phase: Revert the state
                    board[r][c] = "."
                    rows[r].remove(n)
                    cols[c].remove(n)
                    boxes[box_idx].remove(n)
                    
            return False
            
        solve(0)