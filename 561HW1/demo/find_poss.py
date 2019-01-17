p = []
q = []
r = []
n = 8
p_sum = 8

import copy


for i in range(0, n):
    q.append('.');


for j in range(0, n):
    p.append(copy.copy(q));



for k in range(0, n):
    r.append(q);

all_P = [];

def isvalid (row, col, p):
    for i in range(0, n):
        if(p[i][col] == 'P'):
            return False
    for j in range(0, n):
        if(p[row][j] == 'P'):
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if(p[i][j] == 'P'):
            return False
    for i, j in zip(range(row -1,  -1, -1), range(col + 1, n)):
        if(p[i][j] == 'P'):
            return False
    for i, j in zip(range(row + 1, n), range(col - 1, -1, -1)):
        if(p[i][j] == 'P'):
            return False
    for i, j in zip(range(row + 1, n), range(col + 1, n)):
        if(p[i][j] == 'P'):
            return False
    return True



def put_police(row, col, p_num):
    if(p_num < p_sum):
        for i in range(row, n):
            for j in range(col, n):
                if( isvalid(i, j, p)):
                    print (i, j, p_num)
                    p[i][j] = 'P'
                    put_police(0, 0, p_num + 1)
                    p[i][j] = '.'
    else:
        all_P.append(copy.deepcopy(p))
        for i in all_P:
            print(i)








put_police(0, 0, 0)
