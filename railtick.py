# Make a new program wirh my own methods. It should be a nice one
#Import all the desired  modules

import tkinter
import math
import random
import time
import mysql.connector
from tkinter import ttk
import smtplib


#Write the first lines of codes i.e. formation of the screen
main=tkinter.Tk()
main.title("RAILWAY RESERVATION SYSTEM")
main.geometry("1000x1000")
main.configure(bg='white')
main.attributes('-fullscreen',True)


label1=tkinter.Label(main,text='Welcome To The Railway Reservation System',font=('Times','16'),fg='black',bg='white')
label1.grid(row=1,column=2)
glabel=tkinter.Label(main,text='     ',font=('Times','16'),fg='black',bg='white')
glabel.grid(row=2,column=2)
label2=tkinter.Label(main,text=' ',font=('Times','16'),fg='black',bg='white')
label2.grid(row=3,column=2)
label2111=tkinter.Label(main,text=' ',font=('Times','16'),fg='black',bg='white')
label2111.grid(row=6,column=2)
label2112=tkinter.Label(main,text=' ',font=('Times','16'),fg='black',bg='white')
label2112.grid(row=8,column=2)
label2112=tkinter.Label(main,text=' ',font=('Times','16'),fg='black',bg='white')
label2112.grid(row=10,column=2)
label2112=tkinter.Label(main,text=' ',font=('Times','16'),fg='black',bg='white')
label2112.grid(row=12,column=2)
#Update time
def ShuT():
         x=time.strftime('%H:%M:%S %p')
         lab="The Current Time in IST is "+str(x)
         label2.configure(text=lab)
         main.after(1000,ShuT)

ShuT()

#Make the labels that will help us to create an account into the system
label3=tkinter.Label(main,text='New here? Please create an account here:',font=('Times','16'),fg='black',bg='white')
label3.grid(row=5,column=1)
label3=tkinter.Label(main,text='Book your tickets here:',font=('Times','16'),fg='black',bg='white')
label3.grid(row=7,column=1)
label3=tkinter.Label(main,text='Account Details Missing? Recover Your Account Here:',font=('Times','16'),fg='black',bg='white')
label3.grid(row=9,column=1)
label3=tkinter.Label(main,text='Any Complaints/Compliments? Submit It Here:',font=('Times','16'),fg='black',bg='white')
label3.grid(row=11,column=1)

