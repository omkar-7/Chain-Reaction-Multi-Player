import mysql.connector
import time
import datetime

mydb=None
a=1.5
b=1.25
c=0.5
d=1
e=0.75
f=0.85

def connect_db():
    global mydb
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MySQL@ver8",
        database="Chain_Reaction"
    )

def Insert_new(p_name,moves,Win):
    global mydb
    mycursor=mydb.cursor(buffered=True)
    global a,b,c,d,e,f
    win_prob=Win
    Loss=0
    max_moves_win,min_moves_win,avg_moves_win,avg_moves_loss,max_moves_loss,min_moves_loss=0,0,0,0,0,0
    wp=-1
    if Win==1:
        avg_moves_win=moves
        max_moves_win=moves
        min_moves_win=moves
        wp=1.000
    else:
        Loss=1
        wp=0.000
        avg_moves_loss=moves
        max_moves_loss=moves
        min_moves_loss=moves

    skill_level=(a+(min_moves_win*b)+(max_moves_win*c))-((Loss*d)+(e*min_moves_loss)+(max_moves_loss*f))

    if skill_level<0:
        skill_level=0
    sql="Insert into Players (player_name,games_played,wins,losses,max_move_win,max_move_loss,min_move_win,min_move_loss,avg_move_win,avg_move_loss,Skill_Level,Win_Prob) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(p_name,1,Win,Loss,max_moves_win,max_moves_loss,min_moves_win,min_moves_loss,avg_moves_win,avg_moves_loss,skill_level,wp)
    mycursor.execute(sql,val)
    print(mycursor.rowcount,"records inserted.")
    mydb.commit()


def Update_tables(p_name,moves,Win):
    global a,b,c,d,e,f,mydb
    mycursor=mydb.cursor(buffered=True)
    mycursor.execute("select wins,losses,Win_Prob,games_played,max_move_win,min_move_win,avg_move_win,avg_move_loss,max_move_loss,min_move_loss from Players where player_name = %s",(p_name,))
    res=mycursor.fetchone()
    (Wins,Losses,win_prob,games_pld,max_moves_win,min_moves_win,avg_moves_win,avg_moves_loss,max_moves_loss,min_moves_loss)=res
    win_prob=((win_prob*games_pld)+Win)/(games_pld+1)       #win prob calculation
    
    if Win==1:
        if moves>max_moves_win:
            max_moves_win=moves
        if moves<min_moves_win or min_moves_win==0:
            min_moves_win=moves
        Wins+=1
    else:
        if moves > max_moves_loss:
            max_moves_loss=moves

        if moves < min_moves_loss or min_moves_loss==0:
            min_moves_loss=moves
        Losses+=1

    if Win:
        avg_moves_win=((avg_moves_win*games_pld)+moves)/(games_pld+1)
    else:
        avg_moves_loss=((avg_moves_loss*games_pld)+moves)/(games_pld+1)

    if Win==1:
        skill_level=((Wins*a)+(min_moves_win*b)+(max_moves_win*c))+3-((Losses*d)+(e*min_moves_loss)+(f*max_moves_loss))
    else:
        skill_level=((Wins*a)+(min_moves_win*b)+(max_moves_win*c))-3-((Losses*d)+(e*min_moves_loss)+(f*max_moves_loss))
        
    if skill_level<0:
        skill_level=0
    sql="Update Players set games_played=%s,wins=%s,losses=%s,max_move_win=%s,max_move_loss=%s,min_move_win=%s,min_move_loss=%s,avg_move_win=%s,avg_move_loss=%s,Skill_Level=%s,Win_Prob=%s where player_name=%s"
    val=(games_pld+1,Wins,Losses,max_moves_win,max_moves_loss,min_moves_win,min_moves_loss,avg_moves_win,avg_moves_loss,skill_level,win_prob,p_name)
    mycursor.execute(sql,val)
    print(mycursor.rowcount,"records updated.")
    mydb.commit()

def update_database(p_name,moves,win):
    global mydb
    mycursor=mydb.cursor(buffered=True)
    sql="Select player_name from Players where player_name=%s"
    val=p_name
    mycursor.execute(sql,(val,))
    print(mycursor.rowcount,"records found")
    if mycursor.rowcount==0:
        Insert_new(p_name,moves,win)
    else:
        Update_tables(p_name,moves,win)

def insert_all(p_name,Win,n):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    global mydb
    mycursor=mydb.cursor(buffered=True)
    Loss=0
    if Win==1:
        Loss=0
    else:
        Loss=1
    sql="Insert into Games (player_name,Date_,win,loss,num_of_players) values(%s,%s,%s,%s,%s)"
    val=(p_name,timestamp,Win,Loss,n)
    mycursor.execute(sql,val)
    print(mycursor.rowcount,"records inserted.")
    mydb.commit()

# connect_db()
# update_database("Omkar",12,0)
# insert_all("Omkar",1,3)
# insert_all("SUBHRADEEP",0,3)
# insert_all("ShohaibM",0,3)
