from tkinter import *
from tkinter import messagebox
import operator
import pandas as pd
import numpy as np

teams = dict()
window = Tk()

window.title("Hult Prize")

p1= PhotoImage(file='LOGO.png')
window.iconphoto(False, p1)
window.geometry("400x700")
window.minsize(200,200)
window.maxsize(600,600)
window['background'] = '#AA336A'

label_team = Label(window,text='The team name',bg='pink')
label_team.grid(row=0,column=0)
entry_team = Entry(window)
entry_team.grid(row=0,column=1)

label_Shadwa = Label(window,text='     First Score    ',bg='pink')
label_Shadwa.grid(row=1,column=0)
entry_shadwa = Entry(window)
entry_shadwa.grid(row=1,column=1)

label_refaat = Label(window,text='  Second Score  ',bg='pink')
label_refaat.grid(row=2,column=0)
entry_refaat = Entry(window)
entry_refaat.grid(row=2,column=1)

label_abdelaziz = Label(window,text='    Third Score    ',bg='pink')
label_abdelaziz.grid(row=3,column=0)
entry_abdelaziz = Entry(window)
entry_abdelaziz.grid(row=3,column=1)

label_okasha = Label(window,text='   Fourth Score   ',bg='pink')
label_okasha.grid(row=4,column=0)
entry_okasha = Entry(window)
entry_okasha.grid(row=4,column=1)
teamsNumber=Label(window,text='Teams you entered')
teamsNumber.grid(row=5,column=2)



def enter():
    try:
        name = str(entry_team.get())
        first_score = int(entry_shadwa.get())
        second_score = int(entry_refaat.get())
        third_score = int(entry_abdelaziz.get())
        fourth_score = int(entry_okasha.get())
    except ValueError:
        messagebox.showerror('Error',' You must enter a valid value -String for the team name and an integers for the scores-')
        assert("Invalid Input (Type Error)")
    if first_score not in range(0,21) :
        messagebox.showerror('Invalid Score Input','Your Score Input must be in range 0-20')
        return ValueError
    if second_score not in range(0,21) :
        messagebox.showerror('Invalid Score Input','Your Score Input must be in range 0-20')
        return ValueError
    if third_score not in range(0,21) :
        messagebox.showerror('Invalid Score Input','Your Score Input must be in range 0-20')
        return ValueError
    if fourth_score not in range(0,21) :
        messagebox.showerror('Invalid Score Input','Your Score Input must be in range 0-20')
        return ValueError
    
    teams[name] = first_score + second_score + third_score + fourth_score
    print(teams)
    teamsNL.configure(text= len(teams.values()))
    
teamsNL=Label(window,text=f'{len(teams.values())}')
teamsNL.grid(row=5,column=3)
enterbutton = Button(window, text='Enter', command=enter)
enterbutton.grid(row=5,column=0)




sortedteams =dict()

def showsorted(sortedteams):
    for i,key in enumerate(sortedteams.keys()):
        if i <3:
            teami= Label(window,text=f'{i+1}){key} Score= {sortedteams[key]}',bg='gold')
        else:
            teami= Label(window,text=f'{i+1}){key} Score= {sortedteams[key]}')
        teami.grid(row=i+8,column=1)
        
def sort():
    if len(teams.values())==0:
        messagebox.showerror("Error",'You have not enter any team')
        return TypeError
    global sortedteams
    sortedteams = dict(sorted(teams.items(),key=operator.itemgetter(1),reverse=True))
    showsorted(sortedteams)
    print(sortedteams)

sortbutton = Button(window,text='Sort',command=sort)
sortbutton.grid(row=5,column=1)

def save():
    global sortedteams
    if len(sortedteams.values())==0:
        messagebox.showerror('Error','You have not enter any team')
        return TypeError
    Names = list(sortedteams.keys())
    Scores = list(sortedteams.values())
    big_L = [[Names[i],Scores[i]] for i in range(len(Names))]
    data = pd.DataFrame(np.array(big_L),columns= ['Team Name','Score'])
    data.to_csv('Teams.csv')


savebutton = Button(window, text='Save In csv',command=save,height=1,width=10)
savebutton.grid(row=6,column=1)

window.mainloop()