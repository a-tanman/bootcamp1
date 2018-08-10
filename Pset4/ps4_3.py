class Tile:

    def __init__(self, x, y, thing):
        self.x = x
        self.y = y
        self.thing = thing

    def __str__(self):
        return str(self.thing)

    
    
class MsGrid:

    def __init__(self, rows, cols):
        self.grid = []

        for y in range(rows):
            self.grid = self.grid + [[]]
            for x in range(cols):
                self.grid[y] = self.grid[y] + [0]

    def set_tile(self, x, y, tile_type):
        self.grid[y][x] = Tile(x, y, tile_type)
    
    def __str__(self):
        return(str(self.grid))

def main():
    cols = 5
    rows = 5
    num_bombs = 3

    newgrid = MsGrid(5, 5)
    newgrid.set_tile(0,0,"B")
    print(newgrid)
    #print(grid)
    #grid[0][0] = Tile(0,0,"BOMB")
    #print(grid)

if __name__ == "__main__": main()