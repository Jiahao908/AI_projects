import copy

f = open("input1.txt")
n = int(f.readline())
p_sum = int(f.readline())
s_sum = int(f.readline())
police_map = []
q = []
r = {}

for a in range(0, n):
    for b in range(0, n):
        r[(a, b)] = 0

for i in range(0, n):
    q.append(0);


for j in range(0, n):
    police_map.append(copy.copy(q));




for line in f:
    i = int(line[0])
    j = int(line[2])
    r[j,i] += 1

f.close()


def mark(col, row, p):
    for a in range(0, n):
        p[a][col] += 1
    for b in range(0, n):
        p[row][b] += 1
    for c, d in zip(range(row, -1, -1), range(col, -1, -1)):
        p[c][d] += 1
    for e, f in zip(range(row, n), range(col, -1, -1)):
        p[e][f] += 1
    for g, h in zip(range(row, -1, -1), range(col, n)):
        p[g][h] += 1
    for i, j in zip(range(row, n), range(col, n)):
        p[i][j] += 1

def demark(col, row, p):
    for a in range(0, n):
        p[a][col] -= 1
    for b in range(0, n):
        p[row][b] -= 1
    for c, d in zip(range(row, -1, -1), range(col, -1, -1)):
        p[c][d] -= 1
    for e, f in zip(range(row, n), range(col, -1, -1)):
        p[e][f] -= 1
    for g, h in zip(range(row, -1, -1), range(col, n)):
        p[g][h] -= 1
    for i, j in zip(range(row, n), range(col, n)):
        p[i][j] -= 1



"""mark(1,2,p)

for i in r:
    print (i, r[i])
for key, value in sorted(r.iteritems(), key = lambda(k,v):(v,k), reverse = True):
    print(key, r[key])
"""

res = []
global max
max = 0

sorted_r = sorted(r.iteritems(), key = lambda(k,v):(v,k), reverse = True)

"""for i in sorted_r[2:]:
    print (i[1])"""



def put_police(last_add, sum, p_num, police_map, current_pos):
    if(p_num < p_sum):
        cnt = 0
        for key, value in sorted_r[current_pos:]:
            global max
            cnt += 1
            if(p_num == 0 and value <= max):
                return;
            if(police_map[key[0]][key[1]] <= 0):
                mark(key[1], key[0], police_map)
                sum += value
                put_police(value, sum, p_num + 1, police_map, current_pos+cnt)
                demark(key[1], key[0], police_map)
                sum -= value
    else:
        res.append(sum)
        global max
        max = last_add




put_police(0, 0, 0, police_map, 0)

res.sort(reverse = True)
f2 = open("output.txt", "w")
f2.write(str(res[0]))
f2.close()
