from tkinter import *
import tkinter.messagebox

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            checkWin()
            player = "O"
            button["bg"] = "yellow"
      else :
            checkWin()
            player = "X"
            button["bg"] = "lightgreen"
            
def checkWin():
      if list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
            victory()
      elif list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
            victory()
      elif list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
            victory()
      elif list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
            victory()
      elif list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
            victory()
      elif list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
            victory()
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
            victory()
      elif list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
            victory()

def victory():
      if player == "X":
            tkinter.messagebox.showinfo("","X Win!")
            quit()
      else:
             tkinter.messagebox.showinfo("","O Win!")
             quit()
window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


