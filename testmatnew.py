import matplotlib.pyplot as plt
# import matplotlib.axes as ax
import pandas as pd
import csv
import tkinter
import mysql.connector
import csv
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="MySQL@ver8",
  database="Chain_Reaction"
)


def skill_graph():
    df_skill = pd.read_csv("ChainReactionData.csv")
    dp_skill = pd.DataFrame
    df_skill = df_skill.sort_values(by='Skill_Level').groupby(["player_name"],sort=False)["Skill_Level"].max().head()

    dp_skill = df_skill.plot.bar(rot=0,width=0.3)
    #(kind="bar",figsize=(10,5),colormap="summer",width=0.3)

    dp_skill.set_xlabel("Names")
    dp_skill.set_ylabel("Skill level")
    plt.show()
# df.plot.bar(x="Names",y="Skills",rot=0)

def win_graph():
    df_win = pd.read_csv("ChainReactionData.csv")
    dp_win = pd.DataFrame
    df_win = df_win.groupby(["player_name"],sort=False)["wins"].max().head()

    dp_win = df_win.plot(kind="bar",figsize=(10,5),width=0.3)
    dp_win.set_xlabel("Names")
    dp_win.set_ylabel("Wins")
    plt.show()

# df.plot.bar(x="Names",y="Skills",rot=0)

def loss_graph():
    df_loss = pd.read_csv("ChainReactionData.csv")
    dp_loss = pd.DataFrame
    df_loss = df_loss.groupby(["player_name"],sort=False)["losses"].max().head()

    dp_loss = df_loss.plot(kind="bar",figsize=(10,5),width=0.3)
    dp_loss.set_xlabel("Names")
    dp_loss.set_ylabel("Losses")

# df.plot.bar(x="Names",y="Skills",rot=0)
    plt.show()
def moves_graph():
    plt.subplot(2,2,1)
    df_mmw = pd.read_csv("ChainReactionData.csv")
    dp_mmw = pd.DataFrame
    df_mmw = df_mmw.groupby(["player_name"],sort=False)["max_move_win"].max().head()

    dp_mmw = df_mmw.plot.bar(rot=0,figsize=(12,6),width=0.2)
    dp_mmw.set_xlabel("Names")
    dp_mmw.set_ylabel("Max moves win")

    plt.subplot(2,2,2)
    df_mml = pd.read_csv("ChainReactionData.csv")
    dp_mml = pd.DataFrame
    df_mml = df_mml.groupby(["player_name"],sort=False)["max_move_loss"].max().head()

    dp_mml = df_mml.plot.bar(rot=0,figsize=(12,6),width=0.2)
    dp_mml.set_xlabel("Names")
    dp_mml.set_ylabel("Max moves loss")

    plt.subplot(2,2,3)
    df_mimw = pd.read_csv("ChainReactionData.csv")
    dp_mimw = pd.DataFrame
    df_mimw = df_mimw.groupby(["player_name"],sort=False)["min_move_win"].max().head()

    dp_mimw = df_mimw.plot.bar(rot=0,figsize=(12,6),width=0.2)
    dp_mimw.set_xlabel("Names")
    dp_mimw.set_ylabel("Min moves win")

    plt.subplot(2,2,4)
    df_miml = pd.read_csv("ChainReactionData.csv")
    dp_miml = pd.DataFrame
    df_miml = df_miml.groupby(["player_name"],sort=False)["min_move_loss"].max().head()

    dp_miml = df_miml.plot.bar(rot=0,figsize=(12,6),width=0.2)
    dp_miml.set_xlabel("Names")
    dp_miml.set_ylabel("Min moves loss")

    plt.show()

