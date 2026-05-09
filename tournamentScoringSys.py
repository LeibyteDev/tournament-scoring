import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

tournamentTeams=[]
tournamentIndividuals=[]
tournamentActivities=["Quiz","Chess","Football","Basketball","Sudoku"]

# Add teams window
def teamsWindow():
 team=Toplevel()
 team.grab_set()
 team.title("Add Teams")
 team.resizable(False,False)
 team.configure(background="#1e1e1e")
 Label(team,text="Add Teams",fg="white",background="#1e1e1e",font=("",15,"bold")).pack(pady=15)
 Label(team,text="Please input team names, separated by commas (,)\n(e.g. Team 1, Team 2, Team 3)",fg="white",background="#1e1e1e",font=("",12)).pack(padx=30)
 Label(team,text="You can add up to 4 teams.",fg="white",background="#1e1e1e",font=("",12,"bold")).pack()
 teamEntry=Entry(team,width=50) # Team entry field
 teamEntry.pack(pady=5)

 def saveTeamInput(): # Saves input from add teams window
   teamInput=teamEntry.get()
   if teamInput=="":
       messagebox.showerror("Error","You cannot save without inputting team(s).")
   else:
       global tournamentTeams
       addedTeams=[name.strip() for name in teamInput.split(",") if name.strip()]
       if len(tournamentTeams)+len(addedTeams)>4: # If amount of teams inputted exceeds 4 at any time
           messagebox.showerror("Error","You cannot add more than 4 teams.")
       else:
           tournamentTeams.extend(addedTeams)
           teamCount.config(text=f"Teams: {len(tournamentTeams)}/4") # Update count on main
           messagebox.showinfo("Success",f"Team(s): {tournamentTeams}")
           if len(tournamentTeams)==4:
               addTeamButton.config(state=DISABLED)
               print(teamInput) # debug
               team.destroy()
           else:
               print(teamInput) # debug
               team.destroy()

 Button(team,text="Save",font=("",12,"bold"),command=saveTeamInput).pack(pady=10)
 Button(team,text="Close",font=("",12),command=team.destroy).pack(pady=20)

# Add individuals window
def individualsWindow():
 indiv=Toplevel()
 indiv.grab_set()
 indiv.resizable(False,False)
 indiv.title("Add Individuals")
 indiv.configure(background="#1e1e1e")
 Label(indiv,text="Add Individuals",fg="white",background="#1e1e1e",font=("",15,"bold")).pack(pady=15)
 Label(indiv,text="Please input individual names, separated by commas (,)\n(e.g. Name 1, Name 2, Name 3)",fg="white",background="#1e1e1e",font=("",12)).pack(padx=30)
 Label(indiv,text="You can add up to 20 individuals.",fg="white",background="#1e1e1e",font=("",12,"bold")).pack()
 indivEntry=Entry(indiv,width=50) # Indiv entry field
 indivEntry.pack(pady=5)

 def saveIndivInput(): # Saves input from add individuals window
   indivInput=indivEntry.get()
   if indivInput=="":
       messagebox.showerror("Error","You cannot save without inputting individual(s).")
   else:
       global tournamentIndividuals
       addedIndiv=[name.strip() for name in indivInput.split(",") if name.strip()]
       if len(tournamentIndividuals)+len(addedIndiv)>20: # If amount of individuals exceeds 20 at any time
           messagebox.showerror("Error","You cannot add more than 20 individuals.")
       else:
           tournamentIndividuals.extend(addedIndiv)
           indivCount.config(text=f"Individuals: {len(tournamentIndividuals)}/20") # Update count on main
           messagebox.showinfo("Success",f"Individuals(s): {tournamentIndividuals}")
           if len(tournamentIndividuals)==20:
               addIndivButton.config(state=DISABLED)
               print(indivInput) # debug
               indiv.destroy()
           else:
               print(indivInput) # debug
               indiv.destroy()
       
 Button(indiv,text="Save",font=("",12,"bold"),command=saveIndivInput).pack(pady=10)
 Button(indiv,text="Close",font=("",12),command=indiv.destroy).pack(pady=20)

