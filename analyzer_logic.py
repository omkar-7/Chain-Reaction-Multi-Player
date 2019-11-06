import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pickle

a = 0.4
b = 0.3
c = 0.1
d = 0.2

lost_plyrs = []


def main():
    global lost_plyrs

    aggression = 0
    win_cnt = 0
    own_cell = 0
    explodable_cell = 0
    opp_explodable = 0
    file_ptr = open("data.txt", "rb")

    num = pickle.load(file_ptr)
    blk_ownr = pickle.load(file_ptr)
    lost_plyrs = pickle.load(file_ptr)
    _temp = pickle.load(file_ptr)
    file_ptr.close()

    c_row = int(_temp[0])
    c_col = int(_temp[1])
    cur_plyr = int(_temp[2])
    move = int(_temp[3])

    if 0 < move < 20:
        if c_row - 1 >= 0:
            if blk_ownr[c_row - 1][c_col] != cur_plyr:
                aggression = (aggression * (move - 1) + 1) / move
        if c_row + 1 < 9:
            if blk_ownr[c_row + 1][c_col] != cur_plyr:
                aggression = (aggression * (move - 1) + 1) / move
        if c_col - 1 >= 0:
            if blk_ownr[c_row][c_col - 1] != cur_plyr:
                aggression = (aggression * (move - 1) + 1) / move
        if c_col + 1 < 6:
            if blk_ownr[c_row][c_col + 1] != cur_plyr:
                aggression = (aggression * (move - 1) + 1) / move

    for plyr in range(players):

        own_cell = 0
        explodable_cell = 0
        opp_explodable = 0

        for i in range(9):
            own_cell += blk_ownr[i].count(plyr)
            if blk_ownr[i].count(plyr):
                for j in range(6):
                    temp = check_explode(num, i, j)
                    explodable_cell += temp
                    if temp:
                        if i - 1 >= 0:
                            if blk_ownr[i - 1][j] != plyr:
                                opp_explodable += 1
                        if i + 1 < 6:
                            if blk_ownr[i + 1][j] != plyr:
                                opp_explodable += 1
                        if j - 1 >= 0:
                            if blk_ownr[i][j - 1] != plyr:
                                opp_explodable += 1
                        if j + 1 < 9:
                            if blk_ownr[i][j + 1] != plyr:
                                opp_explodable += 1

        win_cnt = a * aggression + b * own_cell + \
            c * explodable_cell + d * opp_explodable
        win_vals[plyr] = win_cnt


def check_explode(num, c_row, c_col):
    limit = 3
    explode_intensity = 0
    if c_row == 0 or c_row == 9:
        limit -= 1
        explode_intensity += 1
    if c_col == 0 or c_col == 6:
        limit -= 1
        explode_intensity += 1
    if num[c_row][c_col] == limit:
        return explode_intensity
    return 0


def animate(i):
    main()
    temp_win_val = []
    _sum = 0
    for i in range(players):
        if i in lost_plyrs:
            win_vals[i] = 0
        _sum += win_vals[i]
    if not _sum:
        _sum = 1
    for i in range(players):
        temp_win_val.append(win_vals[i] / _sum)

    return plt.bar(plyr_names, temp_win_val)


players = 0
win_vals = []
plyr_names = []


players = int(input("Enter no of Players : "))

for i in range(players):
    plyr_names.append(str(i))
    win_vals.append(0)


style.use('seaborn-bright')
fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, blit=True, interval=1000)

plt.bar(plyr_names, win_vals)
plt.show()
