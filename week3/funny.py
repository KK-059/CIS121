import random
import time
import os

class Maze:
    def init(self, width, height):
        self.width = width
        self.height = height
        self.maze = [['#' for  in range(width)] for  in range(height)]
        self.visited = [[False for  in range(width)] for  in range(height)]
        self.start = (1, 1)
        self.end = (height - 2, width - 2)

    def generate(self, x=1, y=1):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        self.visited[y][x] = True
        self.maze[y][x] = ' '

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and not self.visited[ny][nx]:
                self.maze[y + dy // 2][x + dx // 2] = ' '
                self.generate(nx, ny)

    def display(self, path=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if path and (y, x) in path:
                    print('.', end='')
                else:
                    print(self.maze[y][x], end='')
            print()
        time.sleep(0.05)

    def solve(self):
        path = []
        visited = set()

        def dfs(y, x):
            if (y, x) == self.end:
                return True
            visited.add((y, x))
            path.append((y, x))
            self.display(path)

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    if self.maze[ny][nx] == ' ' and (ny, nx) not in visited:
                        if dfs(ny, nx):
                            return True
            path.pop()
            return False

        dfs(*self.start)
        self.display(path)
        return path


#Main program
if name == "main":
    width, height = 21, 15  # Must be odd numbers
    maze = Maze(width, height)
    maze.generate()
    maze.maze[maze.end[0]][maze.end[1]] = ' '
    maze.display()
    print("\nSolving the maze...\n")
    time.sleep(1)
    maze.solve()
    print("\nMaze solved!")