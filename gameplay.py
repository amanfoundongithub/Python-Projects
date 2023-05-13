#Import required modules 
import tkinter
import random
import math
import time
import smtplib
import mysql.connector
import sqlite3
from tkinter import ttk
from tkinter import messagebox
''' Launch a Python window'''
main=tkinter.Tk()

main.geometry("1000x1000")
main.title("Gaming Panel")
main.configure(bg="white")
main.attributes('-fullscreen',True)



mf=tkinter.Frame(main)
mf.pack(fill= 'both',expand=1)

mycan=tkinter.Canvas(mf)
mycan.pack(side= 'left',fill='both',expand=1)
mycan.configure(bg='white')

sc=ttk.Scrollbar(mf,orient= 'vertical',command=mycan.yview)
sc.pack(side= 'right',fill= 'y')


mycan.configure(yscrollcommand=sc.set)
mycan.bind('<Configure>', lambda e: mycan.configure(scrollregion=mycan.bbox('all')))

fra=tkinter.Frame(mycan)
mycan.create_window((0,0),window=fra,anchor='nw')
fra.configure(bg='white')

tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=0,column=1)
tkinter.Label(fra,text="Welcome To The Gaming Panel!!!",font=("Times",'20','bold'),bg="white",fg="black",anchor='e').grid(row=1,column=2)
tkinter.Label(fra,text="The Current Time in IST is :-",font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=3,column=1)
timer1=tkinter.Label(fra,text="  ",font=("Times",'16','bold'),bg="white",fg="black",anchor='e')
timer1.grid(row=3,column=2)
tkinter.Label(fra,text="HANGMAN Game:-Fees is 20 GCs and winner will get 25 GCs.",font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=11,column=1)
tkinter.Label(fra,text="Click Here To Create An Account :-",font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=5,column=1)
tkinter.Label(fra,text="Click Here To Recharge Your Account :-",font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=7,column=1)
tkinter.Label(fra,text="Click Here To Check Money in Your Account :-",font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=9,column=1)
tkinter.Label(fra,text="Color Game:-Fees is 20 GCs and winner will get 2 GCs per point earned. "
              ,font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=13,column=1)
tkinter.Label(fra,text="SPS: Fees is 20 GCs and Winner will get 4 GCs per point earned."
              ,font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=15,column=1)
tkinter.Label(fra,text="War Game: Fees is 20 GCs and winner will get 40 GCs. If draw, then 10 GCs are given."
              ,font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=17,column=1)
tkinter.Label(fra,text="Bulls and Cows: Fees is 20 GCs and winner will get 30 GCs."
              ,font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=21,column=1)
tkinter.Label(fra,text="Have Any Complaints/Compliments? Send Us A Feedback:",font=("Times",'16','bold'),bg="white",fg="black",anchor='e').grid(row=23,column=1)
lst=['expense','neutral','auspicious','cachet'
     ,'ambivalent','helmet','omnipotent','deformed','logarithm','calculus','velocity'
     ,'advisory','gambling','documentary','altruism']
mt=''
tkinter.Label(fra,text=" ",font=("Times",'16','bold'),bg="white",fg="red",anchor='e').grid(row=4,column=2)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=6,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=8,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=10,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=12,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=14,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=16,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=18,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=20,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=22,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=24,column=1)
tkinter.Label(fra,text=" ",font=("Times",'13','bold'),bg="white",fg="red",anchor='e').grid(row=26,column=1)
def ShuTime():
         x=time.strftime("%H:%M:%S %p")
         timer1.configure(text=x)
         main.after(1000,ShuTime)
ShuTime()
         
