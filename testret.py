import tkinter
import tkinter.messagebox
import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="MySQL@ver8",
  database="Chain_Reaction"
)

root = tkinter.Tk()
root.geometry("1250x500+200+200")
root.configure(background="cyan")
name_entry=name_frame=loss_frame=win_frame=skill_frame=None 

def getname():
  global name_entry
  global name_frame
  loss_frame = tkinter.Frame(root)
  loss_frame.place_forget()
  loss_frame = tkinter.Frame(root)
  loss_frame.place_forget()
  skill_frame = tkinter.Frame(root)
  skill_frame.place_forget()
  win_frame = tkinter.Frame(root)
  win_frame.place_forget()
  while(True):
    find_name = name_entry.get()
    if find_name.isalpha():
      break
    else:
      tkinter.messagebox.showwarning("Invalid entry")
      getname()
  mycursor = mydb.cursor(buffered=True)
  sql="SELECT Skill_Level,Wins,Losses FROM players where player_name=%s"
  val=(find_name,)
  mycursor.execute(sql,val)
  myresult = mycursor.fetchone()
  print(myresult)
  # print("Player id =",myresult[0])
  # pid=str(myresult[0])
  skill=str(myresult[0])
  win=str(myresult[1])
  loss=str(myresult[2])
  name_frame = tkinter.Frame(root)
  name_frame.place(x=150,y=200)
  label3=tkinter.Label(name_frame,text="\nPlayer skill level="+skill+"\nPlayer totalwins="+win+"\nPlayer total losses="+loss,background="pink",justify="center")
  label3.config(font=("Comic Sans MS",18))
  label3.pack()

    
def getskill():
  global skill_frame
  name_frame = tkinter.Frame(root)
  name_frame.place_forget()
  win_frame = tkinter.Frame(root)
  win_frame.place_forget()
  loss_frame = tkinter.Frame(root)
  loss_frame.place_forget()
  mycursor = mydb.cursor(buffered=True)
  mycursor.execute("SELECT player_name,Skill_Level from players order by Skill_Level desc limit 3")
  myresult = mycursor.fetchall()
  skill_frame = tkinter.Frame(root,background="pink")
  skill_frame.place(x=475,y=200)
  for x in myresult:
    label3=tkinter.Label(skill_frame,text=x,background="pink",justify="center")
    # label3.config(text=("\n".join(str.split(repr(x)))))
    label3.config(font=("Comic Sans MS",18))
    label3.pack()

  # pskill = str(myresult[1])
  # print(pskill[1])
def getwin():
  global win_frame
  name_frame = tkinter.Frame(root)
  name_frame.place_forget()
  skill_frame = tkinter.Frame(root)
  skill_frame.place_forget()
  loss_frame = tkinter.Frame(root)
  loss_frame.place_forget()
  mycursor = mydb.cursor(buffered=True)
  mycursor.execute("SELECT player_name,wins from players order by wins desc limit 3")
  myresult = mycursor.fetchall()
  win_frame = tkinter.Frame(root,background="pink")
  win_frame.place(x=725,y=200)
  for x in myresult:
    label3=tkinter.Label(win_frame,text=x,background="pink",justify="center")
    # label3.config(text=("\n".join(str.split(repr(x)))))
    label3.config(font=("Comic Sans MS",18))
    label3.pack()

def getloss():
  global loss_frame
  name_frame = tkinter.Frame(root)
  name_frame.place_forget()
  skill_frame = tkinter.Frame(root)
  skill_frame.place_forget()
  win_frame = tkinter.Frame(root)
  win_frame.place_forget()
  mycursor = mydb.cursor(buffered=True)
  mycursor.execute("SELECT player_name,losses from players order by losses desc limit 3")
  myresult = mycursor.fetchall()
  loss_frame = tkinter.Frame(root,background="pink")
  loss_frame.place(x=975,y=200)
  for x in myresult:
    label3=tkinter.Label(loss_frame,text=x,background="pink",justify="center")
    # label3.config(text=("\n".join(str.split(repr(x)))))
    label3.config(font=("Comic Sans MS",18))
    label3.pack()

def inputName(message):
  name=message.lower()
  if name.isalpha():
    return 1
  else:
    tkinter.messagebox.showinfo("Invalid entry")
    return 0  

label1=tkinter.Label(root,text="ENTER NAME",background="pink",justify="center")
label1.config(font=("Comic Sans MS",12))
label1.place(x=225,y=0)
# cursor = mydb.cursor()    
# cursor.execute("select * from gameset")
# with open("trial.csv", "w", newline='') as csv_file:
#   csv_writer = csv.writer(csv_file)
#   csv_writer.writerow([i[0] for i in cursor.description]) # write headers
#   csv_writer.writerows(cursor)
name_entry=tkinter.Entry(root,bd=2,width=30,justify="center")
name_entry.config(font=("",12))
name_entry.place(x=150,y=20)
button1=tkinter.Button(root,text="GO",background="#45CE30",command=getname)
button1.config(font=(12))
button1.place(x=250,y=50)
skill_but=tkinter.Button(root,text="Skills",background="#45CE30",command=getskill)
skill_but.config(font=(12))
skill_but.place(x=500,y=50)
win_but=tkinter.Button(root,text="Wins",background="#45CE30",command=getwin)
win_but.config(font=(12))
win_but.place(x=750,y=50)
loss_but=tkinter.Button(root,text="Losses",background="#45CE30",command=getloss)
loss_but.config(font=(12))
loss_but.place(x=1000,y=50)
