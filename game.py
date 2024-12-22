class Grid:
    def __init__(self):
        self.grid = [[0]*6 for _ in range(6)]

    def alive(self, x, y):
        self.grid[x][y] = 1

    def dead(self, x, y):
        self.grid[x][y] = 0

    def show(self):
        for row in self.grid:
            print(" ".join(map(str, row)))  # Efficient row display
        print()

    def neighbours(self, x, y):
        count = 0
        for nx, ny in [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1), (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]:
            # Check boundaries to avoid out-of-bounds errors
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]):
                count += self.grid[nx][ny]  # Accumulate directly
        return count


if __name__ == "__main__":
    grid = Grid()
    num_cells = int(input("How many living cells? "))
    for cell in range(num_cells):
        x = int(input(f"Enter x coordinate for cell {cell}: "))
        y = int(input(f"Enter y coordinate for cell {cell}: "))
        grid.alive(x, y)

    round = 0
    while True:
        print(f"Round {round}")
        grid.show()

        # Use enumerate to iterate over rows and columns
        for x, row in enumerate(grid.grid):
            for y, cell in enumerate(row):
                count = grid.neighbours(x, y)
                if cell == 1:  # If the cell is alive
                    if count < 2 or count > 3:  # Underpopulation or overpopulation
                        grid.dead(x, y) # Mark as dead
                else:  # If the cell is dead
                    if count == 3:  # Reproduction
                        grid.alive(x, y)  # Mark as alive
        match input("Enter to continue or q to exit\n"):
            case "q":
                break
            case _:
                pass
        round += 1
