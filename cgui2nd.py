import socket
import pickle
import threading
import time
import tkinter

canvas=None
s=None
player_id=0
username=""
name_entry=None
root=None

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

players = 3
max_row = 9
max_col = 6
cell_size = 60
radius = 10
move = 0
lost_players = []
end = False
canvas=None
curr = 0
username=""

def clear_screen():
    canvas.create_rectangle(0, 0, max_col * cell_size,
                            max_row * cell_size, fill="#000000")
    return


def reDraw(num, block_owner, col_3):
    color[len(color) - 1] = col_3
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


def click(event):
    global num, block_owner, color,move
    if curr == color[len(color) - 1]:
        move+=1
        s.send(bytes(str(player_id), encoding="utf-8"))

        cords = [event.x, event.y]
        data = pickle.dumps(cords)

        s.send(bytes(str(len(data)), "utf-8"))
        s.send(data)


def transfering(root):
    global curr, s, num, block_owner,canvas
    while True:
        canvas.bind('<Button-1>', click)
        while True:
            if s.recv(1024).decode():  # changes
                break
            else:
                time.wait(0.1)

        print("received changes")
        status = s.recv(1024).decode()
        if status == "Continue" or status == "finish":
            data_len = int(s.recv(3).decode())
            data1 = s.recv(data_len)
            num = pickle.loads(data1)

            data_len = int(s.recv(3).decode())
            data2 = s.recv(data_len)
            block_owner = pickle.loads(data2)

            c = int(s.recv(1).decode())
            clear_screen()
            reDraw(num, block_owner, c)
            curr = int(s.recv(1).decode())
            print("Curr", curr)
            if status=="finish":
                break
        else:
            break
    print("HI")
    canvas.unbind_all('<Button-1>')
    root.destroy()

def getuser():
    global username,root
    username=name_entry.get()
    if(len(username)<3):
        msg=tkinter.messagebox.showerror(title="Name Error",message="Name cannot be less than 3 character")
        getname
    elif(len(username)>9):
        msg=tkinter.messagebox.showerror(title="Name Error",message="Name cannot be more than 9 character")
        getname
    else:
        frame1.pack_forget()
        return()

def play():
    global root,s,player_id,username,canvas
    getuser()
    root.destroy()
    s = socket.socket()
    host = socket.gethostname()
    port = 4444
    s.connect((host, port))

    player_id = int(s.recv(1).decode())
    s.send(bytes(str(len(username)),encoding="utf-8"))
    s.send(bytes(username,encoding="utf-8"))
    print("id :", player_id)
    while True:
        if s.recv(1024).decode():
            curr = int(s.recv(8).decode())
            print("Curr", curr)
            root = tkinter.Tk()
            canvas = tkinter.Canvas(root, width=max_col * cell_size,
                                    height=max_row * cell_size, bg="#000000")
            canvas.pack()

            for i in range(0, max_col):
                canvas.create_line(i * cell_size, 0, i * cell_size,
                                max_row * cell_size, fill=color[color[len(color) - 1]])
            for j in range(0, max_row):
                canvas.create_line(0, j * cell_size, max_col *
                                cell_size, j * cell_size, fill=color[color[len(color) - 1]])
            root.title(username)
            threading._start_new_thread(transfering, (root,))
            root.mainloop()
            s.close()
            break
        else:
            time.sleep(0.1)
    print("GAMEOVER!!!")

def getname():

    global name_entry

    frame1.place(x=40,y=40)

    label=tkinter.Label(frame1,text="ENTER NAME",background="pink",justify="center")
    label.config(font=("Comic Sans MS",12))
    label.place(x=frame1.winfo_reqwidth()/2-100,y=0.25*frame1.winfo_reqheight(),width=200)

    name_entry=tkinter.Entry(frame1,bd=2,width=30,justify="center")
    name_entry.config(font=("",12))
    name_entry.place(x=frame1.winfo_reqwidth()/2-(0.7*frame1.winfo_reqwidth()/2),y=0.50*frame1.winfo_reqheight(),relwidth=.7,relheight=.09)

    button1=tkinter.Button(frame1,text="GO",background="#45CE30",command=play)
    button1.place(x=frame1.winfo_reqwidth()/2-30,y=.65*frame1.winfo_reqheight(),width=60)





root=tkinter.Tk()
frame1=tkinter.Frame(root,background="pink",height=max_row * cell_size-80,width=max_col * cell_size-80)
root.protocol('WM_DELETE_WINDOW',False)
resolution=str(max_col * cell_size)+"x"+str(max_row * cell_size)
root.config(background="cyan")
root.geometry(resolution)
root.resizable(0,0)
getname()



root.mainloop()