# Scoreboard window
def scoreboardWindow():
 sboard=Toplevel()
 sboard.grab_set()
 sboard.geometry("750x500")
 sboard.resizable(False,False)
 sboard.title("Scoreboard")
 sboard.configure(background="#1e1e1e")
 Label(sboard,text="Scoreboard",fg="white",background="#1e1e1e",font=("",15,"bold")).pack(pady=15)
 sboardTable=ttk.Treeview(sboard)
 sboardTable["columns"]=("Name","Type",*tournamentActivities,"Total Score","Final Score")
 sboardTable.column("#0",width=0,stretch=tk.NO)
 sboardTable.column("Name",anchor=tk.W,width=25)
 sboardTable.heading("Name",text="Name",anchor=tk.W)
 sboardTable.column("Type",anchor=tk.W,width=25)
 sboardTable.heading("Type",text="Type",anchor=tk.W)
 for activityInput in tournamentActivities:
     sboardTable.column(activityInput,anchor=tk.W,width=25)
     sboardTable.heading(activityInput,text=activityInput,anchor=tk.W)
 sboardTable.column("Total Score",anchor=tk.W,width=25)
 sboardTable.heading("Total Score",text="Total Score",anchor=tk.W)
 sboardTable.column("Final Score",anchor=tk.W,width=25)
 sboardTable.heading("Final Score",text="Final Score",anchor=tk.W)
 sboardData=[]
 def scoreGeneration(): # Generates the scores (activity scores are random for demo)
     activityScore=[random.randint(0,100)for _ in tournamentActivities]
     totalScore=sum(activityScore)
     finalScore=sum(activityScore) # temporary
     return activityScore,totalScore,finalScore
 for name in tournamentTeams:
     activityScore,totalScore,finalScore=scoreGeneration()
     sboardRow=[name,"Team"]+activityScore+[totalScore,finalScore]
     sboardData.append(tuple(sboardRow))
 for name in tournamentIndividuals:
     activityScore,totalScore,finalScore=scoreGeneration()
     sboardRow=[name,"Individual"]+activityScore+[totalScore,finalScore]
     sboardData.append(tuple(sboardRow))
 for sboardRow in sboardData:
     sboardTable.insert("","end",values=sboardRow)
 sboardTable.pack(expand=True,fill=tk.BOTH,padx=25) 
 Button(sboard,text="Close",font=("",12),command=sboard.destroy).pack(pady=20) 

# Start (main) window
if __name__ == "__main__":
 start=Tk()
 start.resizable(False,False)
 start.title("Tournament Scoring System")
 start.configure(background="#1e1e1e")
 Label(start,text="Tournament\nScoring System",fg="white",background="#1e1e1e",font=("",20,"bold")).pack(pady=25,padx=50)
 addTeamButton=Button(start,text="Add Teams",font=("",13,"bold"),command=teamsWindow)
 addTeamButton.pack()
 Label(start,text="Add teams to the tournament",fg="white",background="#1e1e1e",font=("",12)).pack()
 Label(start,text="",fg="#1e1e1e",background="#1e1e1e").pack()
 addIndivButton=Button(start,text="Add Individuals",font=("",13,"bold"),command=individualsWindow)
 addIndivButton.pack()
 Label(start,text="Add individuals to the tournament",fg="white",background="#1e1e1e",font=("",12)).pack()
 Label(start,text="",fg="#1e1e1e",background="#1e1e1e").pack()
 sboardButton=Button(start,text="Scoreboard",font=("",13,"bold"),command=scoreboardWindow)
 sboardButton.pack()
 Label(start,text="View the tournament scoreboard",fg="white",background="#1e1e1e",font=("",12)).pack()
 Label(start,text="",fg="#1e1e1e",background="#1e1e1e").pack(pady=5)
 Label(start,text="Participant Count",fg="white",background="#1e1e1e",font=("",13)).pack()
 teamCount=Label(start,text=f"Teams: {len(tournamentTeams)}/4",fg="white",background="#1e1e1e",font=("",11,"bold")) # Team and individual counts w/limits
 teamCount.pack()
 indivCount=Label(start,text=f"Individuals: {len(tournamentIndividuals)}/20",fg="white",background="#1e1e1e",font=("",11,"bold"))
 indivCount.pack()
 Label(start,text="",fg="#1e1e1e",background="#1e1e1e").pack(pady=5)
 Button(start,text="Exit",font=("",12),command=start.destroy).pack()
 Label(start,text="",fg="#1e1e1e",background="#1e1e1e").pack(pady=10)
