#import libraies
import tkinter as tk
import NT_User_Interface.NT_UI_Main
from NT_User_Interface.NT_UI_Error import ErrorGUI

#define node class used by the application, essentially just a linked list
class node():
    def __init__(self):
        self.name = ""
        self.IPAddress = []
        self.connectedNodes = []

def AddNode(nodes,node):
    nodes.append(node)

def NodeConstructor():
    return node()

#function to prevent the window from moving on refresh
def UpdateWindowLocation(UI,windowLocation):
    windowLocation[0],windowLocation[1]=UI.winfo_x(),UI.winfo_y()
    return windowLocation

#User interface for creating new nodes
def AddNodeGui(windowLocation,nodes):

    UI = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])

    UI.geometry("+"+windowX+"+"+windowY)

    #Configure Windows
    UI.title('Node-tool')
    UI.configure(bg="white")
    UI.resizable(False,False)
    #Node Name Input Section
    totalColums = 7

    UI.message = tk.Label(UI, bg="white",fg='black', font='Arial 10 bold', text="Enter Node Name")
    UI.message.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)

    UI.nodeNameEntry = tk.Entry(UI, width=20)
    UI.nodeNameEntry.grid(row = 1, column = 0, columnspan = totalColums, pady = 2)

    input_size = 10
    
    #Ip address Input Section
    UI.IPinputMessage = tk.Label(UI, bg="white", fg='black', font='Arial 10 bold',text="IP address for node")
    UI.IPinputMessage.grid(row = 3, column = 0, columnspan = totalColums, pady = 2)

    UI.IPaddressBit1 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit1.grid(row = 4, column = 0,  pady = 6)

    UI.dot1 = tk.Label(UI, bg="white", text=".")
    UI.dot1.grid(row = 4, column = 1,  pady = 4)

    UI.IPaddressBit2 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit2.grid(row = 4, column = 2,  pady = 6)

    UI.dot2 = tk.Label(UI, bg="white", text=".")
    UI.dot2.grid(row = 4, column = 3,  pady = 4)

    UI.IPaddressBit3 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit3.grid(row = 4, column = 4,  pady = 6)

    UI.dot3 = tk.Label(UI, bg="white",text=".")
    UI.dot3.grid(row = 4, column = 5,  pady = 4)

    UI.IPaddressBit4 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit4.grid(row = 4, column = 6,  pady = 6)

    def inputValdation(UI,nodes):

        nodeList = []
        for node in nodes:
            nodeList.append(node.name)

        invalid = False
        nodeNameCharacterLimit = 16
        nameInput = UI.nodeNameEntry.get()
        if(len(nameInput)==0):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Node name not entered")
                return False

        for node in nodes:
            if(node.name==nameInput):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Node "+nameInput+" Allready Exists")
                return False


        if(len(nameInput)>nodeNameCharacterLimit):
            ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Node Name Character limit Exceeded\n Character Limit : "+str(nodeNameCharacterLimit))
            return False
        
        octets = [UI.IPaddressBit1.get(),UI.IPaddressBit2.get(),UI.IPaddressBit3.get(),UI.IPaddressBit4.get()]

        for octet in octets:
            if(len(octet)==0):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"IP address Not entered")
                invalid = True
                break
            elif(not octet.isnumeric()):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Ip address must only contain numbers")
                invalid = True
                break
            elif(int(octet)>255 or int(octet)<0):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"One or more octets are out of range\n Range : 0-255")
                invalid = True
                break

        if(invalid == True):
            return False
        else:
            return True

    def CreateNode(UI,nodes):
        if (inputValdation(UI,nodes)):
            node = NodeConstructor()
            node.name = UI.nodeNameEntry.get()
            node.IPAddress = [UI.IPaddressBit1.get(),UI.IPaddressBit2.get(),UI.IPaddressBit3.get(),UI.IPaddressBit4.get()]
            AddNode(nodes,node)
            UpdateWindowLocation(UI,windowLocation)
            UI.destroy()
            NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)

    UI.confirmbutton = tk.Button(UI, width=16, fg="white", font='Arial 10 bold', bg='#18A1CC',text="Create Node", command=lambda:CreateNode(UI,nodes))
    UI.confirmbutton.grid(row = 6, column = 0, columnspan = 3, pady = 2)
    UI.cancelButton = tk.Button(UI, width=16 , fg='white', font='Arial 10 bold', bg='#18A1CC', text="Cancel", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                             UI.destroy(),
                                                                             NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    UI.cancelButton.grid(row = 6, column = 4, columnspan = 3, pady = 2)
 