def win_loss_graph():
    cur=mydb.cursor(buffered=True)
    cur.execute("select count(*) from players;")
    res=cur.fetchone()
    print(res)
    N=res[0]
    ind = np.arange(N)
    # plt.subplot(2,1,1)
    
    fig=plt.figure(figsize=(10,5))
    ax=fig.add_subplot(111)
    df_win = pd.read_csv("ChainReactionData.csv")
    dp_win = pd.DataFrame
    dp_win = df_win.groupby(["player_name"],sort=False)["wins"].max()
    print(dp_win)
    # dp_win = df_win.plot.bar(rot=0)
    # dp_win.set_xlabel("Names")
    # dp_win.set_ylabel("Win")

    # names = pd.read_csv("ChainReactionData.csv")
    # xAxis = [dp_win["player_name"]]
    # xaxis = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
    # print(xAxis)
    # xAxis = names["p_name"].drop_duplicates().values.tolist()
    # print(xAxis)
    # name = pd.DataFrame
    # name = names.groupby(["p_name"],sort=False)["win"].max()
    # print(name)
    # xAxis=[]
    # print(name["p_name"].values.tolist())
    
    df_loss = pd.read_csv("ChainReactionData.csv")
    dp_loss = pd.DataFrame
    dp_loss = df_loss.groupby(["player_name"],sort=False)["losses"].max()

    ax.axis([0,9,0,15])
    width=0.4
    bar1 = ax.bar(ind,dp_win,width,label='Win')
    #xAxis = list(map(lambda x: x+width,xAxis))
    bar2=ax.bar(ind+width,dp_loss,width,label='Loss')
    ax.axes.set_xticks(ind+width/2)
    ax.axes.set_xticklabels(df_loss["player_name"])
    #xAxis = list(map(lambda x: x+width,xAxis))
    # dp_loss = df_loss.plot.bar(rot=0)
    # dp_loss.set_xlabel("Names")
    # dp_loss.set_ylabel("Loss")

# df.plot.bar(x="Names",y="Skills",rot=0)
    plt.legend(loc=1)
    plt.show()

def get_name():
    import testret



root=tkinter.Tk()
width = root.winfo_screenwidth()        #height of screen
height = root.winfo_screenheight()      #width of screen
print("height :",height,"\nwidth :",width)
resolution=str(width)+"x"+str(height)
root.configure(background="cyan")
root.geometry(resolution)

df_stats = pd.read_csv("gamedata.csv")
print(df_stats.describe().transpose())
# col=['p_sl','win','loss']
# for i in col:
# 	avg=df_stats[i].max()
# 	print(df_stats[i])

skill_btn=tkinter.Button(root,text="Skills",command=skill_graph,bg="blue",fg="white",height=2,width=30,font=('8'))
skill_btn.place(x=width/2-150,y=100)

# win_btn=tkinter.Button(root,text="Wins",command=win_graph,bg="blue",fg="white",height=2,width=10,font=('8'))
# win_btn.place(x=width/2,y=300)

# loss_btn=tkinter.Button(root,text="Loss",command=loss_graph,bg="blue",fg="white",height=2,width=10,font=('8'))
# loss_btn.place(x=width/2,y=500)

moves_btn=tkinter.Button(root,text="Moves",command=moves_graph,bg="blue",fg="white",height=2,width=30,font=('8'))
moves_btn.place(x=width/2-150,y=500)

win_btn=tkinter.Button(root,text="Total wins and losses",command=win_loss_graph,bg="blue",fg="white",height=2,width=30,font=('8'))
win_btn.place(x=width/2-150,y=300)

ip_btn=tkinter.Button(root,text="Player",command=get_name,bg="blue",fg="white",height=2,width=30,font=('8'))
ip_btn.place(x=width/2-150,y=700)

root.protocol('WM_DELETE_WINDOW')

cursor = mydb.cursor(buffered=True)    
cursor.execute("select * from players")
with open("ChainReactionData.csv", "w", newline='') as csv_file:
  csv_writer = csv.writer(csv_file)
  csv_writer.writerow([i[0] for i in cursor.description]) # write headers
  csv_writer.writerows(cursor)

root.mainloop()





# for i in range(1, 7):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)),
#              fontsize=18, ha='center')
# plt.show()





#xAxis = [i+1 for i, _ in enumerate(country_names)]
# xAxis=[]
# for i in range(len(country_names)):
#     xAxis.append(i+1)



# print(xAxis)




# plt.axis([0,5,0,150])
# width=0.2
# plt.bar(xAxis,gold_medals,width,label='GOLD MEDALS')
# xAxis = list(map(lambda x: x+width,xAxis))
# plt.bar(xAxis,silver_medals,width,label='SILVER MEDALS')
# xAxis = list(map(lambda x: x+width,xAxis))
# plt.bar(xAxis,bronze_medals,width,label='BRONZE MEDALS')
# plt.legend(loc=1)
# plt.show()

# nvalues=[' ','na','--','NA']
# df=pd.read_csv("sepm.csv")
# print(df)

# print(df.isnull().sum())
# print(df['total_bill'].isnull())

# col=['total_bill','ratings']
# for i in col:
# 	avg=df[i].mean()
# 	df[i].fillna(avg,inplace=True)


# df['email'].fillna('-',inplace=True)
# df['mobile'].fillna(0,inplace=True)	

# df.dropna(axis=0,how='any',thresh=int(df.shape[0]*0.5),subset=None)

# print(df)