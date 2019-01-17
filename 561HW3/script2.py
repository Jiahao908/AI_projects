grid_size = 3


iter_grid = []
iter_row = []
dir_row = []
dir_grid = []
cars = []
iter_grid_update = []
import copy

for x in range(0, grid_size):
    iter_row.append(-1)
    dir_row.append("STOP")

for y in range(0, grid_size):
    iter_grid.append(copy.deepcopy(iter_row))
    dir_grid.append(copy.deepcopy(dir_row))


iter_grid[0][0] = 99
iter_grid[0][1] = -101
iter_grid_update = copy.deepcopy(iter_grid)

r = 0.9

while(1):
    max_change = 0
    max_la = 0
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            if(iter_grid[i][j] != 99):
                if(i == 0 and j == 0):
                    choose_East = 0.7 * iter_grid[i+1][j] + 0.1 * iter_grid[i][j+1] + 2 * 0.1 * iter_grid[i][j]
                    choose_West = 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_North = 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.7 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j] + 2 * 0.1 * iter_grid[i][j]
                elif(i == 0 and j < grid_size - 1):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.7 * iter_grid[i+1][j]
                    choose_North = 0.7 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.7 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                elif(i < grid_size - 1 and j == 0):
                    choose_West = 0.1 * iter_grid[i][j] + 0.7 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_East = 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.7 * iter_grid[i+1][j]
                    choose_North = 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.7 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                elif(i == grid_size - 1 and j < grid_size - 1 and j != 0):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.7 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.7 * iter_grid[i][j]
                    choose_North = 0.7 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                    choose_South = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.7 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                elif(j == grid_size - 1 and i < grid_size - 1 and i != 0):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.7 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j] + 0.7 * iter_grid[i+1][j]
                    choose_North = 0.7 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                elif(i == grid_size - 1 and j == grid_size - 1):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.7 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j] + 0.7 * iter_grid[i][j]
                    choose_North = 0.7 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j]
                    choose_South = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i][j]
                elif(i == grid_size - 1 and j == 0):
                    choose_West = 0.1 * iter_grid[i][j] + 0.7 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                    choose_East = 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.7 * iter_grid[i][j]
                    choose_North = 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                    choose_South = 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.7 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                elif(i == 0 and j == grid_size - 1):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j] + 0.7 * iter_grid[i+1][j]
                    choose_North = 0.7 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.7 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                else:
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.7 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.7 * iter_grid[i+1][j]
                    choose_North = 0.7 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.7 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                """print("choose_East = ")
                print(choose_East)
                print('\n')
                print("choose_West = ")
                print(choose_West)
                print('\n')
                print("choose_South = ")
                print(choose_South)
                print('\n')
                print("choose_North = ")
                print(choose_North)
                print('\n')"""
                max_la = max(choose_East, choose_West, choose_North, choose_South)
                if(max_la == choose_West):
                    dir_grid[i][j] = "W"
                if(max_la == choose_East):
                    dir_grid[i][j] = "E"
                if(max_la == choose_South):
                    dir_grid[i][j] = "S"
                if(max_la == choose_North):
                    dir_grid[i][j] = "N"
                update = iter_grid[i][j] + r * max_la
                if(abs(update - iter_grid[i][j])> max_change):
                    max_change = abs(update - iter_grid[i][j])
                iter_grid_update[i][j] = update
    iter_grid = copy.deepcopy(iter_grid_update)
    if(max_change < (0.01/0.9)):
        print(iter_grid)
        break;
    else:
        print("Updated!")
        print('\n')
        print(iter_grid)
        print('\n')
        print(dir_grid)
        print('\n')
