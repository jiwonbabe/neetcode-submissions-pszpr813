import math 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row, col, subbox = [set() for _ in range(n)], [set() for _ in range(n)], [set() for _ in range(n)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                cell = int(board[i][j])
                if cell in row[i]:
                    return False
                row[i].add(cell)
                if cell in col[j]:
                    return False
                col[j].add(cell)
                box_index = (i // 3) * 3 + j // 3
                if cell in subbox[box_index]:
                    return False
                subbox[box_index].add(cell)
        
        return True