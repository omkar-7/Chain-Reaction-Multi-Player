import dbms
import socket
from threading import *
import threading
import pickle
import time
import queue
import tkinter

num = [[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

block_owner = [[-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1]]


color = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00",
         "#00FFFF", "#FF00FF", "#FF7F00", "#FFFFFF", 0]
flag=1
root=None
canvas = None
max_row = 9
max_col = 6
cell_size = 60
radius = 10
move = 0
lost_players = []
end = False
_row = -1
_col = -1
moves_list = []
players_name=[]
# players_name = ["anant","omkar","Ronaldo","shohaib","subhradeep"]

   

current_client = 0


def explode(row, col):
    block_owner[row][col] = -1
    num[row][col] = 0

    if row - 1 >= 0:
        num[row - 1][col
                     ] = num[row - 1][col] + 1
        block_owner[row - 1][col] = color[len(color) - 1]
        if(willExplode(row - 1, col)):
            explode(row - 1, col)

    if row + 1 < max_row:
        num[row + 1][col
                     ] = num[row + 1][col] + 1
        block_owner[row + 1][col] = color[len(color) - 1]
        if(willExplode(row + 1, col)):
            explode(row + 1, col)

    if col - 1 >= 0:
        num[row][col -
                 1] = num[row][col - 1] + 1
        block_owner[row][col - 1] = color[len(color) - 1]
        if(willExplode(row, col - 1)):
            explode(row, col - 1)

    if col + 1 < max_col:
        num[row][col +
                 1] = num[row][col + 1] + 1
        block_owner[row][col + 1] = color[len(color) - 1]
        if(willExplode(row, col + 1)):
            explode(row, col + 1)

    return


def willExplode(row, col):
    limit = 3
    if row == 0 or row == max_row - 1:
        limit = limit - 1
    if col == 0 or col == max_col - 1:
        limit = limit - 1
    if num[row][col] > limit:
        return True
    return False



def on_click(x_cords, y_cords):
    global move, end,n
    if not end:
        _row = row = int(y_cords / cell_size)
        _col = col = int(x_cords / cell_size)

        if block_owner[row][col] == color[len(color) - 1] or block_owner[row][col] == -1:
            block_owner[row][col] = color[len(color) - 1]
            num[row][col] = num[row][col] + 1

            if willExplode(row, col):
                explode(row, col)

            if move >= players:
                for i in range(0, players):
                    if (i not in lost_players) and player_lost(i):
                        print("Player ", i, " has lost !!!")
                        lost_players.append(i)
                        moves_list[i]=(move//n)
                        if move % n > i:
                             moves_list[i] += 1
                if len(lost_players) == players - 1:
                    end = True
            move = move + 1
            while True:
                color[len(color) - 1] = (color[len(color) - 1] + 1) % players
                if color[len(color) - 1] not in lost_players:
                    break

            reDraw()

            if end:
                print(" GAME OVER !!! ")
                return
    else:
        print(" GAME OVER !!! ")
    print(lost_players)
    print("play")
    return


def player_lost(player_num):
    for i in range(0, max_row):
        if player_num in block_owner[i]:
            return False
    return True


def reDraw():
    global canvas
    canvas.create_rectangle(0, 0, max_col * cell_size,
                            max_row * cell_size, fill="#000000")
    for i in range(0, max_col):
        canvas.create_line(i * cell_size, 0, i * cell_size, max_row *
                           cell_size, fill=color[color[len(color) - 1]])
    for j in range(0, max_row):
        canvas.create_line(0, j * cell_size, max_col * cell_size,
                           j * cell_size, fill=color[color[len(color) - 1]])
    for i in range(0, max_row):
        for j in range(0, max_col):
            if num[i][j] == 1:
                canvas.create_oval(j * cell_size + cell_size / 2 - radius, i * cell_size + cell_size / 2 - radius,
                                   j * cell_size + cell_size / 2 + radius, i * cell_size + cell_size / 2 + radius, fill=color[block_owner[i][j]])
            elif num[i][j] == 2:
                canvas.create_oval(j * cell_size + cell_size / 2 + 10 - radius, i * cell_size + cell_size / 2 - radius,
                                   j * cell_size + cell_size / 2 + 10 + radius, i * cell_size + cell_size / 2 + radius, fill=color[block_owner[i][j]])
                canvas.create_oval(j * cell_size + cell_size / 2 - 10 - radius, i * cell_size + cell_size / 2 - radius,
                                   j * cell_size + cell_size / 2 - 10 + radius, i * cell_size + cell_size / 2 + radius, fill=color[block_owner[i][j]])
            elif num[i][j] == 3:
                canvas.create_oval(j * cell_size + cell_size / 2 + 10 - radius, i * cell_size + cell_size / 2 - radius + radius * pow(3, 0.5) / 3,
                                   j * cell_size + cell_size / 2 + 10 + radius, i * cell_size + cell_size / 2 + radius + radius * pow(3, 0.5) / 3, fill=color[block_owner[i][j]])
                canvas.create_oval(j * cell_size + cell_size / 2 - 10 - radius, i * cell_size + cell_size / 2 - radius + radius * pow(3, 0.5) / 3,
                                   j * cell_size + cell_size / 2 - 10 + radius, i * cell_size + cell_size / 2 + radius + radius * pow(3, 0.5) / 3, fill=color[block_owner[i][j]])
                canvas.create_oval(j * cell_size + cell_size / 2 - radius, i * cell_size + cell_size / 2 - radius - 2 * radius * pow(3, 0.5) / 3,
                                   j * cell_size + cell_size / 2 + radius, i * cell_size + cell_size / 2 + radius - 2 * radius * pow(3, 0.5) / 3, fill=color[block_owner[i][j]])
    return


def flow_control(clients):
    global current_client, n
    while True:
        current_client = (current_client+1) % n
        if current_client not in lost_players:
            break
    print("curr :", current_client)
    for i in clients:
        i.send(bytes(str(current_client), encoding="utf-8"))
    return


def send_to_rest_all(clients):
    global n, current_client,end
    for i in range(n):
        clients[i].send(bytes("Changes", encoding="utf-8"))
        time.sleep(0.0001)
        if not end:
            clients[i].send(bytes("Continue",encoding="utf-8"))
        else:
            clients[i].send(bytes("finish",encoding="utf-8"))

def send_changes(clients, num, block_owner, color):
    for i in clients:
        data1 = pickle.dumps(num)
        i.send(str.encode(str(len(data1))))
        i.send(data1)
        data2 = pickle.dumps(block_owner)
        i.send(str.encode(str(len(data2))))
        i.send(data2)
        c = color[len(color) - 1]
        i.send(str.encode(str(c)))

def write_to_file():
    global _row, _col
    file_ptr = open("data.txt", "wb")
    pickle.dump(num, file_ptr)
    pickle.dump(block_owner, file_ptr)
    pickle.dump(lost_players, file_ptr)
    temp = [_row, _col, color[len(color) - 1], move]
    pickle.dump(temp, file_ptr)
    file_ptr.close()
    return

def threads(con):
    global clients,root,current_client, num, block_owner, color,end
    # protocol = True
    while not end:
        # l=[1,2,3,4,5,6,7]
        while True:
            try:
                sync = int(con.recv(1).decode())  # recv p_id
            except:
                pass
            print(sync, " ", current_client)
            if sync != current_client:
                data_len = int(con.recv(2).decode())
                data = con.recv(data_len)  # no other option.
                cords = pickle.loads(data)
            else:
                data_len = int(con.recv(2).decode())
                data = con.recv(data_len)
                cords = pickle.loads(data)

                temp_c = int(cords[0] / cell_size)
                temp_r = int(cords[1] / cell_size)

                print(temp_r, " ", temp_c)

                if block_owner[temp_r][temp_c] == current_client or block_owner[temp_r][temp_c] == -1:
                    break
                else:
                    pass 
        print("Cords : ", cords)
        on_click(cords[0], cords[1])
        write_to_file()
        print("clients : ", len(clients))
        print("lost_players : ", lost_players)
        send_to_rest_all(clients)
        send_changes(clients, num, block_owner, color)
        flow_control(clients)
    root.destroy()


def run_clients(clients):
    for i in clients:
        threading._start_new_thread(threads, (i,))
    for i in clients:
        i.send(bytes("Start", encoding="utf-8"))
        print("sent")
        i.send(bytes(str(0), encoding="utf-8"))  # curr


def server():  # thread
    global canvas,clients,root,flag
    root = tkinter.Tk()
    root.title("Server")
    canvas = tkinter.Canvas(root, width=max_col * cell_size,
                            height=max_row * cell_size, bg="#000000")
    canvas.pack()
    for i in range(0, max_col):
        canvas.create_line(i * cell_size, 0, i * cell_size,
                           max_row * cell_size, fill=color[color[len(color) - 1]])
    for j in range(0, max_row):
        canvas.create_line(0, j * cell_size, max_col *
                           cell_size, j * cell_size, fill=color[color[len(color) - 1]])
    root.mainloop()
    # return()
    flag=0

def dbms_(players_name,moves_list,lost_players):
    global n
    for i in range(n):
        if i != n-1:
            dbms.insert_all(players_name[lost_players[i]],0,n)
            dbms.update_database(players_name[lost_players[i]],moves_list[lost_players[i]],0)
        else:
            dbms.insert_all(players_name[lost_players[i]],1,n)
            dbms.update_database(players_name[lost_players[i]],moves_list[lost_players[i]],1)

s = socket.socket()
host = socket.gethostname()
print(host)
port = 4444
s.bind((host, port))
s.listen(4)
players = int(input("Enter the number of players : "))
n = players2 = players
id = 0
start_clients = 1
clients = []
gameover=0

for i in range(n):
    moves_list.append(0)

while True:
    while players2 > 0:
        if players2 == 1:
            print("Waiting For", players2, "player to join...")
        else:
            print("Waiting For", players2, "players to join...")
        clt, ad = s.accept()
        clt.send(bytes(str(id), encoding="utf-8"))
        l=int(clt.recv(1).decode())
        players_name.append(clt.recv(l).decode())
        print(players_name)
        id += 1
        clients.append(clt)
        players2 -= 1
    if start_clients == 1:
        print("All Players connected")
        threading._start_new_thread(server, ())
        run_clients(clients)
        start_clients = 0
    if flag==0:
        for q in range(n):
            if q not in lost_players:
                lost_players.append(q)
                moves_list[q]=(move//n)
                if move % n > q:
                    moves_list[q] += 1
        print("lost : ",lost_players)
        print("Moves List",moves_list)
        gameover=1
        dbms.connect_db()
        dbms_(players_name,moves_list,lost_players)
    if gameover == 1:
        break
s.close()

print("Game-Over!!!")