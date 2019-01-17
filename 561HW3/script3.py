grid_size_row = 4
grid_size_colm = 3


iter_grid = []
iter_row = []
dir_row = []
dir_grid = []
cars = []
iter_grid_update = []
import copy

for x in range(0, grid_size_colm):
    iter_row.append(-0.04)
    dir_row.append("STOP")

for y in range(0, grid_size_row):
    iter_grid.append(copy.deepcopy(iter_row))
    dir_grid.append(copy.deepcopy(dir_row))



iter_grid[3][0] = 1
iter_grid[3][1] = -1
iter_grid[1][1] = -2

iter_grid_update = copy.deepcopy(iter_grid)



r = 1

while(1):
    max_change = 0
    max_la = 0
    for i in range(0, 4):
        for j in range(0, 3):
            if(iter_grid[i][j] != 1 and iter_grid[i][j] != -1 and iter_grid[i][j] != -2):
                if(i == 0 and j == 0):
                    choose_East = 0.8 * iter_grid[i+1][j] + 0.1 * iter_grid[i][j+1] +  0.1 * iter_grid[i][j]
                    choose_West = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1]
                    choose_North = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j] +  0.1 * iter_grid[i+1][j]
                    choose_South = 0.8 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j] +  0.1 * iter_grid[i][j]
                elif(i == 0 and j == 1):
                    choose_East = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j-1]
                    choose_West = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j-1]
                    choose_North = 0.8 * iter_grid[i][j-1] + 0.2 * iter_grid[i][j]
                    choose_South = 0.8 * iter_grid[i][j+1] + 0.2 * iter_grid[i][j]
                elif(i == 1 and j == 0):
                    choose_East = 0.8 * iter_grid[i+1][j] + 0.2 * iter_grid[i][j]
                    choose_West = 0.8 * iter_grid[i-1][j] + 0.2 * iter_grid[i][j]
                    choose_North = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i+1][j]
                elif(i == 1 and j == 2):
                    choose_East = 0.8 * iter_grid[i+1][j] + 0.2 * iter_grid[i][j]
                    choose_West = 0.8 * iter_grid[i-1][j] + 0.2 * iter_grid[i][j]
                    choose_North = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i+1][j]
                elif(i == 2 and j == 1):
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j+1] + 0.8 * iter_grid[i+1][j]
                    choose_West = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j-1]
                    choose_North = 0.8 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.8 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                elif(i == 0 and j < grid_size_colm - 1):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j+1] + 0.8 * iter_grid[i+1][j]
                    choose_North = 0.8 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i][j] + 0.8 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                elif(i < grid_size_row - 1 and j == 0):
                    choose_West = 0.1 * iter_grid[i][j] + 0.8 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1]
                    choose_East = 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i][j+1] + 0.8 * iter_grid[i+1][j]
                    choose_North = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j]  + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i-1][j] + 0.8 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                elif(i == grid_size_row - 1 and j < grid_size_colm - 1 and j != 0):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.8 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j+1] + 0.8 * iter_grid[i][j]
                    choose_North = 0.8 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j]
                    choose_South = 0.1 * iter_grid[i-1][j] + 0.8 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                elif(j == grid_size_colm - 1 and i < grid_size_row - 1 and i != 0):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.8 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.8 * iter_grid[i+1][j]
                    choose_North = 0.9 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i-1][j] + 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                elif(i == grid_size_row - 1 and j == grid_size_colm - 1):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.8 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.8 * iter_grid[i][j]
                    choose_North = 0.8 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j]  + 0.1 * iter_grid[i][j]
                    choose_South = 0.1 * iter_grid[i-1][j] + 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j]
                elif(i == grid_size_row - 1 and j == 0):
                    choose_West = 0.1 * iter_grid[i][j] + 0.8 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1]
                    choose_East = 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1] + 0.8 * iter_grid[i][j]
                    choose_North = 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j]
                    choose_South = 0.1 * iter_grid[i-1][j] + 0.8 * iter_grid[i][j+1] + 0.1 * iter_grid[i][j]
                elif(i == 0 and j == grid_size_colm - 1):
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i][j]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.8 * iter_grid[i+1][j]
                    choose_North = 0.8 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                    choose_South =  0.1 * iter_grid[i][j] + 0.8 * iter_grid[i][j] + 0.1 * iter_grid[i+1][j]
                else:
                    choose_West = 0.1 * iter_grid[i][j-1] + 0.8 * iter_grid[i-1][j] + 0.1 * iter_grid[i][j+1]
                    choose_East = 0.1 * iter_grid[i][j-1] + 0.1 * iter_grid[i][j+1] + 0.8 * iter_grid[i+1][j]
                    choose_North = 0.8 * iter_grid[i][j-1] + 0.1 * iter_grid[i-1][j] + 0.1 * iter_grid[i+1][j]
                    choose_South = 0.1 * iter_grid[i-1][j] + 0.8 * iter_grid[i][j+1] + 0.1 * iter_grid[i+1][j]
                print("choose_East = ")
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
                print('\n')
                max_la = max(choose_East, choose_West, choose_North, choose_South)
                if(max_la == choose_West):
                    dir_grid[i][j] = "W"
                if(max_la == choose_East):
                    dir_grid[i][j] = "E"
                if(max_la == choose_South):
                    dir_grid[i][j] = "S"
                if(max_la == choose_North):
                    dir_grid[i][j] = "N"
                update = iter_grid[i][j] +  max_la
                if(abs(update - iter_grid[i][j])> max_change):
                    max_change = abs(update - iter_grid[i][j])
                iter_grid_update[i][j] = update
    if(max_change <= 100):
        print(dir_grid)
        break;
    else:
        iter_grid = copy.deepcopy(iter_grid_update)
        print("Updated!")
        print(max_change)
        print('\n')
        print(iter_grid)
        print('\n')
        print(dir_grid)
        print('\n')
