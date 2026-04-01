from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                (x, y) = q.popleft()
                grid[x][y] = -1
                if x-1 >=0 and grid[x-1][y] == '1':
                    q.append((x-1, y))
                if x+1 < len(grid) and grid[x+1][y] == '1':
                    q.append((x+1, y))
                if y-1 >= 0 and grid[x][y-1] == '1':
                    q.append((x, y-1))
                if y+1 < len(grid[0]) and grid[x][y+1] == '1':
                    q.append((x, y+1))
                
                
            
        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    num_of_islands += 1
        
        return num_of_islands
