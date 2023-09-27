#!/usr/bin/python3
"""script that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """
        function iterates over the cells of the grid and checks each
        land cell's adjacent cells. If a land cell is adjacent to water
        or is at the edge of the grid, it contributes to the perimeter.
        The total perimeter is then calculated and returned.
    """
    if not grid:
        return 0

    rows = len(grid);
    # calculates the length of the first row in the grid.
    # Since each row has the same number of columns
    columns = len(grid[0]);

    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                # check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # check right
                if j == columns - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

                # check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter
