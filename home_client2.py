import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk


root=None
mainmenu_frame=None
width=height=0
help_frame=None

def help():
    '''global root
    root.destroy()
    root = tkinter.Tk()'''
    root.title("Instructions")
    #global mainmenu_frame
    instruction="1.The gameplay takes place in an m times n m×n board.\n2.For each cell in the board, we define a critical mass. The critical mass is equal to the number of orthogonally adjacent cells. That would be 4 for usual cells, 3 for cells in the edge and 2 for cells in the corner.\n3.All cells are initially empty. The Red and the Green player take turns to place orbs of their corresponding colors. The Red player can only place an (red) orb in an empty cell or a cell which already contains one or more red orbs. When two or more orbs are placed in the same cell, they stack up.\n4.When a cell is loaded with a number of orbs equal to its critical mass, the stack immediately explodes. As a result of the explosion, to each of the orthogonally adjacent cells, an orb is added and the initial cell looses as many orbs as its critical mass. The explosions might result in overloading of an adjacent cell and the chain reaction of explosion continues until every cell is stable.\n5.When a red cell explodes and there are green cells around, the green cells are converted to red and the other rules of explosions still follow. The same rule is applicable for other colors.\n6.The winner is the one who eliminates every other players orbs."
    mainmenu_frame.pack_forget()

    help_frame=tkinter.Frame(root,bg="black",width=width,height=height)
    help_frame.place(relheight=1,relwidth=1)


    label1=tkinter.Label(help_frame,padx="135",pady="50",text="Instructions",bg='black',fg='#ffffff')
    label1.config(font=("Courier",30))
    label1.pack()


    label2=tkinter.Label(help_frame,text=instruction,padx=50,pady=50,bg='black',fg='#ffffff',wraplength=width-100,justify="left")
    label2.config(font=("Courier",18))
    label2.pack()

    back_btn=tkinter.Button(help_frame,text="Back",anchor='s',command= init_page)
    back_btn.pack()

    root.protocol('WM_DELETE_WINDOW')
    root.mainloop()

def Exit1():
    Exit1 = tkinter.messagebox.askyesno("Chain Rection", "Are you sure")
    if Exit1 > 0:
        root.destroy()
    return

def new_game():
    global root
    root.destroy()
    import cgui2nd
    # init_page

def init_page():
    global root,mainmenu_frame,width,height
    try:
        root.destroy()
    except:
        pass
    root=tkinter.Tk()
    width = root.winfo_screenwidth()        #height of screen
    height = root.winfo_screenheight()      #width of screen
    print("height :",height,"\nwidth :",width)
    root.title("Client")
    print("height :", height, "\nwidth :", width)

    

    mainmenu_frame = tkinter.Frame(root,background="#25CCF7",width=width,height=height)
    mainmenu_frame.pack()



    canvas = tkinter.Canvas(mainmenu_frame, background="#25CCF7", width=width, height=height)
    canvas.pack()

    frame1 = tkinter.Frame(mainmenu_frame, bg='#25CCF7')
    frame1.place(x=0, y=height, relwidth=0.3, relheight=1, anchor="sw")

    frame2 = tkinter.Frame(mainmenu_frame, bg='#25CCF7')
    frame2.place(x=width,y=0, relwidth=0.3, relheight=.5, anchor="ne")

#---------------------------------------------- Storing image in a variable -------------------------------------------------------------

    chainreaction_image = Image.open("chainreaction.png")
    chainreaction_image = chainreaction_image.resize((int(.3 * width), int(.3 * height)), Image.ANTIALIAS)
    chainreaction_image = ImageTk.PhotoImage(chainreaction_image)
    #chainreaction_image = ImageTk.PhotoImage(image=Image.fromarray(chainreaction_image))'''

    #chainreaction_image=tkinter.PhotoImage(master=canvas,file="chainreaction.PPM")

    start_image = Image.open("start.png")
    start_image = start_image.resize((int(.15 * width), int(.10 * height)), Image.ANTIALIAS)
    start_image = ImageTk.PhotoImage(start_image)

    help_image = Image.open("help_final.png")
    help_image = help_image.resize((int(.15 * width), int(.10 * height)), Image.ANTIALIAS)
    help_image = ImageTk.PhotoImage(help_image)


    exit_image = Image.open("exit.png")
    exit_image = exit_image.resize((int(.15 * width), int(.10 * height)), Image.ANTIALIAS)
    exit_image = ImageTk.PhotoImage(exit_image)


#--------------------------------------------- Adding buttons and images --------------------------------------------------------

    chainreaction_logo = canvas.create_image(width / 2,height / 2 - .3 * height, image=chainreaction_image)


    start_button = tkinter.Button(frame1, image=start_image, bd=0, bg="#25CCF7", relief="raised", activebackground="#25CCF7",command=new_game)
    start_button.place(x=70, y=height - 310 - 86 - int(.10 * height))

    help_button = tkinter.Button(frame1, image=help_image, bd=0, bg="#25CCF7", relief="flat", activebackground="#25CCF7",command=help)
    help_button.place(x=70, y=height - 180 - 86 - int(.10 * height))

    exit_button = tkinter.Button(frame1, image=exit_image, bd=0, bg="#25CCF7", relief="raised", activebackground="#25CCF7",command=Exit1)
    exit_button.place(x=70, y=height - 50 - 86 - int(.10 * height))
    print(int(.10 * height))


    root.protocol('WM_DELETE_WINDOW',False)
    root.mainloop()
root = tkinter.Tk()
init_page()