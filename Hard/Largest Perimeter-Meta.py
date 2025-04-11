def largest_island_perimeter(grid):
    
    if isinstance(grid, dict) and "grid" in grid:
        grid = grid["grid"]
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def neighbors(r, c):
        """Yield valid 4-directional neighbors of (r, c)."""
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc
    
    def dfs(r, c):
        """Perform a DFS from (r, c) to find island cells and compute the perimeter."""
        stack = [(r, c)]
        visited[r][c] = True
        island_cells = []
        
        while stack:
            cr, cc = stack.pop()
            island_cells.append((cr, cc))
            for nr, nc in neighbors(cr, cc):
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    
        # Calculate perimeter for this island
        perimeter = 0
        for (ir, ic) in island_cells:
            for nr, nc in neighbors(ir, ic):
                if grid[nr][nc] == 0:  # adjacent to water
                    perimeter += 1

            # Edges along the boundary of the grid
            if ir == 0:
                perimeter += 1
            if ir == rows - 1:
                perimeter += 1
            if ic == 0:
                perimeter += 1
            if ic == cols - 1:
                perimeter += 1

        return perimeter
    
    max_perimeter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                island_perimeter = dfs(r, c)
                max_perimeter = max(max_perimeter, island_perimeter)
    
    return max_perimeter