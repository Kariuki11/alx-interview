### Island Perimeter Problem

The **Island Perimeter** problem is a common algorithmic challenge, particularly in coding interviews. Given a 2D grid representing a map where:
- `0` represents water, and
- `1` represents land,

you need to compute the perimeter of the "island." The island is a group of connected `1`s (land cells) where there are no lakes (i.e., water surrounded by land). The perimeter is calculated as the total length of the boundary edges around the island.

### Problem Breakdown:
1. A land cell (`1`) contributes 4 sides to the perimeter.
2. If a land cell has an adjacent land cell (up, down, left, or right), the shared side between them reduces the perimeter by 1 for each adjacency.

### Approach:
- Traverse the grid, and for each land cell (`1`):
  1. Add 4 to the perimeter for the cell.
  2. Check for adjacent land cells in four directions (up, down, left, right). For each adjacent land cell, subtract 1 from the perimeter (because the sides are shared).

### Example:
```python
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
```

The perimeter of the island in this grid is `16`.

### Python Code Solution:

```python
def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # If the current cell is land
                perimeter += 4  # Add 4 sides for the current cell
                
                # Check all 4 directions
                if r > 0 and grid[r-1][c] == 1:  # Up
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:  # Down
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:  # Left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c+1] == 1:  # Right
                    perimeter -= 1
    return perimeter
```

### Example Usage:
```python
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output: 16
```

### Time Complexity:
- **O(m * n)** where `m` is the number of rows and `n` is the number of columns in the grid. You visit every cell exactly once and check its neighbors in constant time.

---

### Potential Interview Questions:

1. **Basic Understanding**:
   - Can you explain the problem in your own words?
   - How would you approach calculating the perimeter for a given grid?

2. **Optimization**:
   - Can you improve the solution to avoid checking cells multiple times?
   - What is the time complexity of your solution?

3. **Edge Cases**:
   - What happens if there is no land at all in the grid?
   - How does your solution handle a grid with multiple islands (though the problem might assume there’s only one island)?

4. **Variations**:
   - How would you handle the case if there are lakes (water completely surrounded by land)?
   - What if the grid is infinite, with water extending indefinitely beyond the edges?

5. **Follow-up questions**:
   - How would you calculate the perimeter if the island can wrap around the grid edges (toroidal grid)?
   - How would you modify the solution to return the perimeter of the largest island if there are multiple islands?

---

This problem is typically used to test knowledge of grid traversal, boundary conditions, and managing shared edges between elements in a grid.
