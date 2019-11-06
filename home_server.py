import tkinter
from PIL import Image,ImageTk


root=None
destflag=1

def instr():
    global root,destflag
    root.destroy()
    destflag=1
    root = tkinter.Tk()
    root.title("Instructions")
    root.configure(background='black')
    root.geometry("400x580")

    label1=tkinter.Label(padx="135",pady="20",text="Instructions",bg='#000000',fg='#ffffff')
    label1.config(font=("Courier",14))
    label1.pack()


    label2=tkinter.Label(root,text="1.The gameplay takes place in an m times n m×n board.\n2.For each cell in the board, we define a critical mass. The critical mass is equal to the number of orthogonally adjacent cells. That would be 4 for usual cells, 3 for cells in the edge and 2 for cells in the corner.\n3.All cells are initially empty. The Red and the Green player take turns to place orbs of their corresponding colors. The Red player can only place an (red) orb in an empty cell or a cell which already contains one or more red orbs. When two or more orbs are placed in the same cell, they stack up.\n4.When a cell is loaded with a number of orbs equal to its critical mass, the stack immediately explodes. As a result of the explosion, to each of the orthogonally adjacent cells, an orb is added and the initial cell looses as many orbs as its critical mass. The explosions might result in overloading of an adjacent cell and the chain reaction of explosion continues until every cell is stable.\n5.When a red cell explodes and there are green cells around, the green cells are converted to red and the other rules of explosions still follow. The same rule is applicable for other colors.\n6.The winner is the one who eliminates every other players orbs.",bg='#000000',fg='#ffffff',wraplength="370",justify="left")
    label2.config(font=("Courier",10))
    label2.pack()
    back_btn=tkinter.Button(root,text="Back",command=init_page)
    back_btn.pack()
    root.protocol('WM_DELETE_WINDOW')
    root.mainloop()

def new_game():
    global root,destflag
    root.destroy()
    import sgui2nd_recur
    # root=tkinter.Tk()
    # destflag=1
    # init_page()

def more_page():
    global root,destflag
    root.destroy()
    import testmatnew


def init_page():
    global root,destflag
    if destflag==1:
        root.destroy()
    root=tkinter.Tk()
    width = root.winfo_screenwidth()        #height of screen
    height = root.winfo_screenheight()      #width of screen
    print("height :",height,"\nwidth :",width)
    resolution=str(width)+"x"+str(height)
    root.geometry(resolution)
    root.title("Chain Reaction (SERVER)")



    canvas = tkinter.Canvas(root,background="cyan" ,width = width, height = height )
    canvas.pack()
    frame=tkinter.Frame(canvas,bg='cyan')
    frame.place(relwidth=1,relheight=1)




    chainreaction_image = Image.open("chainreaction.png")
    chainreaction_image = chainreaction_image.resize((int(.3*width), int(.3*height)),Image.ANTIALIAS)
    chainreaction_image = ImageTk.PhotoImage(chainreaction_image)

    start_image = Image.open("start.png")
    start_image = start_image.resize((int(.15*width), int(.10*height)),Image.ANTIALIAS)
    start_image = ImageTk.PhotoImage(start_image)

    more_image = Image.open("stats.png")
    more_image = more_image.resize((int(.15*width), int(.10*height)),Image.ANTIALIAS)
    more_image = ImageTk.PhotoImage(more_image)

    help_image = Image.open("help.png")
    help_image = help_image.resize((100,100),Image.ANTIALIAS)
    help_image = ImageTk.PhotoImage(help_image)

    exit_image = Image.open("exit.png")
    exit_image = exit_image.resize((int(.15*width), int(.10*height)), Image.ANTIALIAS)
    exit_image = ImageTk.PhotoImage(exit_image)






    chainreaction_button = tkinter.Button(frame,image=chainreaction_image,bd=0,bg="cyan",relief="flat", activebackground="cyan")
    chainreaction_button.place(x=(width/2-.15*width),y=(height/2-.15*height-200))

    start_button = tkinter.Button(frame,image=start_image,bd=0,bg="cyan",relief="raised",   activebackground="cyan",command=new_game)
    start_button.place(x=50,y=400)

    more_button = tkinter.Button(frame,image=more_image,bd=0,bg="cyan",relief="flat",activebackground="cyan",command=more_page)
    more_button.place(x=50,y=500)

    help_button = tkinter.Button(frame,image=help_image,anchor='ne',bd=0,bg="cyan",relief="flat",   activebackground="cyan",command=instr)
    help_button.place(x=width-150,y=50)

    exit_button = tkinter.Button(frame,image=exit_image,bd=0,bg="cyan",relief="raised",activebackground="cyan", command=quit)
    exit_button.place(x=50,y=height-50-86-int(.10*height))
    print(int(.10*height))




    #canvas.create_image(20,height-200,anchor="nw" ,image=start_button)
    #create_image(xpad,ypad,....)
    # root.protocol('WM_DELETE_WINDOW',False)
    root.mainloop()
root = tkinter.Tk()
init_page()