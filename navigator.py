from maze import *
from exception import *
from stack import *

class PacMan:
    def __init__(self, grid: Maze) -> None:
        self.grid = grid
        self.navigator_maze = grid.grid_representation

    def find_path(self, start, end):

        if self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1:
            raise PathNotFoundException

        r = self.grid.row
        c = self.grid.col

        visited = [[False] * c for _ in range(r)]


        st = Stack()
        st.push((start, [start])) 
        visited[start[0]][start[1]] = True

        while not st.is_Empty():
            current_position, path = st.pop()
            x, y = current_position

            if current_position == end:
                return path

            if r>x-1>=0 and not visited[x-1][y] and self.navigator_maze[x-1][y] == 0:
                st.push(((x-1, y),path + [(x-1, y)]))
                visited[x-1][y] = True
            if c>y-1>=0 and not visited[x][y-1] and self.navigator_maze[x][y-1] == 0:
                st.push(((x, y-1),path + [(x, y-1)]))
                visited[x][y-1] = True
            if 0<=x+1<r and not visited[x+1][y] and self.navigator_maze[x+1][y] == 0:
                st.push(((x+1, y),path + [(x+1, y)]))
                visited[x+1][y] = True
            if 0<=y+1<c and not visited[x][y+1] and self.navigator_maze[x][y+1] == 0:
                st.push(((x, y+1),path + [(x, y+1)]))
                visited[x][y+1] = True

        raise PathNotFoundException