def AboutProg():
         #Make a new window tell the rules!!
         re=tkinter.Tk()
         re.geometry("1000x1000")
         re.title("About This Platform")
         re.configure(bg="yellow")
         re.attributes('-fullscreen',True)
         tkinter.Label(re,text="Welcome To The Official Rules of Gaming PANEL!",fg="black",bg="yellow",font="Times").pack()
         tkinter.Label(re,text="1. You MUST have an account on this panel. This can be made from 'Account Creation' Button."
                       ,fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Label(re,text="2. Registered users need not to register again. They can go to play games directly.",fg="black",bg="yellow",font="Times").pack()
         tkinter.Label(re,text="3. All transactions in this game are carried out in terms of Gaming Currency/GCs.These can be recharged easily."
                       ,fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Label(re
                       ,text="4. To recharge, you need real cash. Packs will be displayed during recharging. You will get an 6-digit OTP from the cash counter,"
                       ,fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Label(re,text="which will be used for authentication. ",fg="black",bg="yellow",font="Times").pack()
         tkinter.Label(re
                       ,text="5. After each login into the game, GCs will be deducted from your account,whether you complete the game or not."
                       ,fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Label(re,text="6. Winning a game will give you some GCs in your account.",fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Label(re,text="7. You can also check your account by clicking on 'MY ACCOUNT' page.",fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Label(re,text="8. ENJOY!!!",fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Label(re,text="THANK YOU!!!",fg="black",bg="yellow",font=("Times",'16')).pack()
         tkinter.Button(re,text="EXIT THIS PAGE",bg="green",fg="black",activebackground="green",command=re.destroy,font=("Times",'16')).pack()


def CreatAccount():
         c=tkinter.Tk()
         c.title("ACCOUNT CREATION SYSTEM")
         c.configure(bg="yellow")
         c.geometry("500x500")
         c.attributes('-fullscreen',True)
         tkinter.Label(c,text="OFFICIAL GAMEPLAY ACCOUNT CREATION",font=("Times",'20'),bg="yellow",fg="red").grid(row=0,column=2)
         tkinter.Label(c,text="Enter your details below to continue:",font=("Times",'20'),bg="yellow",fg="black").grid(row=2,column=2)
         tkinter.Label(c,text="Your UserID (only small caps alphabets):",font=("Times",'20'),bg="yellow",fg="black").grid(row=4,column=1)
         tkinter.Label(c,text="Set your Password:",font=("Times",'20'),bg="yellow",fg="black").grid(row=5,column=1)
         tkinter.Label(c,text="NOTE: After creation,you will get GC60.00 as a starting amount!",font=("Times",'20'),bg="yellow",fg="black").grid(row=6,column=2)
         y9=tkinter.Label(c,text=" ",font=("Times",'20'),bg="yellow",fg="black")
         y9.grid(row=8,column=2)
         x1=tkinter.Entry(c,bg="yellow",fg="black",font=("Times",'20'))
         x1.grid(row=4,column=2)
         x2=tkinter.Entry(c,bg="yellow",fg="black",font=("Times",'20'))
         x2.grid(row=5,column=2)
         def CreaAcc():
                           m.grid_forget()
                           n.grid_forget()
                           x1t=str(x1.get())
                           x2t=str(x2.get())
                           #my=sqlite3.connect("record.db")
                           my=sqlite3.connect("record.db")
                           mycursor=my.cursor()
                           mycursor.execute("select * from money")
                           amit=mycursor.fetchall()
                           f=False
                           for i in amit:
                                    if(str(i[1])==x1t and str(i[0])==x2t):
                                             y9.configure(text="AN ACCOUNT ALREADY EXISTS! Please Try Something Different!",font=("Times",'20'))
                                             m.grid(row=10,column=2)
                                             n.grid(row=12,column=2)
                                             my.close()
                                             f=True
                                             break
                                             
                                    elif(str(i[0])==x2t and str(i[1])!= x1t):
                                             y9.configure(text="Please select a different password",font=("Times",'20'))
                                             m.grid(row=10,column=2)
                                             n.grid(row=12,column=2)
                                             my.close()
                                             f=True
                                             break
                           
                                    elif(str(i[1])==x1t and str(i[0])!= x2t):
                                             y9.configure(text="Please select a different USERID",font=("Times",'20'))
                                             m.grid(row=10,column=2)
                                             n.grid(row=12,column=2)
                                             my.close()
                                             f=True 
                                             break 

                           if(f==False):
                                             s="Insert into money(ID,Username,amt) values('"+str(x2t)+"','"+str(x1t)+"',60);"
                                             mycursor.execute(s)
                                             my.commit()
                                             my.close()
                                             def Editor():
                                                      
                                                      y9.configure(text="Your Account Has Been Successfully Created!",font=("Times",'20'))
                                                      n.grid(row=12,column=2)
                                                      c.destroy()
                                             c.after(1000,Editor)

                                             
                                       
                                       
                           
                  
         m=tkinter.Button(c,text="CREATE ACCOUNT",font=("Times",'20'),bg="yellow",fg="black",command=CreaAcc)
         m.grid(row=10,column=2)
         n=tkinter.Button(c,text="EXIT THIS PAGE",font=("Times",'20'),bg="yellow",fg="black",command=c.destroy)
         n.grid(row=12,column=2)

def CandidateLogin():
         log=tkinter.Tk()
         log.title("ACCESS WINDOW")
         log.geometry("400x400")
         log.configure(bg="yellow")
         log.attributes('-fullscreen',True)
         tkinter.Label(log,text="     ",bg="yellow",fg="black",font="Times").grid(row=1,column=0)
         tkinter.Label(log,text="Welcome To The LOGIN Menu!",bg="yellow",fg="black",font=("Times",'20')).grid(row=1,column=2)
         mi=tkinter.Label(log,text="Before Starting, Please Login With Your UserID and Password",bg="yellow",fg="black",font=("Times",'20'))
         mi.grid(row=2,column=2)
         ml=tkinter.Label(log,text="Enter Your UserID:",bg="yellow",fg="black",font=("Times",'20'))
         ml.grid(row=3,column=1)
         mk=tkinter.Label(log,text="Enter Your Password:",bg="yellow",fg="black",font=("Times",'20'))
         mk.grid(row=4,column=1)
         e45=tkinter.Label(log,text="  ",bg="yellow",fg="black",font="Times")
         e45.grid(row=5,column=2)
         userid=tkinter.Entry(log,font=('Times','20'),fg='black')
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(log,font=('Times','20'),fg='red')
         passwd.grid(row=4,column=2)
         def Opener():
                  tkinter.Label(log,text="     ",bg="yellow",fg="black",font="Times").grid(row=1,column=1)
                  mt=str(userid.get())
                  e45.configure(text=' ')
                  mi.configure(text="Authentication Successful!!!",font=('Times','20'),anchor='e')
                  menuo="Your UserID is:  "+str(mt)
                  ml.configure(text=menuo,font=('Times','20'))
                  ml.grid(row=3,column=2)
                  userid.destroy()
                  passwd.destroy()
                  mk.destroy()
                  ml2=tkinter.Label(log,text=" ",bg="yellow",fg="black",font=('Times','20'))
                  ml2.grid(row=4,column=2)
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[1]==mt):
                                    s="Your Account has currently "+str(i[2])+" GCs left currently."
                                    ml2.configure(text=s)
                                    ml3=tkinter.Button(log,text="EXIT THIS PAGE",bg="red",fg="black",font=('Times','20'),activebackground='red',command=log.destroy)
                                    ml3.grid(row=6,column=2)
                                    
                                    
                  
                  
         
         def Akcess():
                  #pROGRAM WILL TAKE THE INPUT AND CHECK ITS VALIDITY!
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x38.destroy()
                                    x389.grid_forget()
                                    e45.configure(text="Access Granted! Please wait...",font=('Times','20'))
                                    myc.close()
                                    log.after(2000,Opener)
                                    f3=True 
                           
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!",font=('Times','20'))

         x38=tkinter.Button(log,text="LOGIN",fg="black",activebackground="green",bg="green",font=('Times','20'),command=Akcess)
         x38.grid(row=6,column=2)
         tkinter.Label(log,text="      ",bg="yellow",fg="black",font="Times").grid(row=7,column=2)
         x389=tkinter.Button(log,text="EXIT",fg="black",activebackground="red",bg="red",font=('Times','20'),command=log.destroy)
         x389.grid(row=8,column=2)
         
                  


def Hangmangame():
         mn=tkinter.Tk()
         mn.configure(bg="yellow")
         mn.geometry("1000x1000")
         mn.attributes('-fullscreen',True)
         mn.attributes('-topmost',True)
         mn.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(mn,text="Welcome to the ACCESS Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(mn,text="Before starting, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(mn,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(mn,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(mn,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(mn,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(mn,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
         
         def Hangmaan():           
                  mn.destroy()
                  global lst 
                  mw=tkinter.Tk()
                  mw.title("HANGMAN GAME")
                  mw.configure(bg="white")
                  mw.geometry("1000x1000")
                  mw.attributes('-fullscreen',True)
                  mw.attributes('-topmost',True)
                  tkinter.Label(mw,text="THE CLASSICAL HANGMAN GAME!",font=("Times",'15','bold'),fg="black",bg="white",anchor='e').grid(row=0,column=1)
                  tkinter.Label(mw,text="   ",font=("Times",'15','bold'),fg="black",bg="white",anchor='e').grid(row=2,column=0)
                  tkinter.Label(mw,text="Your Progress So Far:",font=("Times",'15','bold'),fg="black",bg="white",anchor='e').grid(row=4,column=0)
                  #Make a list of variables 
                  n=5
                  em1=random.randint(0,len(lst)-1)
                  exy=lst[em1]
                  n3=len(exy)
                  x="- "*n3
                  y=tkinter.Label(mw,text=x,font=("Times",'15','bold'),fg="black",bg="white",anchor='e')
                  y.grid(row=4,column=1)
                  tkinter.Label(mw,text="Number Of Turns Left:",font=("Times",'15','bold'),fg="black",bg="white",anchor='e').grid(row=6,column=0)
                  #Make the label! 
                  mert=tkinter.Label(mw,text=str(n),font=("Times",'15','bold'),fg="black",bg="white",anchor='e')
                  mert.grid(row=6,column=1)
         
                  tkinter.Label(mw,text="Enter Only One Alphabet Here:",font=("Times",'15','bold'),fg="black",bg="white",anchor='e').grid(row=8,column=0)
                  x1=tkinter.Entry(mw,font="Times",fg="red",bg="yellow")
                  x1.grid(row=8,column=1)
                  #Make a winner label/loser label
                  winer=tkinter.Label(mw,text="     ",font=("Times",'15','bold'),fg="black",bg="white",anchor='e')
                  winer.grid(row=14,column=1)
                  #A list and a number to check what we have done so far! 
                  n=5
                  lsti=[]
                  for i in range(0,len(exy)):
                           
                           lsti.append('- ')
                  #List is easy to change
                  def Checkis():
                           
                           nonlocal n
                           nonlocal lsti
                           cur=''
                           p=str(x1.get())
                           s=''
                           for l in p:
                                    
                                    if(l.isalpha()==True):
                                             
                                             s=s+l
                           x1.delete(0,tkinter.END)
                           
                  #Check wether the number of turns is more than zero or not. if it is?
                           f=False
                           if(n>0):
                                    
                                    for i in range(0,len(exy)):
                                             
                                             if(str(exy[i])==s):
                                                      
                                                      m=s
                                                      f=True
                                                      lsti[i]=m+" "
                                             else:
                                                      
                                                      pass
                                    
                                    for i2 in range(0,len(lsti)):
                                             
                                             cur=cur+str(lsti[i2])

                                    if(str(cur)==str(exy)):
                                             y.configure(text=cur)
                                             winer.configure(text="YOU HAVE WON THIS GAME!!! 20.00 GCs has been credited to your gaming account!")
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             myr.execute("update money set amt=amt+25 where username='"+str(mt)+"';")
                                             myc.commit()
                                             myc.close()
                                             button1.grid_forget()
                                             button2.grid_forget()
                                             mw.after(4000,mw.destroy)
                                    else:
                                             y.configure(text=cur)

                                    if(f==False):
                                             n=n-1
                                             mert.configure(text=str(n))
                                             
                           if(n==0):
                                    s="You have lost this game! The correct word was:"+str(exy)+"! The window will be deleted shortly..."
                                    button1.grid_forget()
                                    winer.configure(text=s)
                                    mw.after(5000,mw.destroy)

                  button1=tkinter.Button(mw,text="CHECK",font=("Times",'15','bold'),fg="black",bg="white",anchor='e',command=Checkis)
                  button1.grid(row=10,column=1)
                  button2=tkinter.Button(mw,text="DELETE",font=("Times",'15','bold'),fg="black",bg="red",anchor='e',command=mw.destroy)
                  button2.grid(row=12,column=1)
                  
         def Akcess():
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x=str(i[2])
                                    x=str(x)
                                    x=int(x)
                                    f3=True 
                                    if(x>=20):
                                             x38.grid_forget()
                                             e45.configure(text="Access Granted! Please wait...")
                                             myr.execute("update money set amt=amt-20 where ID='"+str(i[0])+"';")
                                             myc.commit()
                                             myc.close()
                                             mn.after(1000,Hangmaan)
                                    else:
                                             e45.configure(text="NOT ENOUGH BALANCE LEFT! PLEASE RECHARGE!")
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")
                                    

         x38=tkinter.Button(mn,text="LOGIN",fg="black",activebackground="blue",bg="blue",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(mn,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=mn.destroy)
         x389.grid(row=8,column=2)
def Rechagres():
         #Make a window that will accept the recharging condition!!
         rechr=tkinter.Tk()
         rechr.configure(bg="yellow")
         rechr.geometry("1000x1000")
         rechr.attributes('-fullscreen',False)
         rechr.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(rechr,text="Welcome to the Recharge Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(rechr,text="Before recharge, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(rechr,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(rechr,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(rechr,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(rechr,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(rechr,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
         def Recharging():
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  login1.destroy()
                  login2.destroy()
                  userid.destroy()
                  passwd.destroy()
                 # make a new system that will accept net banking 
                  lune.configure(text="You have successfully registered in the system!")
                  merid="Your Unique UserID is: "+str(mt)+"."
                  login3=tkinter.Label(rechr,text=merid,font=("Times",'20'),bg="yellow",fg="black")
                  login3.grid(row=3,column=2)
                  login4=tkinter.Label(rechr,text="To recharge your GCs, please choose a PLAN from following list:",font=("Times",'20'),bg="yellow",fg="black")
                  login4.grid(row=4,column=2)
                  login5=tkinter.Label(rechr,text="PLAN A:- Get 20 GCs at INR 50.00",font=("Times",'20'),bg="yellow",fg="black")
                  login5.grid(row=5,column=2)
                  login6=tkinter.Label(rechr,text="PLAN B:- Get 40 GCs at INR 90.00",font=("Times",'20'),bg="yellow",fg="black")
                  login6.grid(row=6,column=2)
                  login7=tkinter.Label(rechr,text="PLAN C:- Get 60 GCs at INR 125.00",font=("Times",'20'),bg="yellow",fg="black")
                  login7.grid(row=7,column=2)
                  login8=tkinter.Label(rechr,text="PLAN D:- Get 100 GCs at INR 200.00",font=("Times",'20'),bg="yellow",fg="black")
                  login8.grid(row=8,column=2)
                  login9=tkinter.Label(rechr,text="Please select a plan (A,B,C or D):",font=("Times",'20'),bg="yellow",fg="black")
                  login9.grid(row=9,column=1)
                  login10=tkinter.Entry(rechr,font=("Times",'20'),bg="yellow",fg="black")
                  login10.grid(row=9,column=2)
                  login11=tkinter.Label(rechr,text=" ",font=("Times",'20'),bg="yellow",fg="black")
                  login11.grid(row=13,column=2)
                  login12=tkinter.Label(rechr,text=" ",font=("Times",'20'),bg="yellow",fg="black")
                  login12.grid(row=14,column=2)
                  def Processing():
                           #OTP payment will be done securely! Come to me for otp!
                           x=str(login10.get())
                           if(x=='A'or x=='a' or x=='B' or x=='b' or x=='C' or x=='c' or x=='D' or x=='d'):
                                    buttonsubmit.grid_forget()
                                    login11.configure(text="Your Plan has been successfully registered!")
                                    login12.configure(text="Please go to cash counter and pay the required money. A 6 digit OTP will be given to you!")
                                    n1=random.randint(100001,999998)
                                    s=smtplib.SMTP('smtp.gmail.com',587)
                                    s.starttls()
                                    s.login('dummyaman2004@gmail.com','eahk zxeg kwiy gvuc')
                                    otps='Your Login OTP is '+str(n1)
                                    s.sendmail('&&&&&&&&&&&','amanrajmathematics@gmail.com',otps)
                                    s.quit()
                                    login13=tkinter.Label(rechr,text="Please Enter the OTP here carefully:",font=("Times",'20'),bg="yellow",fg="black")
                                    login13.grid(row=15,column=1)
                                    login14=tkinter.Entry(rechr,font=("Times",'20'),bg="yellow",fg="black")
                                    login14.grid(row=15,column=2)
                                    login15=tkinter.Label(rechr,text=" ",font=("Times",'20'),bg="yellow",fg="black")
                                    login15.grid(row=16,column=2)
                                    def Feeder():
                                             try:
                                                      x321=str(login14.get())
                                                      x321=int(x321)
                                                      if(x321==n1):
                                                               button1923.grid_forget()
                                                               button1925.grid_forget()
                                                               login15.configure(text="Your transaction is successful. Window will close shortly...")
                                                               p=0
                                                               if(x=='a' or x=='A'):
                                                                        p=20
                                                               if(x=='b' or x=='B'):
                                                                        p=40
                                                               if(x=='c' or x=='C'):
                                                                        p=60
                                                               if(x=='d' or x=='D'):
                                                                        p=100
                                                                        
                                                               myc=sqlite3.connect("record.db")
                                                               myr=myc.cursor()
                                                               s="update money set amt=amt+"+str(p)+" where id='"+str(pw)+"';"
                                                               myr.execute(s)
                                                               myc.commit()
                                                               myc.close()
                                                               rechr.after(4000,rechr.destroy)
                                                               
                                                      else:
                                                               login15.configure(text='INCORRECT OTP!! PAYMENT CANCELLED...',fg="red")
                                                               rechr.after(2000,rechr.destroy)
                                                                   
                                                               

                                             except ValueError:
                                                      login15.configure(text="INVALID OTP!!! Window will close shortly...",fg="red")
                                                      rechr.after(2000,rechr.destroy)
                                             
                                    
                                                      
                                    button1923=tkinter.Button(rechr,text="CONFIRM",fg="black",bg="green",activebackground="green",font=("Times",'20'),command=Feeder)
                                    button1923.grid(row=18,column=2)
                                    button1925=tkinter.Button(rechr,text="EXIT ",fg="black",bg="red",activebackground="red",font=("Times",'20'),command=rechr.destroy)
                                    button1925.grid(row=19,column=2)

                           else:
                                    
                                   login11.configure(text="PLEASE ENTER A VALID ALPHABET!!!",fg='red')
                                    
                  buttonsubmit=tkinter.Button(rechr,text="CONFIRM and Pay",fg="black",bg="green",activebackground="green",font=("Times",'20'),command=Processing)
                  buttonsubmit.grid(row=11,column=2)      
                  buttonsubmitleft=tkinter.Button(rechr,text="EXIT",fg="green",bg="blue",activebackground="blue",font=("Times",'20'),command=rechr.destroy)
                  buttonsubmit.grid(row=20,column=2)
                  
         def Akcess():
                  #pROGRAM WILL TAKE THE INPUT AND CHECK ITS VALIDITY!
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x38.destroy()
                                    x389.grid_forget()
                                    e45.configure(text="Access Granted! Please wait...")
                                    myc.close()
                                    rechr.after(2000,Recharging)
                                    f3=True 
                           
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")

         x38=tkinter.Button(rechr,text="LOGIN",fg="black",activebackground="green",bg="green",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(rechr,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=rechr.destroy)
         x389.grid(row=8,column=2)

def ColorGame():
         mn=tkinter.Tk()
         mn.configure(bg="yellow")
         mn.geometry("1000x1000")
         mn.attributes('-fullscreen',True)
         mn.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(mn,text="Welcome to the ACCESS Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(mn,text="Before starting, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(mn,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(mn,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(mn,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(mn,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(mn,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
         def GamLoader():
                  pw=str(passwd.get())
                  mn.destroy()
                  colours = ['Red','Blue','Green','Black',
                             'Yellow','Purple','Brown']
                  score1 = 0
                  timelft = 60
                  def countdown():
                           enterhere.configure(text="After writing,Press ENTER:-",anchor='e')
                           nonlocal timelft
                           nonlocal score1
                           nonlocal pw
                           if timelft > 0:
                                    timelft -= 1
                                    timeLabel.config(text = "Time left: "+ str(timelft))      
                                    timeLabel.after(1000, countdown)

                           if(timelft==0):
                                    e.destroy()
                                    exitas.grid_forget()
                                    timeLabel.configure(text="Your Total Score is:"+str(score1))
                                    thams.configure(text="THANK YOU!!!")
                                    label.configure(text=" ")
                                    scoreLabel.configure(text=' ')
                                    enterhere.configure(text= '')
                                    insl.configure(text="Hope you enjoyed it")
                                    PA.configure(text=" ")
                                    x=int(score1)
                                    myc=sqlite3.connect("record.db")
                                    myr=myc.cursor()
                                    m=x*2
                                    label.configure(text="In your account,"+str(m)+" GCs have been credited. Window will close shortly..."
                                                    ,font=('Times','20','italic'),fg='blue')
                                    s="update money set amt=amt+"+str(m)+" where id='"+str(pw)+"';"
                                    myr.execute(s)
                                    myc.commit()
                                    myc.close()
                                    root.after(6000,root.destroy)
                  def nextColour():
                           nonlocal score1
                           nonlocal timelft

                           if(timelft>0):
                                    e.focus_set()
                                    if(e.get().lower()==colours[1].lower()):
                                             score1=score1+1
                                    e.delete(0,tkinter.END)
                                    random.shuffle(colours)
                                    label.config(fg = str(colours[1]), text = str(colours[0]))
                                    scoreLabel.config(text = "Score: " + str(score1))
                           
                  def startGame(event):
                           nonlocal timelft
                           nonlocal score1
                           if timelft == 60:
                                    countdown()
                           nextColour()
                  
                  
                           
                  root = tkinter.Tk()
                  root.title("COLORGAME")
                  root.geometry("375x200")
                  root.attributes('-fullscreen',True)
                  root.configure(bg='white')
                  thams=tkinter.Label(root,text="Welcome To The Color Game!",fg="black",bg="white",font=('Times','20'))
                  thams.grid(row=1,column=2)
                  tkinter.Label(root,text="   ",fg="black",bg="white",font=('Times','20')).grid(row=2,column=2)
                  PA=tkinter.Label(root,text="In this game, you have to enter the colour of the word and NOT the word itself."
                                ,fg="black",bg="white",font=('Times','20'))
                  PA.grid(row=3,column=2)
                  scoreLabel=tkinter.Label(root,text=" ",fg="black",bg="white",font=('Times','20'))
                  scoreLabel.grid(row=6,column=2)
                  insl=tkinter.Label(root,text="TYPE A IN BOX ,PRESS ENTER TO BEGIN",fg="black",bg="white",font=('Times','20'))
                  insl.grid(row=7,column=2)
                  timeLabel=tkinter.Label(root,text="Your Time Left:"+str(timelft)
                                          ,fg="black",bg="white",font=('Times','20'))
                  timeLabel.grid(row=5,column=2)
                  label=tkinter.Label(root,text="  ",fg="black",bg="white",font=('Times','30'))
                  label.grid(row=8,column=2)
                  e=tkinter.Entry(root,font=('Times','20'),fg='black',bg='white')
                  e.grid(row=9,column=2)
                  enterhere=tkinter.Label(root,text="    ",fg="black",bg="white",font=('Times','20'))
                  enterhere.grid(row=9,column=1)
                  root.bind('<Return>',startGame)
                  e.focus_set()
                  exitas=tkinter.Button(root,text="EXIT",fg="black",bg="red",font=('Times','20'),activebackground="red",command=root.destroy)
                  exitas.grid(row=11,column=2)
                  

         def Akcess():
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x=str(i[2])
                                    x=str(x)
                                    x=int(x)
                                    f3=True 
                                    if(x>=20):
                                             x38.grid_forget()
                                             e45.configure(text="Access Granted! Please wait...")
                                             myr.execute("update money set amt=amt-20 where ID='"+str(i[0])+"';")
                                             myc.commit()
                                             myc.close()
                                             mn.after(2000,GamLoader)
                                    else:
                                             e45.configure(text="NOT ENOUGH BALANCE LEFT! PLEASE RECHARGE!")
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")


         x38=tkinter.Button(mn,text="LOGIN",fg="black",activebackground="blue",bg="blue",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(mn,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=mn.destroy)
         x389.grid(row=8,column=2)

#Create at least one more game for the people
#Define Stone Ppae scissros
def SPSstart():
         mn=tkinter.Tk()
         mn.configure(bg="yellow")
         mn.geometry("1000x1000")
         mn.attributes('-fullscreen',True)
         mn.attributes('-topmost',True)
         mn.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(mn,text="Welcome to the ACCESS Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(mn,text="Before starting, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(mn,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(mn,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(mn,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(mn,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(mn,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
         def SPSstart2():
                  #WINDOW
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  sps=tkinter.Tk()
                  sps.title('STONE PAPER SCISSORS')
                  sps.configure(bg='white')
                  sps.geometry('1000x1000')
                  sps.attributes('-topmost',True)
                  sps.attributes('-fullscreen',True)
                  mn.destroy()
                  #Labels for guidance
                  tkinter.Label(sps,text="   ",font=('Times','18'),fg='black',bg='white').grid(row=1,column=1)
                  tkinter.Label(sps,text="WELCOME TO THE STONE PAPER SCISSORS WINDOW",font=('Times','18'),fg='black',bg='white').grid(row=1,column=2)
                  tkinter.Label(sps,text="To play this game,you have to select the button corresponding to your choice below."
                                ,font=('Times','18'),fg='black',bg='white').grid(row=2,column=2)
                  w2=tkinter.Label(sps,text="Please Select The Number Of Turns For This Game:"
                                ,font=('Times','18'),fg='black',bg='white')
                  w2.grid(row=3,column=1)
                  lst2=[]
                  for i in range(5,20,5):
                           lst2.append(i)
                  #Input via combobox
                  n0=tkinter.StringVar()
                  ntake=ttk.Combobox(sps,textvariable=n0,width=20)
                  ntake['values']=tuple(lst2)
                  ntake['state']='readonly'
                  ntake.grid(row=3,column=2)
                  ntake.current(0)
                  #define game to start the game
                  def StartG():
                           x=int(ntake.get())
                           buttonen.grid_forget()
                           buttonez.grid_forget()
                           ntake.grid_forget()
                           w2.grid_forget()
                           tkinter.Label(sps,text="Your Game Has Started! Have Fun!!",font=('Times','18'),fg='black',bg='white').grid(row=3,column=2)
                           #Take the points also
                           manp=0
                           comp=0
                           tf=x
                           #Make some way for the better people
                           listo=['stone','paper','scissor']
                           #Labels to see updates
                           tkinter.Label(sps,text="  ",font=('Times','18'),fg='black',bg='white').grid(row=6,column=2)
                           tkinter.Label(sps,text="Computer Choice:",font=('Times','18'),fg='black',bg='white').grid(row=7,column=1)
                           comu=tkinter.Label(sps,text="  ",font=('Times','18'),fg='black',bg='white')
                           comu.grid(row=7,column=2)
                           tkinter.Label(sps,text="Your Choice:",font=('Times','18'),fg='black',bg='white').grid(row=8,column=1)
                           manu=tkinter.Label(sps,text="  ",font=('Times','18'),fg='black',bg='white')
                           manu.grid(row=8,column=2)
                           tkinter.Label(sps,text="Your Score:",font=('Times','18'),fg='black',bg='white').grid(row=9,column=1)
                           scoreu=tkinter.Label(sps,text=str(manp),font=('Times','18'),fg='black',bg='white')
                           scoreu.grid(row=9,column=2)
                           tkinter.Label(sps,text="Turns Left:",font=('Times','18'),fg='black',bg='white').grid(row=10,column=1)
                           turnu=tkinter.Label(sps,text=str(tf),font=('Times','18'),fg='black',bg='white')
                           turnu.grid(row=10,column=2)
                           #Game ender signal
                           taku=tkinter.Label(sps,text=' ',font=('Times','18'),fg='black',bg='white')
                           taku.grid(row=11,column=2)
                           buttonez2=tkinter.Button(sps,text="EXIT THIS PAGE",fg='black',bg='red',activebackground='red',font=('Times','16'),command=sps.destroy)
                           buttonez2.grid(row=12,column=2)
                           def TakeStone1():
                                    nonlocal manp
                                    nonlocal tf
                                    #User takes stone
                                    button145.grid_forget()
                                    button146.grid_forget()
                                    button147.grid_forget()
                                    if(tf>0):
                                             #computer choice
                                             mel=random.choice(listo)
                                             comu.configure(text=str(mel))
                                             manu.configure(text='stone')
                                             tf=tf-1
                                             turnu.configure(text=str(tf))
                                             if(mel=='scissor'):
                                                      manp=manp+1
                                                      scoreu.configure(text=str(manp))
                                             button145.grid(row=5,column=1)
                                             button146.grid(row=5,column=2)
                                             button147.grid(row=5,column=3)
                                             
                                    if(tf==0):
                                             buttonez2.grid_forget()
                                             button145.grid_forget()
                                             button146.grid_forget()
                                             button147.grid_forget()
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             m=manp*4
                                             smela="GAME OVER!!! You have got "+str(m)+" GCs from this game! Window will close shortly..."
                                             taku.configure(text=smela,fg='red')
                                             s="update money set amt=amt+"+str(m)+" where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             sps.after(4000,sps.destroy)
                                             
                                                      
                           def TakePaper2():
                                    nonlocal manp
                                    nonlocal tf
                                    #User takes paper
                                    button145.grid_forget()
                                    button146.grid_forget()
                                    button147.grid_forget()
                                    if(tf>0):
                                             #computer choice
                                             mel=random.choice(listo)
                                             comu.configure(text=str(mel))
                                             manu.configure(text='paper')
                                             tf=tf-1
                                             turnu.configure(text=str(tf))
                                             if(mel=='stone'):
                                                      manp=manp+1
                                                      scoreu.configure(text=str(manp))
                                                      
                                             button145.grid(row=5,column=1)
                                             button146.grid(row=5,column=2)
                                             button147.grid(row=5,column=3)
                                                      
                                    if(tf==0):
                                             buttonez2.grid_forget()
                                             button145.grid_forget()
                                             button146.grid_forget()
                                             button147.grid_forget()
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             m=manp*4
                                             smela="GAME OVER!!! You have got "+str(m)+" GCs from this game! Window will close shortly..."
                                             taku.configure(text=smela,fg='red')
                                             s="update money set amt=amt+"+str(m)+" where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             sps.after(4000,sps.destroy)                  
                           
                           def TakeScissor3():
                                    nonlocal manp
                                    nonlocal tf
                                    #User takes paper
                                    button145.grid_forget()
                                    button146.grid_forget()
                                    button147.grid_forget()
                                    if(tf>0):
                                             #computer choice
                                             mel=random.choice(listo)
                                             comu.configure(text=str(mel))
                                             manu.configure(text='scissor')
                                             tf=tf-1
                                             turnu.configure(text=str(tf))
                                             if(mel=='paper'):
                                                      manp=manp+1
                                                      scoreu.configure(text=str(manp))
                                             button145.grid(row=5,column=1)
                                             button146.grid(row=5,column=2)
                                             button147.grid(row=5,column=3)
                                                      
                                    if(tf==0):
                                             buttonez2.grid_forget()
                                             button145.grid_forget()
                                             button146.grid_forget()
                                             button147.grid_forget()
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             m=manp*4
                                             smela="GAME OVER!!! You have got "+str(m)+" GCs from this game! Window will close shortly..."
                                             taku.configure(text=smela,fg='red')
                                             s="update money set amt=amt+"+str(m)+" where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             sps.after(4000,sps.destroy)
                           
                           button145=tkinter.Button(sps,text="STONE",fg='black',bg='yellow',activebackground='yellow',font=('Times','16'),command=TakeStone1)
                           button145.grid(row=5,column=1)
                           button146=tkinter.Button(sps,text="PAPER",fg='black',bg='pink',activebackground='pink',font=('Times','16'),command=TakePaper2)
                           button146.grid(row=5,column=2)
                           button147=tkinter.Button(sps,text="SCISSOR",fg='black',bg='cyan',activebackground='cyan',font=('Times','16'),command=TakeScissor3)
                           button147.grid(row=5,column=3)
                                             
                           
                  #Button to take in value and also for exit
                  buttonen=tkinter.Button(sps,text="SUBMIT AND START GAME",fg='black',bg='blue',activebackground='blue',font=('Times','16'),command=StartG)
                  buttonen.grid(row=5,column=2)
                  tkinter.Label(sps,text="   ",font=('Times','18'),fg='black',bg='white').grid(row=6,column=2)
                  tkinter.Label(sps,text=" ",font=('Times','18'),fg='black',bg='white').grid(row=4,column=2)
                  buttonez=tkinter.Button(sps,text="EXIT THIS PAGE",fg='black',bg='red',activebackground='red',font=('Times','16'),command=sps.destroy)
                  buttonez.grid(row=7,column=2)



         def Akcess():
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x=str(i[2])
                                    x=str(x)
                                    x=int(x)
                                    f3=True 
                                    if(x>=20):
                                             x38.grid_forget()
                                             e45.configure(text="Access Granted! Please wait...")
                                             myr.execute("update money set amt=amt-20 where ID='"+str(i[0])+"';")
                                             myc.commit()
                                             myc.close()
                                             mn.after(1000,SPSstart2)
                                    else:
                                             e45.configure(text="NOT ENOUGH BALANCE LEFT! PLEASE RECHARGE!")
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")
                                    

         x38=tkinter.Button(mn,text="LOGIN",fg="black",activebackground="blue",bg="blue",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(mn,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=mn.destroy)
         x389.grid(row=8,column=2)

         
def ratewindow():
         rt=tkinter.Tk()
         rt.title("FEEDBACK")
         rt.configure(bg='white')
         rt.geometry('1000x1000')
         rt.attributes('-topmost',True)
         rt.attributes('-fullscreen',True)
         #Make the labels to guide you
         tkinter.Label(rt,text="  ",font=('Times','16'),fg='black',bg='white').grid(row=1,column=0)
         tkinter.Label(rt,text="FEEDBACK SYSTEM",font=('Times','16'),fg='black',bg='white').grid(row=0,column=2)
         tkinter.Label(rt,text="If you have any complaints/compliments, you can use this window.",font=('Times','16'),fg='black',bg='white').grid(row=1,column=2)
         tkinter.Label(rt,text="Before that, please tell us your name:",font=('Times','16'),fg='black',bg='white').grid(row=2,column=2)
         namel=tkinter.Label(rt,text="Please Enter Your Name Here:",font=('Times','16'),fg='black',bg='white',justify='right')
         namel.grid(row=3,column=1)
         
         #Name Taker
         nametake=tkinter.Entry(rt,font=('Times','16'),fg='black',bg='white')
         nametake.grid(row=3,column=2)
         #Make the f=button and functin
         #For update
         name2=tkinter.Label(rt,text="  ",font=('Times','16'),fg='black',bg='white',justify='right')
         name2.grid(row=7,column=2)
         def GiveRate():
                  buttontak.grid_forget()
                  x=str(nametake.get())
                  if(len(x)==0):
                           name2.configure(text="Please Enter Your Name!!",fg='red')
                           buttontak.grid(row=4,column=2)
                  else:
                           f=False
                           for i in x:
                                    if(i.isdigit()==True):
                                             name2.configure(text="Please Enter A Valid Name!!",fg='red')
                                             buttontak.grid(row=4,column=2)
                                             f=True
                                             break
                           if(f==False):
                                    #Take the review
                                    name2.configure(text=' ')
                                    name3=tkinter.Label(rt,text="Please Select Your Rating Here:",font=('Times','16'),fg='black',bg='white',justify='right')
                                    name3.grid(row=8,column=1)
                                    mte=tkinter.StringVar()
                                    stater=ttk.Combobox(rt,width=20,textvariable=mte)
                                    lstrate=[]
                                    for i in range(1,11):
                                             lstrate.append(i)
                                    stater['values']=tuple(lstrate)
                                    stater.grid(row=8,column=2)
                                    #Write some review about the panel
                                    name4=tkinter.Label(rt,text="Write a Review (Optional):",font=('Times','16'),fg='black',bg='white',justify='right')
                                    name4.grid(row=9,column=1)
                                    name7=tkinter.Label(rt,text="Enter Your EmailID Here:",font=('Times','16'),fg='black',bg='white',justify='right')
                                    name7.grid(row=10,column=1)
                                    name5=tkinter.Label(rt,text="  ",font=('Times','16'),fg='black',bg='white',justify='right')
                                    name5.grid(row=12,column=2)
                                    #Textbox
                                    rev=tkinter.Text(rt,bg='white',fg='black',font=('Times','16'),height=5,width=52)
                                    rev.grid(row=9,column=2)
                                    nametake2=tkinter.Entry(rt,font=('Times','16'),fg='black',bg='white')
                                    nametake2.grid(row=10,column=2)
                                    #Submit final call
                                    def GiveAWAY():
                                             try:
                                                      buttomsub.grid_forget()
                                                      x=str(stater.get())
                                                      x=int(x)
                                                      y=str(rev.get('1.0','end-1c'))
                                                      xy=str(nametake2.get())
                                                      r=False
                                                      if(len(xy)==0):
                                                               name5.configure(text="Please Enter Correct Email!",fg='red')
                                                               r=True
                                                               buttomsub.grid(row=11,column=2)
                                                      if(r==False):
                                                               s=smtplib.SMTP('smtp.gmail.com',587)
                                                               s.starttls()
                                                               s.login('dummyaman2004@gmail.com','eahk zxeg kwiy gvuc')
                                                               messa="REVIEW OF THE SYSTEM\n"
                                                               messa=messa+"Name of the person:"+str(nametake.get())+".\n"
                                                               messa=messa+"Stars given:"+str(x)+"\n"
                                                               messa=messa+"Review:"+str(y)+"\n"
                                                               messa=messa+"Email contact:"+str(xy)+"\n"
                                                               s.sendmail('&&&&&&&&&&&','amanrajmathematics@gmail.com',messa)
                                                               s.close()
                                                               name5.configure(text="Successfully Submitted... Window will close shortly...")
                                                               rt.after(4000,rt.destroy)
                                                      
                                             except ValueError:
                                                      name5.configure(text="PLEASE SELECT A VALID RATING!",fg='red')
                                                      buttomsub.grid(row=10,column=2)
                                             
                                    buttomsub=tkinter.Button(rt,text="FINAL SUBMIT",fg='black',bg='blue',font=('Times','16'),command=GiveAWAY)
                                    buttomsub.grid(row=11,column=2)
                           
                           
                           
         buttontak=tkinter.Button(rt,text="CONFIRM",bg='green',activebackground='green',fg='black',command=GiveRate,font=('Times','16'))
         buttontak.grid(row=4,column=2)
         tkinter.Label(rt,text="  ",font=('Times','16'),fg='black',bg='white').grid(row=5,column=2)
         buttontake=tkinter.Button(rt,text="EXIT THIS PAGE",bg='red',activebackground='red',fg='black',command=rt.destroy,font=('Times','16'))
         buttontake.grid(row=6,column=2)
#Make the new The Simple Fight Game
def SimFig():
         mn=tkinter.Tk()
         mn.configure(bg="yellow")
         mn.geometry("1000x1000")
         mn.attributes('-fullscreen',True)
         mn.attributes('-topmost',True)
         mn.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(mn,text="Welcome to the ACCESS Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(mn,text="Before starting, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(mn,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(mn,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(mn,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(mn,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(mn,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
        
         #Make the initiator of the game
         def Game1():
                  #Make the window that guides to the formation

                  #Make the guider labels
                  tkinter.Label(game,text="  ",fg='black',bg='#60d916',font=('Times','18')).grid(row=1,column=1)
                  tkinter.Label(game,text="Welcome To The WAR Game",fg='black',bg='#60d916',font=('Times','18')).grid(row=1,column=2)
                  choserlab=tkinter.Label(game,text="Please Select Your Character:",fg='black',bg='#60d916',font=('Times','18'))
                  choserlab.grid(row=2,column=1)
                  #here
                  il=tkinter.StringVar()
                  sta1=ttk.Combobox(game,textvariable=il,width=25)
                  sta1['values']=('Tiger 100 HP','Hrithik 150 HP','Varun 200 HP')
                  sta1['state']='readonly'
                  sta1.current(0)
                  sta1.grid(row=2,column=2)
                  buttonse2=tkinter.Button(game,text="EXIT THIS PAGE",fg='black',bg='#de1616',activebackground='#de1616',command=game.destroy,font=('Times','18'))
                  buttonse2.grid(row=5,column=2)
                  tkinter.Label(game,text="    ",fg='black',bg='#60d916',font=('Times','18')).grid(row=4,column=2)
                  #define function on basis of character yo!
                  def Pla():
                           buttonsen.grid_forget()
                           buttonse2.grid_forget()
                           x=str(sta1.get())
                           #Make player hit points
                           playerhp=0
                           computerhp=180
                           kp=0 #Kick points
                           pp=0 #Punch points (player)
                           gp=0 #Gun points
                           tim=2 #umber of times you cn  use guns
                           #Update hitpoint/kick/punch/gunof basis of x
                           sta1.grid_forget()
                           choserlab.grid_forget()
                           if(x=='Tiger 100 HP'):
                                    playerhp=100
                                    kp=20
                                    pp=30
                                    gp=40
                                    tkinter.Label(game,text="You are: Tiger",fg='black',bg='#60d916',font=('Times','18')).grid(row=6,column=2)
                           if(x=='Hrithik 150 HP'):
                                    playerhp=150
                                    kp=10
                                    pp=20
                                    gp=30
                                    tkinter.Label(game,text="You are: Hrithik",fg='black',bg='#60d916',font=('Times','18')).grid(row=6,column=2)
                           if(x=='Varun 200 HP'):
                                    playerhp=200
                                    kp=10
                                    pp=15
                                    gp=25
                                    tkinter.Label(game,text="You are: Varun",fg='black',bg='#60d916',font=('Times','18')).grid(row=6,column=2)
                           tkinter.Label(game,text="Kill Computer by using the three buttons for attack and one for defence."
                                         ,fg='black',bg='#60d916',font=('Times','18')).grid(row=7,column=2)
                           #HP updator label
                           ss="Your HPs:"+str(playerhp)
                           n=playerhp
                           pointup=tkinter.Label(game,text=ss,fg='black',bg='#60d916',font=('Times','18'))
                           pointup.grid(row=8,column=2)
                           ss3="Computer HPs:"+str(computerhp)
                           n2=computerhp
                           pointup2=tkinter.Label(game,text=ss3,fg='black',bg='#60d916',font=('Times','18'))
                           pointup2.grid(row=14,column=2)
                           #We have to the find comp functions
                           comlst=['kick','punch','defend']
                           #Complete screen layout
                           ss2="Computer Has Chosen:"
                           comchoice=tkinter.Label(game,text=ss2,fg='black',bg='#60d916',font=('Times','18'))
                           comchoice.grid(row=15,column=2)
                           #Describe Label
                           text1="Damage By this button is:"+str(kp)+" HP"
                           tkinter.Label(game,text=text1,fg='black',bg='#60d916',font=('Times','18')).grid(row=10,column=1)
                           text2="Damage By this button is:"+str(pp)+" HP"
                           tkinter.Label(game,text=text2,fg='black',bg='#60d916',font=('Times','18')).grid(row=11,column=1)
                           text3="Damage By this button is:"+str(gp)+" HP"
                           tkinter.Label(game,text=text3,fg='black',bg='#60d916',font=('Times','18')).grid(row=12,column=1)
                           text2="This button reduced the opponent damage by 10 HPs."
                           tkinter.Label(game,text=text2,fg='black',bg='#60d916',font=('Times','18')).grid(row=13,column=1)
                           #Desgin functions to faciliatte the attack
                           buttonexit1=tkinter.Button(game,text="EXIT THIS WINDOW",font=('Times','16'),fg='black',bg='red',activebackground='red',command=game.destroy)
                           buttonexit1.grid(row=16,column=2)
                           def Kick():
                                    nonlocal playerhp
                                    nonlocal computerhp
                                    commove=random.choice(comlst)
                                    buttonkick.grid_forget()
                                    buttonpunch.grid_forget()
                                    buttongun.grid_forget()
                                    buttondef.grid_forget()
                                    ss2='Computer Has Chosen:'+str(commove)
                                    comchoice.configure(text=ss2)
                                    if(playerhp>0 and computerhp>0):
                                             if(commove=='kick'):
                                                      playerhp=playerhp-10
                                                      computerhp=computerhp-kp
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='punch'):
                                                      playerhp=playerhp-30
                                                      computerhp=computerhp-kp
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='defend'):
                                                      playerhp=playerhp-0
                                                      computerhp=computerhp-kp+10
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                    if(playerhp==0 and computerhp !=0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game,text="You Have Lost the Game... Better Luck Next Time!!"
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             game.after(4000,game.destroy)
                                    if(playerhp !=0 and computerhp ==0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttondef.grid_forget()
                                             buttonexit1.grid_forget()
                                             tkinter.Label(game
                                                           ,text="You Have Won the Game... 40 GCs have been credited to your account!! Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+40 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                                    if(playerhp==0 and computerhp ==0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game,text="Its a Draw!! 10 GCs will be credited to your account. Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+10 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                           def Punch():
                                    nonlocal playerhp
                                    nonlocal computerhp
                                    commove=random.choice(comlst)
                                    buttonkick.grid_forget()
                                    buttonpunch.grid_forget()
                                    buttongun.grid_forget()
                                    buttondef.grid_forget()
                                    ss2='Computer Has Chosen:'+str(commove)
                                    comchoice.configure(text=ss2)
                                    if(playerhp>0 and computerhp>0):
                                             if(commove=='kick'):
                                                      playerhp=playerhp-10
                                                      computerhp=computerhp-pp
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='punch'):
                                                      playerhp=playerhp-30
                                                      computerhp=computerhp-pp
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='defend'):
                                                      playerhp=playerhp-0
                                                      computerhp=computerhp-pp+10
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                    if(playerhp<=0 and computerhp >0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game,text="You Have Lost the Game... Better Luck Next Time!!"
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             game.after(4000,game.destroy)
                                    if(playerhp >0 and computerhp <=0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game
                                                           ,text="You Have Won the Game... 40 GCs have been credited to your account!! Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+40 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                                    if(playerhp<=0 and computerhp <=0):
                                             buttonkick.grid_forget()
                                             buttondef.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             tkinter.Label(game,text="Its a Draw!! 10 GCs will be credited to your account. Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+10 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                           def Gun():
                                    nonlocal tim
                                    nonlocal playerhp
                                    nonlocal computerhp
                                    commove=random.choice(comlst)
                                    buttonkick.grid_forget()
                                    buttonpunch.grid_forget()
                                    buttongun.grid_forget()
                                    buttondef.grid_forget()
                                    ss2='Computer Has Chosen:'+str(commove)
                                    comchoice.configure(text=ss2)
                                    val=True
                                    if(tim>0):
                                             val=False
                                    if(val==True):
                                             tkinter.Label(game,text="Gun is NOT allowed since you have shoot two times!!!"
                                                           ,fg='black',bg='#60d916',font=('Times','14')).grid(row=18,column=2)
                                             buttonkick.grid(row=10,column=2)
                                             buttonpunch.grid(row=11,column=2)
                                             buttongun.grid(row=12,column=2)
                                             buttondef.grid(row=13,column=2)
                                             
                                    if(playerhp>0 and computerhp>0 and val==False):
                                             tim=tim-1
                                             if(commove=='kick'):
                                                      playerhp=playerhp-10
                                                      computerhp=computerhp-gp
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='punch'):
                                                      playerhp=playerhp-30
                                                      computerhp=computerhp-gp
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='defend'):
                                                      playerhp=playerhp-0
                                                      computerhp=computerhp-gp+10
                                                      ss="Your HPs:"+str(computerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(playerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                    if(playerhp==0 and computerhp !=0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game,text="You Have Lost the Game... Better Luck Next Time!!"
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             game.after(4000,game.destroy)
                                    if(playerhp !=0 and computerhp ==0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game
                                                           ,text="You Have Won the Game... 40 GCs have been credited to your account!! Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+40 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                                    if(playerhp==0 and computerhp ==0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game,text="Its a Draw!! 10 GCs will be credited to your account. Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+10 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                           def Defence():
                                    nonlocal playerhp
                                    nonlocal computerhp
                                    commove=random.choice(comlst)
                                    buttonkick.grid_forget()
                                    buttonpunch.grid_forget()
                                    buttongun.grid_forget()
                                    buttondef.grid_forget()
                                    ss2='Computer Has Chosen:'+str(commove)
                                    comchoice.configure(text=ss2)
                                    if(playerhp>0 and computerhp>0):
                                             if(commove=='kick'):
                                                      playerhp=playerhp
                                                      computerhp=computerhp-0
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='punch'):
                                                      playerhp=playerhp-20
                                                      computerhp=computerhp-0
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                             if(commove=='defend'):
                                                      playerhp=playerhp-0
                                                      computerhp=computerhp-0
                                                      ss="Your HPs:"+str(playerhp)+"/"+str(n)
                                                      pointup.configure(text=ss)
                                                      ss3="Computer HPs:"+str(computerhp)+"/"+str(n2)
                                                      pointup2.configure(text=ss3)
                                                      buttonkick.grid(row=10,column=2)
                                                      buttonpunch.grid(row=11,column=2)
                                                      buttongun.grid(row=12,column=2)
                                                      buttondef.grid(row=13,column=2)
                                    if(playerhp==0 and computerhp !=0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game,text="You Have Lost the Game... Better Luck Next Time!!"
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             game.after(4000,game.destroy)
                                    if(playerhp !=0 and computerhp ==0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game
                                                           ,text="You Have Won the Game... 40 GCs have been credited to your account!! Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+40 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                                    if(playerhp==0 and computerhp ==0):
                                             buttonkick.grid_forget()
                                             buttonpunch.grid_forget()
                                             buttongun.grid_forget()
                                             buttonexit1.grid_forget()
                                             buttondef.grid_forget()
                                             tkinter.Label(game,text="Its a Draw!! 10 GCs will be credited to your account. Window will close shortly..."
                                                           ,fg='black',bg='#60d916',font=('Times','18')).grid(row=16,column=2)
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             s="update money set amt=amt+10 where id='"+str(pw)+"';"
                                             myr.execute(s)
                                             myc.commit()
                                             myc.close()
                                             game.after(6000,game.destroy)
                                             
                           #Buttons for attack and defence
                           buttonkick=tkinter.Button(game,text="KICK",font=('Times','16'),fg='black',bg='#22c968',activebackground='#22c968',command=Kick)
                           buttonkick.grid(row=10,column=2)
                           buttonpunch=tkinter.Button(game,text="PUNCH",font=('Times','16'),fg='black',bg='#22c968',activebackground='#22c968',command=Punch)
                           buttonpunch.grid(row=11,column=2)
                           buttongun=tkinter.Button(game,text="GUN",font=('Times','16'),fg='black',bg='#22c968',activebackground='#22c968',command=Gun)
                           buttongun.grid(row=12,column=2)
                           buttondef=tkinter.Button(game,text="DEFENCE",font=('Times','16'),fg='black',bg='#22c968',activebackground='#22c968',command=Defence)
                           buttondef.grid(row=13,column=2)         

                           
                  buttonsen=tkinter.Button(game,text="CONFIRM AND PLAY",fg='black',bg='#1db2db',activebackground='#1db2db',command=Pla,font=('Times','18'))
                  buttonsen.grid(row=3,column=2)
                  
                  

         
         
         def Akcess():
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x=str(i[2])
                                    x=str(x)
                                    x=int(x)
                                    f3=True 
                                    if(x>=20):
                                             x38.grid_forget()
                                             e45.configure(text="Access Granted! Please wait...")
                                             myr.execute("update money set amt=amt-20 where ID='"+str(i[0])+"';")
                                             myc.commit()
                                             myc.close()
                                             mn.after(1000,Game1)
                                    else:
                                             e45.configure(text="NOT ENOUGH BALANCE LEFT! PLEASE RECHARGE!")
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")
                                    

         x38=tkinter.Button(mn,text="LOGIN",fg="black",activebackground="blue",bg="blue",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(mn,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=mn.destroy)
         x389.grid(row=8,column=2)
def HTP():
         #Instructions window.
         inst=tkinter.Tk()
         inst.title('INSTRUCTIONS')
         inst.configure(bg='yellow')
         inst.attributes('-topmost',True)
         inst.geometry('1000x1000')
         inst.attributes('-fullscreen',True)
         #Instructins
         tkinter.Label(inst,text="INSTRUCTIONS REGARDING WAR GAME",fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst,text="1. The game has 2 players: YOU and  THE COMPUTER.",fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="2. The game begins with selection of character. With each character, its Health Points(HP) are written aside it. "
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst,text="3. Currently, only 3 characters are available: Tiger,Hrithik and Varun.",fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="4. All characters can attack computer via four moves: KICK, PUNCH, GUN or DEFENCE."
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="5. The damage done by each move will be depicted during the game. "
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="6.THE GUN CAN BE USED ONLY TWO TIMES DURING THE ENTIRE GAME. USE IT WISELY"
                       ,fg='black',bg='yellow',font=('Times','16','bold')).pack()
         tkinter.Label(inst
                       ,text="7. With DEFENCE, you will NOT attack the COMPUTER and the attack of COMPUTER will be decreased by 10 HPs simply."
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="8. The COMPUTER also has a set of moves: KICK, PUNCH and DEFENCE. "
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="9. A KICK by the COMPUTER can cause 10 HP damage and a PUNCH causes 30 HPs damage. DEFENCE is same for both."
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="10. HPs are a measure of the life of the character.They will be displayed during the entire game."
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="11. When either of YOU or COMPUTER has 0 HPs, the game ends. Consequently, the GCs will be awarded after that."
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="12. If you have positive HPs at the end, you will be declared winner and will be awarded 40 GCs."
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="13. If both have 0 HPs, then it will be a DRAW and 10 GCs will be awarded. Loss will result in no GCs. "
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Label(inst
                       ,text="14. If you exit before the Game, you earn no GCs, but 20 GCs are already deducted from your account."
                       ,fg='black',bg='yellow',font=('Times','16')).pack()
         tkinter.Button(inst,text="EXIT",fg='black',bg='red',font=('Times','16'),command=inst.destroy).pack()

#Make bulls and cows
def BS():
         mn=tkinter.Tk()
         mn.configure(bg="yellow")
         mn.geometry("1000x1000")
         mn.attributes('-fullscreen',True)
         mn.attributes('-topmost',True)
         mn.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(mn,text="Welcome to the ACCESS Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(mn,text="Before starting, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(mn,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(mn,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(mn,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(mn,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(mn,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
         #Start the game window
         def BullsandCows():
                  pw=str(passwd.get())
                  mt=str(userid.get())
                  #Window
                  b=tkinter.Tk()
                  b.geometry('1000x1000')
                  b.title('Games')
                  b.configure(bg='#89d62b')
                  b.attributes('-topmost',True)
                  b.attributes('-fullscreen',True)
                  mn.destroy()
                  #Create guider labels
                  tkinter.Label(b,text="COWS AND BULLS GAME",fg='black',bg='#89d62b',font=('Times','15')).grid(row=1,column=2)
                  tkinter.Label(b,text="Here is The Tutorial:-",fg='black',bg='#89d62b',font=('Times','15')).grid(row=2,column=1)
                  tkinter.Label(b,text="                     ",fg='black',bg='#89d62b',font=('Times','15')).grid(row=1,column=0)
                  tkinter.Label(b,text="A 4 digit integer is the answer. DO NOT ENTER 0000 in the box",fg='black',bg='#89d62b',font=('Times','15')).grid(row=3,column=2)
                  tkinter.Label(b,text="Enter A Number Here:",fg='black',bg='#89d62b',font=('Times','15')).grid(row=5,column=1)
                  output=tkinter.Label(b,text="  ",fg='black',bg='#89d62b',font=('Times','15'))
                  output.grid(row=7,column=2)
                  timee="Turns Left: 15"
                  output2=tkinter.Label(b,text=timee,fg='black',bg='#89d62b',font=('Times','15'))
                  output2.grid(row=4,column=2)
                  #Create ubput extempt
                  intake=tkinter.Entry(b,font=('Times','15'),fg='black',bg='white')
                  intake.grid(row=5,column=2)
                  #Create exit button
                  ex=tkinter.Button(b,text="EXIT THIS PAGE",fg='black',bg='#ff0303',font=('Times','15'),command=b.destroy)
                  ex.grid(row=8,column=2)
                  #Make the control moves
                  turn=15
                  lstn=[]
                  for i in range(0,10):
                           lstn.append(i)
                  n1=random.randint(1,9)
                  num1=lstn[n1]
                  lstn.remove(num1)
                  n2=random.randint(0,8)
                  num2=lstn[n2]
                  lstn.remove(num2)
                  n3=random.randint(0,7)
                  num3=lstn[n3]
                  lstn.remove(num3)
                  n4=random.randint(0,6)
                  num4=lstn[n4]
                  lstn.remove(num4)
                  correct=(1000*n1)+(100*n2)+(10*n3)+n4
                  print(correct)
                  mlon=9
                  #Define game controls
                  def TakeIn():
                           su.grid_forget()
                           nonlocal mlon
                           nonlocal turn
                           try:
                                    n=str(intake.get())
                                    n=int(n)
                                    if(turn>0):
                                             if(n==correct):
                                                      output.configure(text=
                                                                       "You have won this GAME!!! 30 GCs have been credited to your account... Window will close shortly...")
                                                      ex.grid_forget()
                                                      myc=sqlite3.connect("record.db")
                                                      myr=myc.cursor()
                                                      s="update money set amt=amt+30 where id='"+str(pw)+"';"
                                                      myr.execute(s)
                                                      myc.commit()
                                                      myc.close()
                                                      b.after(4000,b.destroy)
                                             else:
                                                      
                                                      
                                                      bulls=0
                                                      cows=0
                                                      n=str(n)
                                                      xt=str(correct)
                                             #for cows
                                                      us=''
                                                      mys=''
                                                      for i in range(0,4):
                                                               mera=n[i]
                                                               tera=xt[i]
                                                               if(mera==tera):
                                                                        bulls=bulls+1
                                                               else:
                                                                        mys=mys+mera
                                                                        us=us+tera
                                                      for i in range(0,len(us)):
                                                               if((mys[i] in us)==True):
                                                                        cows=cows+1
                                                      turn=turn-1
                                                      non="You Entered:"+str(n)+". It has"+str(bulls)+" bulls and "+str(cows)+" cows."
                                                      tkinter.Label(b,text=non,fg='black',bg='#89d62b',font=('Times','15')).grid(row=mlon,column=2)
                                                      mlon=mlon+1
                                                      kon="It has"+str(bulls)+" bulls and "+str(cows)+" cows."
                                                      output.configure(text=kon,fg='black')
                                                      nim="Turns Left: "+str(turn)
                                                      output2.configure(text=nim,fg='black')
                                                      su.grid(row=6,column=2)
                                    if(turn==0):
                                             if(n==correct):
                                                      su.grid_forget()
                                                      ex.grid_forget()
                                                      output.configure(text=
                                                                       "You Have Won This Game!! 30 GCs have been credited to your account... Window will close shortly...")
                                                      myc=sqlite3.connect("record.db")
                                                      myr=myc.cursor()
                                                      s="update money set amt=amt+30 where id='"+str(pw)+"';"
                                                      myr.execute(s)
                                                      myc.commit()
                                                      myc.close()
                                                      b.after(4000,b.destroy)
                                             else:
                                                      su.grid_forget()
                                                      ex.grid_forget()
                                                      nik="Sorry You Have lost this game!! The Number Was:"+str(correct)+"!"
                                                      output.configure(text=nik)
                                                      b.after(4000,b.destroy)
                                                      
                                                      
                           except ValueError:
                                    output.configure(text="PLEASE ENTER VALID NUMBER!!!",fg='red')
                           
                  def Inst():
                           mil=tkinter.Tk()
                           mil.geometry('1000x1000')
                           mil.configure(bg='yellow')
                           mil.attributes('-topmost',True)
                           mil.attributes('-fullscreen',True)
                           tkinter.Label(mil,text="INSTRUCTIONS",font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil,text="1. In this game, you have to guess a four digit number.",font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="2. You have 15 turns to guess after which the game will be over."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="3. Each of your response is indicated by using BULLS and COWS."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="Just take an example. Suppose the correct answer is 3426"
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="You type 1436 in the box given."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="HERE, THE BULLS indicate the number of the place(s) where NUMBERS has/have been CORRECTLY filled."
                                         ,font=('Times','15','bold'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="So, in above example, '4' and '6' will act as a BULL. The output will show 2 bull hence."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="HERE, THE COWS indicate the number of number(s) that is/are in the number but NOT in correct places."
                                         ,font=('Times','15','bold'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="In above example, '3' will be a cow. So We have 1 cow as our output."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="4. FOR YOUR REFERENCE, the outputs will be displayed below the EXIT button."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="5. USE your wit and guesswork to solve this game."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="6. Winner will get 30 GCs and losers will get none. "
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Button(mil
                                         ,text="exit"
                                         ,font=('Times','15'),bg='red',fg='black',command=mil.destroy).pack()
                                             
                                    
                  su=tkinter.Button(b,text="CHECK MY NUMBER",fg='black',bg='green',font=('Times','15'),command=TakeIn)
                  su.grid(row=6,column=2)
                  HP=tkinter.Button(b,text="INSTRUCTIONS",fg='black',bg='blue',font=('Times','15'),command=Inst)
                  HP.grid(row=2,column=2)

         
         def Akcess():
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x=str(i[2])
                                    x=str(x)
                                    x=int(x)
                                    f3=True 
                                    if(x>=20):
                                             x38.grid_forget()
                                             e45.configure(text="Access Granted! Please wait...")
                                             myr.execute("update money set amt=amt-20 where ID='"+str(i[0])+"';")
                                             myc.commit()
                                             myc.close()
                                             mn.after(1000,BullsandCows)
                                    else:
                                             e45.configure(text="NOT ENOUGH BALANCE LEFT! PLEASE RECHARGE!")
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")
                                    

         x38=tkinter.Button(mn,text="LOGIN",fg="black",activebackground="blue",bg="blue",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(mn,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=mn.destroy)
         x389.grid(row=8,column=2)
def HangmanUpdated():
         mn=tkinter.Tk()
         mn.configure(bg="yellow")
         mn.geometry("1000x1000")
         mn.attributes('-fullscreen',True)
         mn.attributes('-topmost',True)
         mn.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(mn,text="Welcome to the ACCESS Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(mn,text="Before starting, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(mn,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(mn,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(mn,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(mn,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(mn,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
         #Strt actually new window for hangman
         def HangManStart():
                  mn.destroy()
                  global lst 
                  mw=tkinter.Tk()
                  mw.title("HANGMAN GAME")
                  mw.configure(bg="white")
                  mw.geometry("1000x1000")
                  mw.attributes('-topmost',True)
                  mw.attributes('-fullscreen',True)
                  #Variabkes
                  n=5
                  eme=random.randint(0,len(lst)-1)
                  exy=lst[eme]
                  n3=len(exy)
                  x="- "*n3
                  y=tkinter.Label(mw,text=x,font=("Times",'18','bold'),fg="black",bg="white",anchor='e')
                  y.place(x=683,y=256)
                  #Make the screen attributes
                  tkinter.Label(mw,text="HANGMAN GAME",fg='black',bg='white',font=('Times','18')).place(x=683,y=64)
                  tkinter.Label(mw,text="VIEW INSTRUCTIONS HERE:-",fg='black',bg='white',font=('Times','18')).place(x=100,y=128)
                  tkinter.Label(mw,text="Game Has Started!! Below is your Progress and Turns left...",fg='black',bg='white',font=('Times','18')).place(x=683,y=192)
                  tkinter.Label(mw,text="YOUR PROGRESS SO FAR:-",fg='black',bg='white',font=('Times','18')).place(x=100,y=256)
                  tkinter.Label(mw,text="NUMBER OF TURNS LEFT:-",fg='black',bg='white',font=('Times','18')).place(x=100,y=320)
                  tintin=tkinter.Label(mw,text="Use The Given Keys Below To Submit Your Choice. Each Key Correspond to Letter On It.",
                                       fg='black',bg='white',font=('Times','18'))
                  tintin.place(x=200,y=384)
                  haddock=tkinter.Label(mw,text="NOTE: Please Enter Carefully. You cannot change your entry after pressing ANY Key"
                                        ,fg='black',bg='white',font=('Times','18'))
                  haddock.place(x=200,y=448)
                  
                  mert=tkinter.Label(mw,text=str(n),font=("Times",'18','bold'),fg="black",bg="white",anchor='e')
                  mert.place(x=683,y=320)
                  winer=tkinter.Label(mw,text="     ",font=("Times",'18','bold'),fg="black",bg="white",anchor='e')
                  winer.place(x=300,y=704)
                  lsta=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                  lstb=[]
                  for i in range(0,26):
                           lstb.append(' ')
                  #X VARIABLE
                  lsti=[]
                  for i in range(0,len(exy)):
                           lsti.append('- ')
                  button2=tkinter.Button(mw,text="EXIT THIS PAGE",font=("Times",'15','bold'),fg="black",bg="red",anchor='e',command=mw.destroy)
                  button2.place(x=683,y=640)
                  def Inst2():
                           #inst window
                           myins=tkinter.Tk()
                           myins.title('instructions')
                           myins.geometry('1000x1000')
                           myins.attributes('-fullscreen',True)
                           myins.attributes('-topmost',True)
                           myins.configure(bg='yellow')
                           #Instructions packed
                           tkinter.Label(myins,text='INSTRUCTIONS REGARDING HANGMAN GAME',fg='black',bg='yellow',font=('Times','16','bold')).pack()
                           tkinter.Label(myins,text='Please read these instructions carefully.',fg='black',bg='yellow',font=('Times','16','italic')).pack()
                           tkinter.Label(myins
                                         ,text='1. In this game, you have to guess a word that will be displayed by using "-" sign.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='2. Each "-" in Your Progress denotes a letter. '
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='3. The YOUR PROGRESS bar indicates that how much you are closer to that word.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='4. Using the keys given, try a letter. If it is in the word, it will be updated. Otherwise it will be same.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='5. You have to complete the game with no more than 5 mistakes/wrong guesses. Once it reaches 5, game will END.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='6. The number of ALLOWABLE INCORRECT GUESSES is mentioned in the TURNS LEFT Tab.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='7. If you guess the world correctly before TURNS becomes zero, then you will get 30 GCs.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='8. If you are unable to do (7), then you will earn no GCs.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='9. In case you want to LEAVE before completion of game, you can do so by using EXIT THIS PAGE button. '
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Label(myins
                                         ,text='10. The window will CLOSE by itself after the game gets completed. You NEED NOT to exit the window.'
                                         ,fg='black',bg='yellow',font=('Times','16')).pack()
                           tkinter.Button(myins,text="EXIT",fg='black',bg='red',font=('Times','16'),command=myins.destroy).pack()
                  button3=tkinter.Button(mw,text="INSTRUCTIONS",font=("Times",'15','bold'),fg="black",bg="green",anchor='e',command=Inst2)
                  button3.place(x=683,y=128)         
                  def Checkis(ant):
                           nonlocal lstb
                           for i in range(0,26):
                                    lstb[i].grid_forget()
                           nonlocal n
                           nonlocal lsti
                           
                           cur=''
                           
                  #Check wether the number of turns is more than zero or not. if it is?
                           f=False
                           if(n>0):
                                    
                                    for i in range(0,len(exy)):
                                             
                                             if(str(exy[i])==ant):
                                                      myw=ant+" "
                                                      f=True
                                                      lsti[i]=ant
                                             else:
                                                      
                                                      pass
                                    
                                    for i2 in range(0,len(lsti)):
                                             cur=cur+str(lsti[i2])

                                    if(str(cur)==str(exy)):
                                             for i in range(0,26):
                                                      lstb[i].place_forget()
                                             button2.place_forget()
                                             mac=tkinter.Canvas(mw,height=250,width=250)
                                             mac.place(x=683,y=384)
                                             ig=tkinter.PhotoImage(master=mac,file=r"C:\Users\Dell\Downloads\download2.png")
                                             ips=ig.subsample(2,2)
                                             mw.ips=ips
                                             mac.create_image(0,0,image=ips,anchor='nw')
                                             tintin.place_forget()
                                             haddock.place_forget()
                                             y.configure(text=cur)
                                             winer.configure(text="YOU HAVE WON THIS GAME!!! 25.00 GCs has been credited to your gaming account!")
                                             myc=sqlite3.connect("record.db")
                                             myr=myc.cursor()
                                             myr.execute("update money set amt=amt+25 where username='"+str(mt)+"';")
                                             myc.commit()
                                             myc.close()
                                             mw.after(4000,mw.destroy)
                                    else:
                                             y.configure(text=cur)
                                             for i in range(0,26):
                                                      if(i<13):
                                                               nta=50*i+383
                                                               lstb[i].place(x=nta,y=512)
                                                      else:
                                                               nta=50*(i-13)+383
                                                               lstb[i].place(x=nta,y=576)
                                                               
                                                      

                                    if(f==False):
                                             n=n-1
                                             mert.configure(text=str(n))
                                             for i in range(0,26):
                                                      if(i<13):
                                                               nta=50*i+383
                                                               lstb[i].place(x=nta,y=512)
                                                      else:
                                                               nta=50*(i-13)+383
                                                               lstb[i].place(x=nta,y=576)
                                             
                           if(n==0):
                                    for i in range(0,26):
                                                      lstb[i].place_forget()
                                    button2.place_forget()
                                    mac=tkinter.Canvas(mw,height=250,width=250)
                                    mac.place(x=683,y=384)
                                    ig=tkinter.PhotoImage(master=mac,file=r"C:\Users\Dell\Downloads\download3.png")
                                    ips=ig.subsample(3,3)
                                    mw.ips=ips
                                    mac.create_image(0,0,image=ips,anchor='nw')
                                    tintin.place_forget()
                                    haddock.place_forget()
                                    s="You have lost this game! The correct word was:"+str(exy)+"! The window will be deleted shortly..."
                                    for i in range(0,26):
                                             lstb[i].grid_forget()
                                    button2.grid_forget()
                                    winer.configure(text=s)
                                    mw.after(5000,mw.destroy)
                                             

                  
                  
                  for i in range(0,13):
                           m=lsta[i]
                           lstb[i]=tkinter.Button(mw,text=lsta[i].upper(),fg='black',bg='#78e823',width=4,font=('Times','14'),command= lambda m=lsta[i]:Checkis(m))
                           nta=50*i+383
                           lstb[i].place(x=nta,y=512)
                  for i in range(13,26):
                           m=lsta[i]
                           lstb[i]=tkinter.Button(mw,text=lsta[i].upper(),fg='black',bg='#78e823',width=4,font=('Times','14'),command= lambda m=lsta[i]:Checkis(m))
                           nta=50*(i-13)+383
                           lstb[i].place(x=nta,y=576)
                  
                           
                  
                  
                  
                           
                   
                  
                  
                  

         def Akcess():
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x=str(i[2])
                                    x=str(x)
                                    x=int(x)
                                    f3=True 
                                    if(x>=20):
                                             x38.grid_forget()
                                             e45.configure(text="Access Granted! Please wait...")
                                             myr.execute("update money set amt=amt-20 where ID='"+str(i[0])+"';")
                                             myc.commit()
                                             myc.close()
                                             mn.after(1000,HangManStart)
                                    else:
                                             e45.configure(text="NOT ENOUGH BALANCE LEFT! PLEASE RECHARGE!")
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")
                                    

         x38=tkinter.Button(mn,text="LOGIN",fg="black",activebackground="blue",bg="blue",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(mn,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=mn.destroy)
         x389.grid(row=8,column=2)

def StartBS():
         mn=tkinter.Tk()
         mn.configure(bg="yellow")
         mn.geometry("1000x1000")
         mn.attributes('-fullscreen',True)
         mn.attributes('-topmost',True)
         mn.title("RECHARGING WINDOW")
         #Make the window more attractive!
         my12=tkinter.Label(mn,text="Welcome to the ACCESS Menu!",font=("Times",'20'),bg="yellow",fg="black")
         my12.grid(row=1,column=2)
         lune=tkinter.Label(mn,text="Before starting, please login to the system:-",font=("Times",'20'),bg="yellow",fg="black")
         lune.grid(row=2,column=2)
         login1=tkinter.Label(mn,text="Enter Your Unique UserID:",font=("Times",'20'),bg="yellow",fg="black")
         login1.grid(row=3,column=1)
         login2=tkinter.Label(mn,text="Enter Your Unique Password:",font=("Times",'20'),bg="yellow",fg="black")
         login2.grid(row=4,column=1)
         userid=tkinter.Entry(mn,font=("Times",'20'))
         userid.grid(row=3,column=2)
         passwd=tkinter.Entry(mn,font=("Times",'20'),show='*')
         passwd.grid(row=4,column=2)
         e45=tkinter.Label(mn,text="   ",font=("Times",'20'),bg="yellow",fg="black")
         e45.grid(row=5,column=2)
         #lAUNCH THE PYTHON GAME
         def Launch():
                  pw=str(passwd.get())
                  mt=str(userid.get())
                  #Window
                  b=tkinter.Tk()
                  b.geometry('1000x1000')
                  b.title('Games')
                  b.configure(bg='#a6f514')
                  b.attributes('-topmost',True)
                  b.attributes('-fullscreen',True)
                  mn.destroy()
                  #Variables are important
                  #Design window
                  tkinter.Label(b,text="BULLS AND COWS",fg='black',bg='#a6f514',font=('Times','16','bold')).place(x=683,y=0)
                  tkinter.Label(b,text="Click Here For Instructions:-",fg='black',bg='#a6f514',font=('Times','16')).place(x=100,y=34)
                  tkinter.Label(b,text="The Answer Is a 4-digit Integer. DO NOT START With 0!! ",fg='black',bg='#a6f514',font=('Times','16')).place(x=683,y=68)
                  tkinter.Label(b,text="Turns Left:-",fg='black',bg='#a6f514',font=('Times','16')).place(x=100,y=102)
                  tkinter.Label(b,text="You Have Typed:-",fg='black',bg='#a6f514',font=('Times','16')).place(x=100,y=136)
                  #Take care of number of turns
                  turn=15
                  lstni=[]
                  for i in range(0,10):
                           lstni.append(i)
                  n1=random.randint(1,9)
                  num1=lstni[n1]
                  lstni.remove(num1)
                  n2=random.randint(0,8)
                  num2=lstni[n2]
                  lstni.remove(num2)
                  n3=random.randint(0,7)
                  num3=lstni[n3]
                  lstni.remove(num3)
                  n4=random.randint(0,6)
                  num4=lstni[n4]
                  lstni.remove(num4)
                  correct=(1000*n1)+(100*n2)+(10*n3)+n4
                  mlon=9
                  #Consider the formation of the list
                  myn=''
                  lstn=[]
                  for i in range(0,4):
                           lstn.append(' ')
                  num=''
                  for i in range(0,4):
                           num=num+lstn[i]
                  #Number output here
                  output3=tkinter.Label(b,text=str(num),fg='black',bg='#a6f514',font=('Times','16'))
                  output3.place(x=683,y=136)
                  #Make a pro labeller
                  output2=tkinter.Label(b,text=str(turn),fg='black',bg='#a6f514',font=('Times','16'))
                  output2.place(x=683,y=102)
                  tkinter.Label(b,text="USE THE BELOW KEYS TO TYPE THE NUMBER:-",fg='black',bg='#a6f514',font=('Times','16')).place(x=300,y=170)
                  mlon=9
                  #define the number taker function
                  eta=0
                  def benj():
                           toplevel=tkinter.Toplevel(b)
                           toplevel.title('CONFIRMATION')
                           toplevel.geometry('300x100')

                           l1=tkinter.Label(toplevel, image="::tk::icons::question")
                           l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
                           l2=tkinter.Label(toplevel,text="ARE YOU SURE YOU WANT TO EXIT THIS PAGE?")
                           l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
                           def ka():
                                    b.destroy()
                                    toplevel.destroy()
 
                           b1=tkinter.Button(toplevel,text="Yes",command=ka,width = 10)
                           b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
                           b2=tkinter.Button(toplevel,text="No",command=toplevel.destroy,width = 10)
                           b2.grid(row=1, column=2, padx=(2, 35), sticky="e")
                  ex=tkinter.Button(b,text="EXIT THIS WINDOW",fg='black',bg='red',font=('Times','16'),command=benj)
                  ex.place(x=683,y=272)                 
                  def Insta():
                           mil=tkinter.Tk()
                           mil.geometry('1000x1000')
                           mil.configure(bg='yellow')
                           mil.attributes('-topmost',True)
                           mil.attributes('-fullscreen',True)
                           tkinter.Label(mil,text="INSTRUCTIONS",font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="1. In this game, your task is to find a 4 digit number."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="2. To help you, you will be indicated the number of BULLS and COWS in the integer. This is illustrated below:"
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text=" Example: Suppose the CORRECT answer is 3546 and YOU typed 7543."
                                         ,font=('Times','15','bold'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="Your answer(a statement) will show number of bulls and cows in 7543."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="THOSE DIGITS which lie in both CORRECT and YOUR integer and at the SAME PLACE also, are called BULLS."
                                         ,font=('Times','15','bold'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="So, in above example, digits '4' and '5' acts as BULLS."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="THOSE digits which DOES NOT lie in CORRECT places yet they are in CORRECT integer, are called COWS."
                                         ,font=('Times','15','bold'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="In the above example, '3' will act as a COW."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="So in above example,we have 2 bulls and 1 cow. "
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="Hence 2 bulls and 1 cow will be printed just below EXIT button."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="5. FOR YOUR REFERENCE, The LABELS will be written below this button. You can see them whenever you want to."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="6. You will be given 15 TURNS to guess after which THE GAME WILL OVER."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Label(mil
                                         ,text="7. A winner will get 30 GCs and LOSER will get 0 GCs."
                                         ,font=('Times','15'),bg='yellow',fg='black').pack()
                           tkinter.Button(mil
                                         ,text="exit"
                                         ,font=('Times','15'),bg='red',fg='black',command=mil.destroy).pack()
                  listoflab=[]
                  def TakeIn():
                           su.place_forget()
                           nonlocal mlon
                           nonlocal turn
                           nonlocal lstn
                           nonlocal lstb
                           nonlocal myn
                           nonlocal listoflab
                           try:
                                    myn=int(myn)
                                    if(turn>1 and myn>=1000):
                                             if(myn==correct):
                                                      ex.place_forget()
                                                      for i in range(0,10):
                                                               lstb[i].place_forget()
                                                      for i in range(0,len(listoflab)):
                                                               listoflab[i].place_forget()
                                                      tkinter.Label(b
                                                                    ,text="You have Won This Game and won 30 GCs!! Window will close shortly... "
                                                                    ,fg='black',bg='#a6f514',font=('Times','16','bold')).place(x=300,y=272)
                                                      raj=tkinter.Label(b,bg='#a6f514')
                                                      raj.place(x=400,y=306)
                                                      imog=tkinter.PhotoImage(master=raj,file=r"C:\Users\Dell\Downloads\download2.png")
                                                      cap=imog.subsample(2,2)
                                                      b.cap=cap
                                                      raj.configure(image=cap)
                                                      myc=sqlite3.connect("record.db")
                                                      myr=myc.cursor()
                                                      s="update money set amt=amt+30 where id='"+str(pw)+"';"
                                                      myr.execute(s)
                                                      myc.commit()
                                                      myc.close()
                                                      b.after(6000,b.destroy)
                                             else:
                                                      
                                                      
                                                      bulls=0
                                                      cows=0
                                                      myn=str(myn)
                                                      xt=str(correct)
                                             #for cows
                                                      us=''
                                                      mys=''
                                                      for i in range(0,4):
                                                               mera=myn[i]
                                                               tera=xt[i]
                                                               if(mera==tera):
                                                                        bulls=bulls+1
                                                               else:
                                                                        mys=mys+mera
                                                                        us=us+tera
                                                      for i in range(0,len(us)):
                                                               if((mys[i] in us)==True):
                                                                        cows=cows+1
                                                      turn=turn-1
                                                      non="You Entered:"+str(myn)+". It has"+str(bulls)+" bulls and "+str(cows)+" cows."
                                                      gab=tkinter.Label(b,text=non,fg='black',bg='#a6f514',font=('Times','15'))
                                                      gab.place(x=300,y=mlon*34)
                                                      listoflab.append(gab)
                                                      mlon=mlon+1
                                                      output2.configure(text=str(turn),fg='black')
                                                      su.place(x=683,y=238)
                                                      del myn
                                                      myn=''
                                                      output3.configure(text=str(myn))
                                                               
                                    elif(turn==1 and myn>=1000):
                                             turn=turn-1
                                             output2.configure(text=str(turn))
                                             if(myn==correct):
                                                      su.place_forget()
                                                      ex.place_forget()
                                                      for i in range(0,len(listoflab)):
                                                               listoflab[i].place_forget()
                                                      for i in range(0,10):
                                                               lstb[i].place_forget()
                                                      raj=tkinter.Label(b,bg='#a6f514')
                                                      raj.place(x=400,y=306)
                                                      imog=tkinter.PhotoImage(master=raj,file=r"C:\Users\Dell\Downloads\download2.png")
                                                      cap=imog.subsample(2,2)
                                                      b.cap=cap
                                                      raj.configure(image=cap)
                                                      tkinter.Label(b
                                                                    ,text="You have Won This Game and won 30 GCs!! Window will close shortly... "
                                                                    ,fg='black',bg='#a6f514',font=('Times','16','bold')).place(x=300,y=272)
                                                      myc=sqlite3.connect("record.db")
                                                      myr=myc.cursor()
                                                      s="update money set amt=amt+30 where id='"+str(pw)+"';"
                                                      myr.execute(s)
                                                      myc.commit()
                                                      myc.close()
                                                      b.after(4000,b.destroy)
                                             else:
                                                      for i in range(0,len(listoflab)):
                                                               listoflab[i].place_forget()
                                                      raj=tkinter.Label(b,bg='#a6f514')
                                                      raj.place(x=400,y=306)
                                                      imog=tkinter.PhotoImage(master=raj,file=r"C:\Users\Dell\Downloads\download3.png")
                                                      cap=imog.subsample(2,2)
                                                      b.cap=cap
                                                      raj.configure(image=cap)
                                                      su.place_forget()
                                                      ex.place_forget()
                                                      for i in range(0,10):
                                                               lstb[i].place_forget()
                                                      nik="Sorry You Have lost this game!! The Number Was:"+str(correct)+"!"
                                                      tkinter.Label(b
                                                                    ,text=nik
                                                                    ,fg='black',bg='#a6f514',font=('Times','16','bold')).place(x=300,y=272)
                                                      b.after(4000,b.destroy)
                                    
                                    else:
                                             
                                             del myn
                                             myn=''
                                             output3.configure(text=str(myn))
                                             output2.configure(text="PLEASE ENTER VALID NUMBER!!!")
                                             su.place(x=683,y=238)
                                             
                                                      
                           except ValueError:
                                    del myn
                                    myn=''
                                    output3.configure(text=str(myn))
                                    output2.configure(text="PLEASE ENTER VALID NUMBER!!!",fg='red')
                                    su.place(x=683,y=238)
                  su=tkinter.Button(b,text="CHECK MY NUMBER",fg='black',bg='#4d0eeb',font=('Times','16'),command=TakeIn)
                  su.place(x=683,y=240)
                  def Takein(m):
                           nonlocal lstn
                           nonlocal lstb
                           nonlocal eta
                           nonlocal myn
                           myn=str(myn)
                           myn=myn+str(m)
                           output3.configure(text=str(myn),fg='black')
                  
                  def Klear():
                           nonlocal lstb
                           nonlocal eta
                           nonlocal lstn
                           nonlocal myn
                           if(len(myn)>0):
                                    nam=myn.rstrip(myn[-1])
                                    myn=nam
                                    output3.configure(text=str(myn),fg='black')
                                    
                           
                           
                           
                                    
                  #list of buttons
                  lstb=[]
                  for iti in range(0,10):
                           lstb.append(' ')
                  mi=533
                  lstcol=['#22dde3','#22e362','#4115ed','#15ed8c','#f071e1']
                  for i in range(0,10):
                           lstb[i]=tkinter.Button(b,text=str(i),font=('Times','16'),fg='black',bg=lstcol[i%5],width=2,command= lambda p=str(i):Takein(p))
                           nta=533+i*30
                           lstb[i].place(x=nta,y=204)
                  tkinter.Button(b,text="CLEAR",fg='black',bg='blue',font=('Times','16'),width=6,command=Klear).place(x=933,y=204)
                  inst=tkinter.Button(b,text="INSTRUCTIONS",fg='black',bg='blue',font=('Times','16'),command=Insta)
                  inst.place(x=683,y=34)
                  
                           
                  
                  

         
         def Akcess():
                  global mt
                  f3=False
                  mt=str(userid.get())
                  pw=str(passwd.get())
                  myc=sqlite3.connect("record.db")
                  myr=myc.cursor()
                  myr.execute("select * from money;")     
                  x51=myr.fetchall()
                  for i in x51:
                           if(i[0]==pw and i[1]==mt):
                                    x=str(i[2])
                                    x=str(x)
                                    x=int(x)
                                    f3=True 
                                    if(x>=20):
                                             x38.grid_forget()
                                             e45.configure(text="Access Granted! Please wait...")
                                             myr.execute("update money set amt=amt-20 where ID='"+str(i[0])+"';")
                                             myc.commit()
                                             myc.close()
                                             mn.after(1000,Launch)
                                    else:
                                             e45.configure(text="NOT ENOUGH BALANCE LEFT! PLEASE RECHARGE!")
                  

                  if(f3==False):
                           e45.configure(text="PLEASE TRY AGAIN!")
                                    

         x38=tkinter.Button(mn,text="LOGIN",fg="black",activebackground="blue",bg="blue",font=("Times",'20'),command=Akcess)
         x38.grid(row=6,column=2)
         x389=tkinter.Button(mn,text="EXIT",fg="black",activebackground="red",bg="red",font=("Times",'20'),command=mn.destroy)
         x389.grid(row=8,column=2)
tkinter.Button(fra,text="ACCOUNT LOGIN",font=("Times",'15','bold'),fg="black",bg="orange",anchor='e',command=CandidateLogin).grid(row=9,column=2)                          
tkinter.Button(fra,text="CREATE AN ACCOUNT",font=("Times",'15','bold'),fg="black",bg="yellow",anchor='e',command=CreatAccount).grid(row=5,column=2)
tkinter.Button(fra,text="RECHARGE HERE",font=("Times",'15','bold'),fg="black",bg="pink",anchor='e',command=Rechagres).grid(row=7,column=2)
tkinter.Button(fra,text="PLAY COLOR GAME",font=("Times",'15','bold'),fg="black",bg="cyan",anchor='e',command=ColorGame).grid(row=13,column=2)
tkinter.Button(fra,text="EXIT THIS PANEL",font=('Times','15','bold'),bg='red',activebackground='red',fg='black',command=main.destroy).grid(row=25,column=2)
tkinter.Button(fra,text="STONE PAPER SCISSOR",font=('Times','15','bold'),bg='#76caf5',activebackground='red',fg='black',command=SPSstart).grid(row=15,column=2)
tkinter.Button(fra,text="SEND A FEEDBACK",font=('Times','15','bold'),bg='#2feb1a',activebackground='red',fg='black',command=ratewindow).grid(row=23,column=2)
tkinter.Button(fra,text="WAR GAME",font=('Times','15','bold'),bg='#fc03d3',activebackground='red',fg='black',command=SimFig).grid(row=17,column=2)
tkinter.Button(fra,text="RULES OF WAR GAME",font=('Times','15','bold'),bg='#fc03d3',activebackground='red',fg='black',command=HTP).grid(row=19,column=2)
tkinter.Button(fra,text="PLAY HANGMAN",font=("Times",'15','bold'),fg="black",bg="#bc79db",anchor='e',command=HangmanUpdated).grid(row=11,column=2)
tkinter.Button(fra,text="BULLS AND COWS",font=("Times",'15','bold'),fg="black",bg='#5af542',anchor='e',command=StartBS).grid(row=21,column=2)
main.mainloop()
