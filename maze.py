class Maze:
    def __init__(self, m: int, n: int) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.row = m
        self.col = n
        self.grid_representation = [[0 for _ in range(n)] for _ in range(m)]
    
    def add_ghost(self, x: int, y: int) -> None:
        # Add a ghost at the given coordinates
        self.grid_representation[x][y] = 1
    
    def remove_ghost(self, x: int, y: int) -> None:
        # Remove a ghost from the given coordinates
        self.grid_representation[x][y] = 0
    
    def is_ghost(self, x: int, y: int) -> bool:
        # Check if there's a ghost at the given coordinates
        return self.grid_representation[x][y] == 1
       
    def print_grid(self) -> None:
        # Print the grid representation of the maze
        for i in range(self.row):
            for j in range(self.col):
                print(self.grid_representation[i][j], end=" ")
            print()
