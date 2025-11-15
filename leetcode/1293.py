from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # define directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # define helper function to check if a cell is valid
        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        queue = deque([(0, 0, 0, k)])
        visted = set((0,0))
        while queue:
            row, col, steps, remaining_k = queue.popleft()
            # check the end conditions
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return steps
            # iterate over the directions
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if is_valid(new_row, new_col) and not (new_row, new_col) in visted:
                    # add to not visited 
                    visted.add((new_row, new_col))
                    # now we check if the cell is a wall
                    if grid[new_row][new_col] == 1:
                        if remaining_k > 0:
                            queue.append((new_row, new_col, steps + 1, remaining_k - 1))
                    else:
                        queue.append((new_row, new_col, steps + 1, remaining_k))
        return -1