#Make the function that help us to create account
def CreateRailAcc():
         acc=tkinter.Tk()
         acc.title('Account Creation System')
         acc.geometry('1000x1000')
         acc.configure(bg='yellow')
         acc.attributes('-fullscreen',True)
         #Make the guider label
         label11=tkinter.Label(acc,text="ACCOUNT CREATION SYSTEM",font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label11.grid(row=1,column=2)
         #Label that tells you to add details
         label12=tkinter.Label(acc,text="To Create Account, Please Fill Your Details:",font=('Times','14','bold'),bg='yellow',fg='black',anchor='e')
         label12.grid(row=2,column=2)
         label13=tkinter.Label(acc,text="Enter Your Preffered Username:",font=('Times','14','bold'),bg='yellow',fg='black',anchor='e')
         label13.grid(row=4,column=1)
         label14=tkinter.Label(acc,text="Enter Your Preffered Password:",font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label14.grid(row=5,column=1)
         label15=tkinter.Label(acc,text="Enter Your EmailID here:",font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label15.grid(row=6,column=1)
         label16=tkinter.Label(acc,text="Enter Your Name Here:",font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label16.grid(row=7,column=1)
         #Entry boxes to enter details
         userid=tkinter.Entry(acc,font=('Times','14'),bg='white',fg='black')
         userid.grid(row=4,column=2)
         passwid=tkinter.Entry(acc,font=('Times','14'),bg='white',fg='black')
         passwid.grid(row=5,column=2)
         idmail=tkinter.Entry(acc,font=('Times','14'),bg='white',fg='red',width=50)
         idmail.grid(row=6,column=2)
         names=tkinter.Entry(acc,font=('Times','14'),bg='white',fg='red')
         names.grid(row=7,column=2)
         #Label that gives some guidance
         label17=tkinter.Label(acc,text="PLEASE SEE: 1. Your USERNAME and EMAILID are unique to you."
                               ,font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label17.grid(row=9,column=2)
         label17=tkinter.Label(acc,text="Please Fill Carefully. OTPs and Tickets will be sent on this only."
                               ,font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label17.grid(row=6,column=3)
         label18=tkinter.Label(acc,text="2. It is to be noted that only your Username and Password are your login credentials to the system."
                               ,font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label18.grid(row=10,column=2)
         label19=tkinter.Label(acc,text="3. Your EmailID and Name are your credentials to recover your account in case you forget your password or username."
                               ,font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label19.grid(row=11,column=2)
         label20=tkinter.Label(acc,text="4. Once you press SUBMIT button, you CANNOT change the credentials. Be Careful Here. "
                               ,font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label20.grid(row=12,column=2)
         label21=tkinter.Label(acc,text="5. By Creating Account, you have agreed to the Terms and Conditions of the System."
                               ,font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label21.grid(row=13,column=2)
         tkinter.Label(acc,text=" ",font=('Times','16','bold'),bg='yellow',fg='black',anchor='e').grid(row=14,column=2)
         tkinter.Label(acc,text=" ",font=('Times','16','bold'),bg='yellow',fg='black',anchor='e').grid(row=16,column=2)
         #Create lael
         label22=tkinter.Label(acc,text="  ",font=('Times','16','bold'),bg='yellow',fg='black',anchor='e')
         label22.grid(row=18,column=2)
         #Create Active Functions for this job
         def Commitment():
                  button2.grid_forget()
                  button1.grid_forget()
                  us=str(userid.get())
                  pw=str(passwid.get())
                  ma=str(idmail.get())
                  na=str(names.get())
                  mycon=mysql.connector.connect(host='localhost',user='root',passwd='',database='py')
                  mycursor=mycon.cursor()
                  mycursor.execute('select * from rail;')
                  x=mycursor.fetchall()
                  f=False
                  for i in x:
                           if(str(i[0]).lower()==us.lower() and str(i[2])==ma):
                                    label22.configure(text='Account is Already There! Pleae Try A Different Combination',fg='red')
                                    button1.grid(row=15,column=2)
                                    button2.grid(row=17,column=2)
                                    f=True
                                    break
                           
                           if(str(i[0]).lower()!=us.lower() and str(i[2])==ma):
                                    label22.configure(text='Please Use A Different EmailID',fg='red')
                                    button1.grid(row=15,column=2)
                                    button2.grid(row=17,column=2)
                                    f=True
                                    break
                           if(str(i[0]).lower()==us.lower() and str(i[2])!=ma):
                                    label22.configure(text='Please Use A Different UserName',fg='red')
                                    button1.grid(row=15,column=2)
                                    button2.grid(row=17,column=2)
                                    f=True
                                    break
                  if(f==False):
                           mystatement="Insert into rail values('"+str(us)+"','"+str(pw)+"','"+str(ma)+"','"+str(na)+"');"
                           mycursor.execute(mystatement)
                           mycon.commit()
                           mycon.close()
                           label22.configure(text="Your Account Has Been Successfully Created!",fg='blue',font=('Times','16','italic'))
                           button2.grid(row=17,column=2)
         #Buttons that will help us to guide the so called program
         button1=tkinter.Button(acc,text="SUBMIT",fg="black",bg="green",activebackground="green",font=('Times','16'),command=Commitment)
         button1.grid(row=15,column=2)
         button2=tkinter.Button(acc,text="EXIT",fg="black",bg="red",activebackground="red",font=('Times','16'),command=acc.destroy)
         button2.grid(row=17,column=2)

def ReservationSys():
         aks=tkinter.Tk()
         aks.title('Access Window')
         aks.geometry('1000x1000')
         aks.configure(bg='white')
         aks.attributes('-fullscreen',True)
         #Label Gang
         aks1=tkinter.Label(aks,text="ACCESS WINDOW",font=('Times','20','bold'),fg='black',bg='white',anchor='e')
         aks1.grid(row=1,column=3)
         aks2=tkinter.Label(aks,text="Before booking, please sign in:",font=('Times','18','bold'),fg='black',bg='white',anchor='e')
         aks2.grid(row=2,column=3)
         aks3=tkinter.Label(aks,text="Enter Your Username Here:",font=('Times','18','bold'),fg='black',bg='white')
         aks3.grid(row=4,column=2)
         aks4=tkinter.Label(aks,text="Enter Your Password Here:",font=('Times','18','bold'),fg='black',bg='white')
         aks4.grid(row=5,column=2)
         aks4=tkinter.Label(aks,text="                                      ",font=('Times','14','bold'),fg='black',bg='white')
         aks4.grid(row=1,column=1)
         
         #Take inputs
         userid=tkinter.Entry(aks,font=('Times','18'),fg='black',bg='white')
         userid.grid(row=4,column=3)
         pass1=tkinter.Entry(aks,font=('Times','18'),fg='black',bg='white',show='*')
         pass1.grid(row=5,column=3)
         #Keep track Label
         aks5=tkinter.Label(aks,text="   ",font=('Times','18','bold'),fg='black',bg='white')
         aks5.grid(row=6,column=3)
         #Validator
         def NewWin():
                  
                  mt=str(userid.get())
                  newwin=tkinter.Tk()
                  newwin.title('RAILWAY RESERVATION SYSTEM')
                  newwin.geometry('1000x1000')
                  newwin.configure(bg='white')
                  newwin.attributes('-fullscreen',True)
                  myn=mysql.connector.connect(host='localhost',user='root',passwd='aman@2004',database='py')
                  mycursor=myn.cursor()
                  s="select * from rail"
                  mycursor.execute(s)
                  m=mycursor.fetchall()
                  myemail=''
                  myname=''
                  for i in m:
                           if(i[0].lower()==mt.lower()):
                                    myemail=str(i[2])
                                    myname=str(i[3])
                  aks.destroy()
                  s2='Welcome To The Railway Reservation System.'
                  label312=tkinter.Label(newwin,text=s2,font=('Times','18'),fg='black',bg='white')
                  label312.grid(row=1,column=2)
                  label313=tkinter.Label(newwin,text='Please Do Not Change Any Information During Booking:',font=('Times','18'),fg='black',bg='white')
                  label313.grid(row=2,column=2)
                  label313=tkinter.Label(newwin,text='Select Here The Initial and Final Stations:',font=('Times','18'),fg='black',bg='white')
                  label313.grid(row=3,column=2)
                  label314=tkinter.Label(newwin,text='Choose Initial Station:',font=('Times','18'),fg='black',bg='white')
                  label314.grid(row=4,column=1)
                  label315=tkinter.Label(newwin,text='Choose Final Station:',font=('Times','18'),fg='black',bg='white')
                  label315.grid(row=5,column=1)
                  #Label for messages
                  labelup=tkinter.Label(newwin,text=' ',font=('Times','18'),fg='black',bg='white')
                  labelup.grid(row=7,column=2)
                  tkinter.Label(newwin,text=' ',font=('Times','18'),fg='black',bg='white').grid(row=6,column=1)
                  tkinter.Label(newwin,text=' ',font=('Times','18'),fg='black',bg='white').grid(row=9,column=1)
                  #mAKE the menus for the selection of the stations
                  n=tkinter.StringVar()
                  state1=ttk.Combobox(newwin,width=27,textvariable=n)
                  state1['values']=('Delhi','Jaipur','Mumbai','Patna')
                  state1['state']='readonly'
                  state1.grid(row=4,column=2)
                  n2=tkinter.StringVar()
                  state2=ttk.Combobox(newwin,width=27,textvariable=n2)
                  state2['values']=('Delhi','Jaipur','Mumbai','Patna')
                  state2['state']='readonly'
                  state2.grid(row=5,column=2)
                  #Invoke thus wen considering booking
                  lsttra=[]
                  n09=tkinter.StringVar()
                  state4=ttk.Combobox(newwin,width=27,textvariable=n09)
                  n70=tkinter.StringVar()
                  state4['state']='readonly'
                  state9=ttk.Combobox(newwin,width=27,textvariable=n70,justify='left')
                  n71=tkinter.StringVar()
                  state9['state']='readonly'
                  state10=ttk.Combobox(newwin,width=27,textvariable=n71,justify='left')
                  n72=tkinter.StringVar()
                  state10['state']='readonly'
                  state11=ttk.Combobox(newwin,width=27,textvariable=n72,justify='left')
                  state11['state']='readonly'
                  lsty=[]
                  for i in range(2021,2040):
                           lsty.append(i)
                  tup=tuple(lsty)
                  state9['values']=tup
                  state9.set('Select Year')
                  lstm=[]
                  for i in range(1,13):
                           lstm.append(i)
                  state10['values']=tuple(lstm)
                  state10.set('Select Month')
                  def TicketMaker():
                           button77.grid_forget()
                           button78.grid_forget()
                           x11=str(state1.get())
                           x21=str(state2.get())
                           if(x11==x21):
                                    labelup.configure(text="Please Choose Different Stations...",fg='red')
                                    button77.grid(row=8,column=2)
                                    button78.grid(row=10,column=2)
                           elif(x11=='' or x21==''):
                                    labelup.configure(text='Please Do Not Leave Blank Spaces',fg='red')
                                    button77.grid(row=8,column=2)
                                    button78.grid(row=10,column=2)
                           else:
                                    BookTickets()
                  def BookTickets():
                           
                           x11=str(state1.get())
                           x21=str(state2.get())
                           labelup.configure(text=' ')
                           button78.grid(row=8,column=2)
                           label313=tkinter.Label(newwin,text='Please Select The Number Of Travellers:',font=('Times','18'),fg='black',bg='white')
                           label313.grid(row=12,column=1)
                           n3=tkinter.StringVar()
                           state3=ttk.Combobox(newwin,width=27,textvariable=n3)
                           state3['values']=('1','2','3','4','5','6','7','8')
                           state3['state']='readonly'
                           state3.grid(row=12,column=2)
                           #Make function to take their names as input
                                    
                           def TakeinNames():
                                    lst=[]
                                    lstbox=[]
                                    lstlabel=[]
                                    button45.grid_forget()
                                    n4=int(state3.get())
                                    for i2 in range(0,n4):
                                             lstbox.append(' ')
                                             lstlabel.append(' ')
                                    n=14
                                    for i in range(0,n4):
                                             w=i+1
                                             tet='Please Enter Name of Passenger '+str(w)+':'
                                             lstlabel[i]=tkinter.Label(newwin,text=tet,fg='black',bg='white',font=('Times','16'))
                                             lstlabel[i].grid(row=14+i,column=1)
                                             lstbox[i]=tkinter.Entry(newwin,fg='black',bg='white',font=('Times','16'))
                                             lstbox[i].grid(row=14+i,column=2)
                                             n=n+1
                                    def TakPayment():
                                             nonlocal newwil
                                             nonlocal lst
                                             nonlocal lstbox
                                             for i in range(0,n4):
                                                      x=str(lstbox[i].get())
                                                      lst.append(x)
                                             newwil.grid_forget()
                                             tkinter.Label(newwin,text='Please Select The Train:'
                                                           ,font=('Times','18'),fg='black',bg='white').grid(row=n,column=1)
                                    
                                             if((x11=='Delhi' and x21=='Jaipur') or (x11=='Jaipur' and x21=='Delhi')):
                                                      state4['values']=('Rajdhani Express INR1000.00','Double Decker INR600.00','AC SuperFast INR900.00')
                                                      state4.grid(row=n,column=2)
                                             if((x11=='Delhi' and x21=='Mumbai') or (x11=='Mumbai' and x21=='Delhi')):
                                                      state4['values']=('Rajdhani Express INR900.00','Ganga AC Express INR1100.00','GaribRath Express INR600.00')
                                                      state4.grid(row=n,column=2)
                                             if((x11=='Mumbai' and x21=='Jaipur') or (x11=='Jaipur' and x21=='Mumbai')):
                                                      state4['values']=('Rajdhani Express INR900.00','Vande Bharat Express INR1200.00'
                                                                        ,'Mumbai-Jaipur Express INR750.00')
                                                      state4.grid(row=n,column=2)
                                             if((x11=='Mumbai' and x21=='Patna') or (x11=='Patna' and x21=='Mumbai')):
                                                      state4['values']=('Rajdhani Express INR1000.00','GaribRath Express INR650.00'
                                                                        ,'Patna-Pune Superfast Express INR850.00')
                                                      state4.grid(row=n,column=2)
                                             if((x11=='Patna' and x21=='Jaipur') or (x11=='Jaipur' and x21=='Patna')):
                                                      state4['values']=('Rajdhani Express INR900.00','Shiv Shakti Express INR1000.00'
                                                                        ,'AC Superfast Express INR950.00')
                                                      state4.grid(row=n,column=2)
                                             if((x11=='Patna' and x21=='Delhi') or (x11=='Delhi' and x21=='Patna')):
                                                      state4['values']=('Rajdhani Express INR900.00','Festival Special Express INR900.00'
                                                                        ,'Gatimaan Express INR1000.00')
                                                      state4.grid(row=n,column=2)
                                             #Make the best move by using a buttom
                                             #Make a window to accept date by the passenger
                                             tkinter.Label(newwin,text='Please Select The Date Here:'
                                                           ,font=('Times','18'),fg='black',bg='white').grid(row=n+1,column=1)
                                             state9.grid(row=n+1,column=2)
                                             state10.grid(row=n+1,column=3)
                                             def Dt():
                                                      try:
                                                               buttonn.grid_forget()
                                                               x=str(state10.get())
                                                               x=int(x)
                                                               y=str(state9.get())
                                                               y=int(y)
                                                               if(x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
                                                                        lstdat=[]
                                                                        for i in range(1,32):
                                                                                 lstdat.append(i)
                                                                        state11['values']=tuple(lstdat)
                                                                        state11.set('Select Date')
                                                                        state11.grid(row=n+1,column=4)
                                                               if(x==4 or x==6 or x==5 or x==9 or x==8 or x==11):
                                                                        lstdat=[]
                                                                        for i in range(1,31):
                                                                                 lstdat.append(i)
                                                                        state11['values']=tuple(lstdat)
                                                                        state11.set('Select Date')
                                                                        state11.grid(row=n+1,column=4)
                                                               if(x==2):
                                                                        if(y%4==0):
                                                                                 lstdat=[]
                                                                                 for i in range(1,30):
                                                                                          lstdat.append(i)
                                                                                 state11['values']=tuple(lstdat)
                                                                                 state11.set('Select Date')
                                                                                 state11.grid(row=n+1,column=4)
                                                                        if(y%4!=0):
                                                                                 lstdat=[]
                                                                                 for i in range(1,29):
                                                                                          lstdat.append(i)
                                                                                 state11['values']=tuple(lstdat)
                                                                                 state11.set('Select Date')
                                                                                 state11.grid(row=n+1,column=4)
                                                      except ValueError:
                                                               buttonn.grid(row=n+1,column=4)

                                                                        
                                             buttonn=tkinter.Button(newwin,text="Select Date",fg='black',bg='green',font=('Times','14'),command=Dt)
                                             buttonn.grid(row=n+1,column=4)
                                             newwil2.grid(row=n+2,column=2)
                                             
                                             

                                    #Make a Payment Gateway using PYthon
                                    def PaymentGate():
                                             nonlocal lst
                                             nonlocal newwil2
                                             x11=str(state1.get())
                                             x21=str(state2.get())
                                             paym=str(state4.get())
                                             yr=str(state9.get())
                                             mon=str(state10.get())
                                             dater=str(state11.get())
                                             p=0
                                             mac=''
                                             #Consider hthe several cases
                                             if((x11=='Delhi' and x21=='Jaipur') or (x11=='Jaipur' and x21=='Delhi')):
                                                      if(paym=='Rajdhani Express INR1000.00'):
                                                               p=1000
                                                               mac='Rajdhani Express'
                                                      if(paym=='Double Decker INR600.00'):
                                                               p=600
                                                               mac='Double Decker'
                                                      if(paym=='AC SuperFast INR900.00'):
                                                               p=900
                                                               mac='AC Superfast'
                                             
                                             if((x11=='Delhi' and x21=='Mumbai') or (x11=='Mumbai' and x21=='Delhi')):
                                                      if(paym=='Rajdhani Express INR900.00'):
                                                               p=900
                                                               mac='Rajdhani Express'
                                                      if(paym=='Ganga AC Express INR1100.00'):
                                                               p=1100
                                                               mac='Ganga AC Express'
                                                      if(paym=='GaribRath Express INR600.00'):
                                                               p=600
                                                               mac='GaribRath Express'

                                             if((x11=='Mumbai' and x21=='Jaipur') or (x11=='Jaipur' and x21=='Mumbai')):
                                                      if(paym=='Rajdhani Express INR900.00'):
                                                               p=900
                                                               mac='Rajdhani Express'
                                                      if(paym=='Vande Bharat Express INR1200.00'):
                                                               p=1200
                                                               mac='Vande Bharat Express'
                                                      if(paym=='Mumbai-Jaipur Express INR750.00'):
                                                               p=750
                                                               mac='Mumbai-Jaipur Express'
                                             if((x11=='Mumbai' and x21=='Patna') or (x11=='Patna' and x21=='Mumbai')):
                                                      if(paym=='Rajdhani Express INR1000.00'):
                                                               p=1000
                                                               mac='Rajdhani Express'
                                                      if(paym=='GaribRath Express INR650.00'):
                                                               p=650
                                                               mac='GaribRath Express'
                                                      if(paym=='Patna-Pune Superfast Express INR850.00'):
                                                               p=850
                                                               mac='Patna-Pune Superfast Express'
                                             if((x11=='Jaipur' and x21=='Patna') or (x11=='Patna' and x21=='Jaipur')):
                                                      if(paym=='Rajdhani Express INR900.00'):
                                                               p=900
                                                               mac='Rajdhani Express'
                                                      if(paym=='Shiv Shakti Express INR1000.00'):
                                                               p=1000
                                                               mac='ShivShakti Express'
                                                      if(paym=='AC Superfast Express INR950.00'):
                                                               p=950
                                                               mac='AC Superfast Express'
                                             if((x11=='Delhi' and x21=='Patna') or (x11=='Patna' and x21=='Delhi')):
                                                      if(paym=='Rajdhani Express INR900.00'):
                                                               p=900
                                                               mac='Rajdhani Express'
                                                      if(paym=='Festival Special Express INR900.00'):
                                                               p=900
                                                               mac='Festival Special Express'
                                                      if(paym=='Gatimaan Express INR1000.00'):
                                                               p=1000
                                                               mac='Gatimaan Express'
                                             newwil2.grid_forget()
                                             tkinter.Label(newwin,text="Redirecting You To Payment Gateway...",fg='black',bg='white'
                                                           ,font=('Times','18')).grid(row=n+2,column=2)
                                             newwin.after(4000,newwin.destroy)
                                             payway=tkinter.Tk()
                                             payway.title('Payment Window')
                                             payway.configure(bg='white')
                                             payway.geometry('1000x1000')
                                             payway.attributes('-fullscreen',True)
                                             payway.attributes('-topmost',True)
                                             tkinter.Label(payway,text="PAYMENT WINDOW",font=('Times','18','bold'),fg='black',bg='white').grid(row=1,column=2)
                                             s98="Welcome,dear "+str(myname)+"!"
                                             welcome1=tkinter.Label(payway,text=s98,font=('Times','18','bold'),fg='black',bg='white')
                                             welcome1.grid(row=2,column=2)
                                             tkinter.Label(payway,text='         ',font=('Times','18','bold'),fg='black',bg='white').grid(row=2,column=1)
                                             m78=p*n4
                                             s45="You have to pay INR"+str(m78)+" only. Request for an OTP,which will be sent to your mail."
                                             welcome2=tkinter.Label(payway,text=s45,font=('Times','18','bold'),fg='black',bg='white')
                                             welcome2.grid(row=3,column=2)
                                             tkinter.Label(payway,text=' ',font=('Times','18','bold'),fg='black',bg='white').grid(row=4,column=2)
                                             tkinter.Label(payway,text=' ',font=('Times','18','bold'),fg='black',bg='white').grid(row=3,column=1)
                                             def OTPver():
                                                      nonlocal lst
                                                      butotp.grid_forget()
                                                      n909=random.randint(100001,999997)
                                                      s=smtplib.SMTP('smtp.gmail.com',587)
                                                      s.starttls()
                                                      otps="Dear "+str(myname)+",\nYour Payment OTP is "+str(n909)+".No Railway employee will ask for this OTP."
                                                      s.login('dummyaman2004@gmail.com','eahk zxeg kwiy gvuc')
                                                      s.sendmail('&&&&&&&&&&&',myemail,otps)
                                                      s.close()
                                                      tkinter.Label(payway,text="Enter OTP here:",fg='black',bg='white'
                                                                    ,font=('Times','18')).grid(row=7,column=1)
                                                      verif=tkinter.Entry(payway,fg='black',bg='white',font=('Times','18'),show='*')
                                                      verif.grid(row=7,column=2)
                                                      buterif=tkinter.Button(payway,text="CANCEL PAYMENT",font=('Times','18'),fg='black',bg='green',
                                                                              activebackground='blue',command=payway.destroy)
                                                      buterif.grid(row=9,column=2)
                                                      up=tkinter.Label(payway,text=' ',font=('Times','18','bold'),fg='black',bg='white')
                                                      up.grid(row=10,column=2)
                                                      def veriCheck():
                                                               nonlocal lst
                                                               try:
                                                                        buterif.grid_forget()
                                                                        butverif.grid_forget()
                                                                        x=str(verif.get())
                                                                        x=int(x)
                                                                        if(n909==x):
                                                                                 np=random.randint(1000,2459)
                                                                                 up.configure(text="Successfully Authenticated... Ticket has been sent to your email...")
                                                                                 s=smtplib.SMTP('smtp.gmail.com',587)
                                                                                 s.starttls()
                                                                                 mes1="Payment Is Successful\n"
                                                                                 lstse=[]
                                                                                 for i in range(0,n4):
                                                                                          y=random.randint(10,99)
                                                                                          lstse.append(y)
                                                                                 for i in range(0,n4):
                                                                                          b=lst[i]
                                                                                          c=lstse[i]
                                                                                          mes1=mes1+"Seat number of "+str(b)+" is "+str(c)+" \n"
                                                                                 mes1=mes1+"Train Booked:"+str(mac)+".\n"
                                                                                 mes1=mes1+"Total Bill Generated:"+str(m78)+".\n"
                                                                                 mes1=mes1+"Date Of Journey:"+str(dater)+"/"+str(mon)+"/"+str(yr)+"\n"
                                                                                 mes1=mes1+"Departure Time of Train:"+str(np)+"hrs\n"
                                                                                 mes1=mes1+"Railway Corporation wishes You Safe Journey!\n"
                                                                                 s.login('dummyaman2004@gmail.com','eahk zxeg kwiy gvuc')
                                                                                 s.sendmail('&&&&&&&&&&&',myemail,mes1)
                                                                                 s.close()
                                                                                 payway.after(4000,payway.destroy)
                                                                        else:
                                                                                 up.configure(text="Please Enter Correct OTP!!")
                                                                                 buterif.grid(row=9,column=2)
                                                                                 butverif.grid(row=8,column=2)
                                                               except ValueError:
                                                                        up.configure(text="Please Enter A Valid Number!")
                                                                        
                                                                        
                                                      butverif=tkinter.Button(payway,text="VERIFY",font=('Times','18'),fg='black',bg='green',
                                                                              activebackground='blue',command=veriCheck)
                                                      butverif.grid(row=8,column=2)
                                                                                 
                                                      
                                             butotp=tkinter.Button(payway,text="REQUEST OTP",fg='black',bg='blue'
                                                                   ,font=('Times','18'),activebackground='blue',command=OTPver)
                                             butotp.grid(row=5,column=2)
                                             
                                             
                                             
                                             
                                             
                                             
                                    #Make give command button
                                    newwil=tkinter.Button(newwin,text='Select Train:',fg='black',bg='blue',activebackground='green',font=('Times','18')
                                                          ,command=TakPayment)
                                    newwil.grid(row=n,column=2)
                                    newwil2=tkinter.Button(newwin,text='Proceed To Payment',fg='black',bg='blue'
                                                           ,activebackground='green',font=('Times','18'),command=PaymentGate)
                                             
                           #Make taler button
                           button45=tkinter.Button(newwin,text='CONFIRM',bg='green',fg='black',font=('Times','18'),command=TakeinNames)
                           button45.grid(row=13,column=2)
                           
                           
                 
                                    

                  button77=tkinter.Button(newwin,text="CONFIRM",fg='black',bg='green',activebackground='green',command=TicketMaker,font=('Times','16'))
                  button77.grid(row=8,column=2)
                  button78=tkinter.Button(newwin,text="EXIT THIS PAGE",fg='black',bg='red',activebackground='red',command=newwin.destroy,font=('Times','16'))
                  button78.grid(row=10,column=2)
                  
         def Akcess():
                  button3.grid_forget()
                  button4.grid_forget()
                  mt=str(userid.get())
                  pw=str(pass1.get())
                  myn=mysql.connector.connect(host='localhost',user='root',passwd='aman@2004',database='py')
                  mycursor=myn.cursor()
                  mycursor.execute('select * from rail;')
                  x=mycursor.fetchall()
                  f=False
                  for i in x:
                           if(i[0].lower()==mt.lower() and i[1].lower()==pw.lower()):
                                    aks5.configure(text='Authentication Successful! You will be redirected to a new page...',fg='black')
                                    myn.close()
                                    f=True
                                    aks.after(3000,NewWin)
                  if(f==False):
                           aks5.configure(text="Authentication Unsuccessful! Please Try Again...",fg="red")
                           button3.grid(row=7,column=2)
                           button4.grid(row=9,column=2)



                  
         button3=tkinter.Button(aks,text="LOGIN",font=('Times','18'),fg='black',bg='green',activebackground='green',command=Akcess)
         button3.grid(row=7,column=3)
         aks6=tkinter.Label(aks,text="   ",font=('Times','14','bold'),fg='black',bg='white')
         aks6.grid(row=8,column=3)
         button4=tkinter.Button(aks,text="EXIT",font=('Times','18'),fg='black',bg='red',activebackground='red',command=aks.destroy)
         button4.grid(row=9,column=3)         

def RecoverAcc():
         reco=tkinter.Tk()
         reco.title('Recovery Menu')
         reco.configure(bg='white')
         reco.geometry('1000x1000')
         reco.attributes('-fullscreen',True)
         reco.attributes('-topmost',True)
         #make the labels to guide the people
         tkinter.Label(reco,text='RECOVERY MENU',fg='black',bg='white',font=('Times','18','bold')).grid(row=1,column=2)
         tkinter.Label(reco,text='     ',fg='black',bg='white',font=('Times','18','bold')).grid(row=1,column=1)
         tkinter.Label(reco,text='This Menu will help you get your password/username.',fg='black',bg='white',font=('Times','18','bold')).grid(row=2,column=2)
         tkinter.Label(reco,text='To do that, you need your EmailID and Name that you gave during account creation'
                       ,fg='black',bg='white',font=('Times','18','bold')).grid(row=3,column=2)
         tkinter.Label(reco,text='TYPE BELOW THE DETAILS:-',fg='black',bg='white',font=('Times','18','bold')).grid(row=4,column=2)
         Labe1=tkinter.Label(reco,text="Enter Your EmailID here:",fg='black',bg='white',font=('Times','16'),justify='right')
         Labe1.grid(row=6,column=1)
         Labe2=tkinter.Label(reco,text="Enter Your Name here:",fg='black',bg='white',font=('Times','16'),justify='right')
         Labe2.grid(row=7,column=1)
         #create tkinter entry boxes
         idmailen=tkinter.Entry(reco,font=('Times','16'),fg='black',bg='white')
         idmailen.grid(row=6,column=2)
         namen=tkinter.Entry(reco,font=('Times','16'),fg='black',bg='white')
         namen.grid(row=7,column=2)
         #create the update label
         userlabel=tkinter.Label(reco,text="   ",fg='black',bg='white',font=('Times','16'))
         userlabel.grid(row=11,column=2)
         passlabel=tkinter.Label(reco,text="",fg='black',bg='white',font=('Times','16'))
         passlabel.grid(row=12,column=2)
         buttonex=tkinter.Button(reco,text="EXIT",fg='black',bg='red',activebackground='red',font=('Times','18'),command=reco.destroy)
         buttonex.grid(row=10,column=2)
         #create the so called label functions that will process information
         def Reco():
                  buttonsub.grid_forget()
                  buttonex.grid_forget()
                  x=str(idmailen.get())
                  y=str(namen.get())
                  mycon=mysql.connector.connect(host='localhost',user='root',passwd='aman@2004',database='py')
                  mycursor=mycon.cursor()
                  mycursor.execute('select * from rail;')
                  allrec=mycursor.fetchall()
                  g=False
                  for i in allrec:
                           if(i[2]==x and i[3].lower()==y.lower()):
                                    userlabel.configure(text= ' ')
                                    otplabel=tkinter.Label(reco,text="To Make Sure It Is Really You, We Have Sent an OTP to Your Mail.Please Check It."
                                                           ,fg='black',bg='white',font=('Times','16'))
                                    otplabel.grid(row=13,column=2)
                                    otpenter=tkinter.Entry(reco,font=('Times','16'),fg='black',bg='white',show='*')
                                    otpenter.grid(row=14,column=2)
                                    otplabel2=tkinter.Label(reco,text="Enter Here The OTP:"
                                                           ,fg='black',bg='white',font=('Times','16'),justify='right')
                                    otplabel2.grid(row=14,column=1)
                                    nwe=random.randint(100001,999998)
                                    message1="Dear "+str(y)+",\nYour OTP for Recovery is "+str(nwe)+".\nNo Railway Employee will ask you for it."
                                    s=smtplib.SMTP('smtp.gmail.com',587)
                                    s.starttls()
                                    s.login('dummyaman2004@gmail.com','eahk zxeg kwiy gvuc')
                                    s.sendmail('&&&&&&&&&&&',str(x),message1)
                                    s.close()
                                    def Vali():
                                             x=str(otpenter.get())
                                             try:
                                                      x=int(x)
                                                      if(x==nwe):
                                                               bs.grid_forget()
                                                               otplabel.grid_forget()
                                                               otpenter.grid_forget()
                                                               otplabel2.grid_forget()
                                                               statement1="Your UserID is:"+str(i[0])
                                                               statement2="Your Password is:"+str(i[1])
                                                               userlabel.configure(text=statement1,fg='blue')
                                                               passlabel.configure(text=statement2,fg='blue')
                                                               buttonex.grid(row=10,column=2)
                                                      else:
                                                               statement1.configure(text="INVALID OTP! TRY AGAIN",fg='red')

                                             except ValueError:
                                                      statement1.configure(text="Please Enter A Reasonable OTP",fg='red')
                                                      tkMessageBox.showinfo("ERROR",'Please Enter A Reasonable OTP')
                                                      
                                    bs=tkinter.Button(reco,text="AUTHENTICATE OTP",font=('Times','16')
                                                      ,fg='black',bg='green',activebackground='green',command=Vali)
                                    bs.grid(row=15,column=2)
                                    g=True
                                    break
                                                      
         
                                    
                                    
                           
                  if(g==False):
                           userlabel.configure(text="Authentication Failed,Please Try Again!",fg='red')
                           buttonsub.grid(row=8,column=2)
                           buttonex.grid(row=10,column=2)
         
                  
         #Buttons
         buttonsub=tkinter.Button(reco,text="CHECK",fg='black',bg='blue',activebackground='blue',font=('Times','18'),command=Reco)
         buttonsub.grid(row=8,column=2)
         
#Make another option in the program for the betterment
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
#Addnew label for the program in here
#make a new function that can help us alter the funcgions          
                  

#Create BUTTONs for the betterment of nations
button132=tkinter.Button(main,text="CREATE ACCOUNT",fg="black",bg="green",activebackground="green",font=('Times','16'),command=CreateRailAcc)
button132.grid(row=5,column=2)
button133=tkinter.Button(main,text="BOOK A TICKET",fg="black",bg="blue",activebackground="green",font=('Times','16'),command=ReservationSys)
button133.grid(row=7,column=2)
button134=tkinter.Button(main,text="RECOVER MY ACCOUNT",fg="black",bg="yellow",activebackground="green",font=('Times','16'),command=RecoverAcc)
button134.grid(row=9,column=2)
button134=tkinter.Button(main,text="EXIT THIS PAGE",fg="black",bg="red",activebackground="green",font=('Times','16'),command=main.destroy)
button134.grid(row=13,column=2)
button134=tkinter.Button(main,text="SEND A FEEDBACK",fg="black",bg="pink",activebackground="green",font=('Times','16'),command=ratewindow)
button134.grid(row=11,column=2)
