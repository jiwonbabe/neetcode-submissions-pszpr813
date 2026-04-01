class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasures.append((i,j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        q = deque(treasures)
        while q:
            (i,j) = q.popleft()
            for d in directions:
                ni, nj = i+d[0], j+d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 2147483647:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni,nj))
        
    
        
        

