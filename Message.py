#  A sample message with Tkinter 
import Tkinter 
import tkMessageBox

root=Tkinter.Tk()
root.withdraw

vote=tkMessageBox.askyesno('vote','Do you love python')
print(vote)