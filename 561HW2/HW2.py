file = open('input.txt').read().splitlines()

num_shelters = int(file[0])
num_parklots = int(file[1])

LAHSA_size_chosen = int(file[2])
i = 0
LAHSA_chosen = []
while(i < LAHSA_size_chosen):
    LAHSA_chosen.append(file[3 + i])
    i += 1

SPLA_size_chosen = int(file[3 + LAHSA_size_chosen])
j = 1;
SPLA_chosen = []
while(j <= SPLA_size_chosen):
    SPLA_chosen.append(file[3 + LAHSA_size_chosen + j])
    j += 1

appli_size = int(file[3 + SPLA_size_chosen + LAHSA_size_chosen + 1])
k = 0
appli_list = []
appr = 5 + SPLA_size_chosen + LAHSA_size_chosen
while(k < appli_size):
    if((file[appr + k][5] == 'F' and file[appr + k][9] == 'N' and ((int(file[appr + k][7]) == 1 and int(file[appr + k][8]) >= 7)
    and (int(file[appr + k][7]) >= 2))) or (file[appr + k][11] == 'Y' and file[appr + k][12] == 'Y' and file[appr + k][10] == 'N')):
        appli_list.append(file[appr + k])
    k += 1


print(num_shelters)
print(num_parklots)
print(LAHSA_chosen)
print(SPLA_chosen)
print(appli_list)
print("\n")

"""max_dict initialize"""
max_dict = {}
for next_choice in appli_list:
    max_dict[next_choice] = 0;
print (max_dict)

print("\n")

"""SPLA residual positions available"""
res = {}
res["Mon"] = num_parklots
res["Tue"] = num_parklots
res["Wed"] = num_parklots
res["Thu"] = num_parklots
res["Fri"] = num_parklots
res["Sat"] = num_parklots
res["Sun"] = num_parklots
print(res)

for x in SPLA_chosen:
    for y in appli_list:
        if(x[4] == y[4]):
            res["Mon"] -= int(y[13])
            res["Tue"] -= int(y[14])
            res["Wed"] -= int(y[15])
            res["Thu"] -= int(y[16])
            res["Fri"] -= int(y[17])
            res["Sat"] -= int(y[18])
            res["Sun"] -= int(y[19])

print(res)
print("\n")



for x in LAHSA_chosen:
    for y in appli_list[:]:
        if (x[0] == y[0] and x[1] == y[1] and x[2] == y[2] and x[3] == y[3] and x[4] == y[4]):
            appli_list.remove(y)

for x in SPLA_chosen:
    for y in appli_list[:]:
        if (x[0] == y[0] and x[1] == y[1] and x[2] == y[2] and x[3] == y[3] and x[4] == y[4]):
            appli_list.remove(y)

print(appli_list)

"""sorted tuple based on appli_needs"""
import operator
sorted_appli_dict = {};
for y in appli_list:
    if(y[9] == 'N' and y[5] == 'F' and ((int(y[7]) == 1 and int(y[8]) > 7) or (int(y[7]) >= 2))):
        sorted_appli_dict[y] = int(y[19]) + int(y[13]) + int(y[14]) + int(y[15]) + int(y[16]) + int(y[17]) + int(y[18])
sorted_appli_list = sorted(sorted_appli_dict.items(),  key=operator.itemgetter(1), reverse = True)

print(sorted_appli_list)
smaller_ID = ""
"""Check function whether the bigggest one meets requirement"""
i = 0
while(i < len(sorted_appli_list) - 1):
    if(sorted_appli_list[i][1] == sorted_appli_list[i + 1][1] and sorted_appli_list[i][0][4] > sorted_appli_list[i + 1][0][4]):
        temp = sorted_appli_list[i]
        sorted_appli_list[i] = sorted_appli_list[i + 1]
        sorted_appli_list[i + 1] = temp
    i += 1

print(sorted_appli_list)

result = ""
for x in sorted_appli_list:
    if(res["Mon"] - int(x[0][13]) >= 0 and res["Tue"] - int(x[0][14]) >= 0 and res["Wed"] - int(x[0][15]) >= 0
    and res["Thu"] - int(x[0][16]) >= 0 and res["Fri"] - int(x[0][17]) >= 0 and res["Sat"] - int(x[0][18]) >= 0
    and res["Sun"] - int(x[0][19]) >= 0):
        result = x[0][0:5]
        break;

print(result)
f = open("output.txt", "w")
f.write(result)


"""max_LAHSA = 0
max_SPLA = 0
SPLA_FC = ""
cnt = 1
LAHSA_choices = []
SPLA_choices = []


def LAHSA_search(appli_list, res, SPLA_choices):
    if((res["Mon"] == 0 and res["Tue"] == 0 and res["Wed"] == 0 and res["Thu"] == 0
    and res["Fri"] == 0 and res["Sat"] == 0 and res["Sun"] == 0 ) or appli_list.size() == 0):
        return;
    while(appli_list[k][9] == 'N' and appli_list[k][5] == 'F' and
    ((int(appli_list[k][7]) == 1 and int(appli_list[k][8]) > 7) or (int(appli_list[k][7]) >= 2))):
        LAHSA_choices.append(appli_list[k])
        del(appli_list[k])

def SPLA_search(appli_list, res, SPLA_choices):
    if((res["Mon"] == 0 and res["Tue"] == 0 and res["Wed"] == 0 and res["Thu"] == 0
    and res["Fri"] == 0 and res["Sat"] == 0 and res["Sun"] == 0 ) or appli_list.size() == 0):
        return;
    while(appli_list[j][10] == 'N' and appli_list[j][11] == 'Y' and appli_list[j][12] == 'Y'):
        if(cnt == 1):
            SPLA_FC = appli_list[j]
        tempj = appli_list[j]
        del(appli_list[j])
"""
