import tkinter as tk

#Define a function to close the window with confirmation window
def ErrorGUI(windowLocation,ErrorMessage):
    #Create Higher level Window
   
    errorWindow = tk.Toplevel()
    windowX = str(windowLocation[0]+20)
    windowY = str(windowLocation[1]+40)
    errorWindow.geometry("300x80"+"+"+windowX+"+"+windowY)
    errorWindow.title('Error')
    errorWindow.configure(bg="white")

    warningMessage = tk.Label(errorWindow, bg="white", text="Error : "+ErrorMessage)
    warningMessage.pack()
    Button = tk.Button(errorWindow, width=20, fg='white', font='Arial 10 bold', bg='#18A1CC' ,text="Ok", command=lambda:errorWindow.destroy())
    Button.pack()
