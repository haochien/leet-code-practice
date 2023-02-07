from typing import List
import collections

class NumberOfIslands:
    """
    LeetCode Question Nr.200
    https://leetcode.com/problems/number-of-islands/

    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.

    Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

    Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3

    """

    @staticmethod
    def great_ans1(grid: List[List[str]]) -> int:
        """
        technique: BFS (Breadth-First-Search)
        Time: O(n*m) 
        Memory: O(1)

        """

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1] ,[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and 
                        0 <= c < cols and
                        grid[r][c] == "1"):
                        grid[r][c] = "0"
                        q.append((r,c))
        

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    grid[r][c] == "0"
                    bfs(r,c)
        
        return islands


    @staticmethod
    def great_ans2(grid: List[List[str]]) -> int:
        """
        technique: DFS
        Time: O(n*m) 
        Memory: O(1)

        """

        def dfs(r, c):
            if (0 <= r < rows and 
                0 <= c < cols and
                grid[r][c] == "1"):

                grid[r][c] = "0"
                directions = [[1,0], [-1,0], [0,1] ,[0,-1]]
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        
        return islands





    @staticmethod
    def great_ans3(grid: List[List[str]]) -> int:
        """
        technique: BFS (Breadth-First-Search)
        Time: O(n*m) 
        Memory: O(n)
        Expination Sources:
        https://www.youtube.com/watch?v=pV2kpPD66nE


        Additional info for collections.deque:
        https://stackoverflow.com/questions/47493446/should-i-use-a-python-deque-or-list-as-a-stack
        Deques have O(1) speed for appendleft() and popleft() while lists have O(n) performance for insert(0, value) and pop(0).
        """

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1] ,[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and 
                        0 <= c < cols and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
        

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands



    @staticmethod
    def great_ans4(grid: List[List[str]]) -> int:
        """
        technique: DFS
        Time: O(n*m) 
        Memory: O(n)
        Expination Sources:
        https://www.youtube.com/watch?v=pV2kpPD66nE
        """

        def dfs(r, c):
            if (not 0 <= r < rows or 
                not 0 <= c < cols or
                grid[r][c] == "0" or
                (r, c) in visited):
                return

            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1] ,[0,-1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc)
                    
        

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        
        return islands

   