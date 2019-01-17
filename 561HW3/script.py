file = open('input1.txt').read().splitlines()

grid_size = int(file[0])
car_num =  int(file[1])
obs_num = int(file[2])

grid_val_init = []
grid_dir_init = []
cars = []
obs = []
veh = []

import copy

def turn_left(move):
    if (move == 'N'):
        return 'W'
    elif(move == 'W'):
        return 'S'
    elif(move == 'S'):
        return 'E'
    elif(move == 'E'):
        return 'N'
    else:
        return 'H'

def turn_right(move):
    if (move == 'N'):
        return 'E'
    elif(move == 'E'):
        return 'S'
    elif(move == 'S'):
        return 'W'
    elif(move == 'W'):
        return 'N'
    else:
        return 'H'


"""grid Initialization"""
row = []
dir_row = []
for x in range(0, grid_size):
    row.append(-1)
    dir_row.append("H")
for x in range(0, grid_size):
    grid_val_init.append(copy.deepcopy(row))
    grid_dir_init.append(copy.deepcopy(dir_row))

a = 0
while(a < obs_num):
    obs.append(map(int, file[3 + a].split(',')))
    grid_val_init[obs[a][0]][obs[a][1]] = -101
    a += 1


b = 0
while(b < car_num):
    cars.append(map(int,file[3 + a + b].split(',')))
    b += 1

result = []

c = 0
while(c < car_num):
    veh.append(map(int, file[3 + a + b + c].split(',')))
    grid_val = copy.deepcopy(grid_val_init)
    grid_val_updated = copy.deepcopy(grid_val_init)
    grid_reward = copy.deepcopy(grid_val_init)
    grid_dir = copy.deepcopy(grid_dir_init)
    grid_val[veh[c][0]][veh[c][1]] = 99
    grid_val_updated[veh[c][0]][veh[c][1]] = 99
    grid_reward[veh[c][0]][veh[c][1]] = 99
    grid_dir[veh[c][0]][veh[c][1]] = 'H'
    ends = file[3 + a + b + c]
    while(1):
        change_max = 0
        for i in range(0, grid_size):
            for j in range(0, grid_size):
                if(grid_val[i][j] == 99):
                    continue;
                if(i == 0):
                    East = grid_val[i+1][j]
                    West = grid_val[i][j]
                    if(j == 0):
                        North = grid_val[i][j]
                        South = grid_val[i][j+1]
                    elif(j == grid_size - 1):
                        South = grid_val[i][j]
                        North = grid_val[i][j-1]
                    else:
                        North = grid_val[i][j-1]
                        South = grid_val[i][j+1]
                elif(i == grid_size - 1):
                    East = grid_val[i][j]
                    West = grid_val[i-1][j]
                    if(j == 0):
                        North = grid_val[i][j]
                        South = grid_val[i][j+1]
                    elif(j == grid_size - 1):
                        South = grid_val[i][j]
                        North = grid_val[i][j-1]
                    else:
                        North = grid_val[i][j-1]
                        South = grid_val[i][j+1]
                elif(j == 0):
                    North = grid_val[i][j]
                    South = grid_val[i][j+1]
                    West = grid_val[i-1][j]
                    East = grid_val[i+1][j]
                elif(j == grid_size - 1):
                    North = grid_val[i][j-1]
                    South = grid_val[i][j]
                    West = grid_val[i-1][j]
                    East = grid_val[i+1][j]
                else:
                    North = grid_val[i][j-1]
                    South = grid_val[i][j+1]
                    West = grid_val[i-1][j]
                    East = grid_val[i+1][j]
                pick_N = 0.7 * North + 0.1 * South + 0.1 * West + 0.1 * East
                pick_S = 0.1 * North + 0.7 * South + 0.1 * West + 0.1 * East
                pick_W = 0.1 * North + 0.1 * South + 0.7 * West + 0.1 * East
                pick_E = 0.1 * North + 0.1 * South + 0.1 * West + 0.7 * East
                MAX = max(pick_N, pick_S, pick_W, pick_E)
                if(MAX == pick_W):
                    grid_dir[i][j] = 'W'
                if(MAX == pick_E):
                    grid_dir[i][j] = 'E'
                if(MAX == pick_S):
                    grid_dir[i][j] = 'S'
                if(MAX == pick_N):
                    grid_dir[i][j] = 'N'
                grid_val_updated[i][j] = MAX * 0.9 + grid_reward[i][j]
                if(change_max < abs(grid_val_updated[i][j] - grid_val[i][j])):
                    change_max = abs(grid_val_updated[i][j] - grid_val[i][j])
        grid_val = copy.deepcopy(grid_val_updated)
        if(change_max < (0.01/0.9)):
            print(grid_dir)
            break;

    total_reward = 0
    import numpy as np
    for j in range(10):
        pos = copy.deepcopy(cars[c])
        np.random.seed(j)
        swerve = np.random.random_sample(1000000)
        k = 0
        while (1):
            print(pos)
            move = grid_dir[pos[0]][pos[1]]
            print(move)
            print(swerve[k])
            if swerve[k] > 0.7:
                if swerve[k] > 0.8:
                    if swerve[k] > 0.9:
                        move = turn_left(turn_left(move))
                    else:
                        move = turn_right(move)
                else:
                    move = turn_left(move)
            print(move)
            if(move == 'N' and pos[1] > 0):
                pos[1] -= 1
            elif(move == 'S' and pos[1] < grid_size - 1):
                pos[1] += 1
            elif(move == 'W' and pos[0] > 0):
                pos[0] -= 1
            elif(move == 'E' and pos[0] < grid_size - 1):
                pos[0] += 1
            elif(move == 'H'):
                print("right!")
                print(total_reward)
                print('\n')
                break;
            total_reward += grid_reward[pos[0]][pos[1]]
            print("total_reward")
            print(total_reward)
            print('\n')
            k += 1
    result.append(int(total_reward / 10))
    total_reward = 0;
    print("result:")
    print(result)
    print('\n')
    c += 1
print(result)
f = open("output.txt", "w")
for i in range(len(result)):
    f.write(str(result[i]) + '\n')
