#import libraies
from tkinter import ttk
import tkinter as tk
import NT_User_Interface.NT_UI_Main
from NT_User_Interface.NT_UI_Error import ErrorGUI

#function to prevent the window from moving on refresh
def UpdateWindowLocation(UI,windowLocation):
    windowLocation[0],windowLocation[1]=UI.winfo_x(),UI.winfo_y()
    return windowLocation

#This tool essentally creates a copy of the node, fills the ui with the information,
#then deletes the old node creating a new one in its place
class node():
    def __init__(self):
        self.name = ""
        self.IPAddress = []
        self.connectedNodes = []

def AddNode(nodes,node):
    nodes.append(node)

def NodeConstructor():
        return node()

#Define a function to close the window with confirmation window
def EditNodeGui(windowLocation,nodes,nodeName):
    for node in nodes:
        if( node.name == nodeName):
            targetNode = node
            break    
    #Create Higher level Window
    UI = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    UI.geometry("+"+windowX+"+"+windowY)
    UI.configure(bg="white")
    UI.title('Modify Existing Node')

    #Node Name Input Section
    totalColums = 7

    UI.windowMessage = tk.Label(UI,bg="white",fg='black', font='Arial 10 bold',text = "Chosen Node")
    UI.windowMessage.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)
    UI.windowMessage = tk.Label(UI,text = targetNode.name)
    UI.windowMessage.grid(row = 1, column = 0, columnspan = totalColums, pady = 2)


    UI.windowMessage3 = tk.Label(UI,bg="white",fg='black', font='Arial 10 bold',text = "Node Name")
    UI.windowMessage3.grid(row = 2, column = 0, columnspan = totalColums, pady = 2)
    nodeName = tk.StringVar(UI, value=str(targetNode.name))
    UI.nodeNameEntry = tk.Entry(UI, textvariable=nodeName, width=20)
    UI.nodeNameEntry.grid(row = 3, columnspan = totalColums, column = 0, pady = 2)



    input_size = 10

    #Ip address Input Section
    UI.IPinputMessage = tk.Label(UI, bg="white",fg='black', font='Arial 10 bold',text="IP address for node")
    UI.IPinputMessage.grid(row = 4, column = 0, columnspan = totalColums, pady = 2)

    oct1 = tk.StringVar(UI, value=str(targetNode.IPAddress[0]))
    UI.IPaddressBit1 = tk.Entry(UI,textvariable=oct1, width=input_size)
    UI.IPaddressBit1.grid(row = 5, column = 0,  pady = 2)

    UI.dot1 = tk.Label(UI,bg='white',text=".")
    UI.dot1.grid(row = 5, column = 1,  pady = 2)

    oct2 = tk.StringVar(UI, value=str(targetNode.IPAddress[1]))
    UI.IPaddressBit2 = tk.Entry(UI,textvariable=oct2, width=input_size)
    UI.IPaddressBit2.grid(row = 5, column = 2,  pady = 2)

    UI.dot2 = tk.Label(UI,bg='white',text=".")
    UI.dot2.grid(row = 5, column = 3,  pady = 2)

    oct3 = tk.StringVar(UI, value=str(targetNode.IPAddress[2]))
    UI.IPaddressBit3 = tk.Entry(UI,textvariable=oct3, width=input_size)
    UI.IPaddressBit3.grid(row = 5, column = 4,  pady = 2)

    UI.dot3 = tk.Label(UI,bg='white',text=".")
    UI.dot3.grid(row = 5, column = 5,  pady = 2)

    oct4 = tk.StringVar(UI, value=str(targetNode.IPAddress[3]))
    UI.IPaddressBit4 = tk.Entry(UI,textvariable=oct4, width=input_size)
    UI.IPaddressBit4.grid(row = 5, column = 6,  pady = 2)

    def inputValdation(UI,nodes):

        nodeList = []
        for node in nodes:
            if(node.name == targetNode.name):
                None
            else:
                nodeList.append(node.name)

        invalid = False
        nodeNameCharacterLimit = 16
        nameInput = UI.nodeNameEntry.get()
        if(len(nameInput)==0):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Node name not entered")
                return False
            
        for node in nodeList:
            if(node==nameInput):
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
            nodes.remove(targetNode)
            return True

    def CreateNode(UI,nodes):
        if (inputValdation(UI,nodes)):
            octets = [UI.IPaddressBit1.get(),UI.IPaddressBit2.get(),UI.IPaddressBit3.get(),UI.IPaddressBit4.get()]
            IPaddress = octets
            node = NodeConstructor()
            node.name = UI.nodeNameEntry.get()
            node.IPAddress = IPaddress
            AddNode(nodes,node)
            UpdateWindowLocation(UI,windowLocation)
            UI.destroy()
            NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)

    UI.confirmbutton = tk.Button(UI, width=16, fg='white', font='Arial 10 bold', bg='#18A1CC', text="Apply", command=lambda:CreateNode(UI,nodes))
    UI.confirmbutton.grid(row = 6, column = 0, columnspan = 3, pady = 2)
    UI.cancelButton = tk.Button(UI, width=16 ,fg='white', font='Arial 10 bold', bg='#18A1CC', text="Cancel", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                             UI.destroy(),
                                                                             NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    UI.cancelButton.grid(row = 6, column = 4, columnspan = 3, pady = 2)

def CheckIfNullEntry(UI,windowLocation,nodes):
    selectedNode = UI.combo.get()
    found = False
    for node in nodes:
        if(node.name == selectedNode):
            found = True
            EditNodeGui(UpdateWindowLocation(UI,windowLocation),nodes,selectedNode)
            UI.destroy()
            break
    if(not found):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No Node Selected")

#Define a function to close the window with confirmation window
def ModifyNodeGui(windowLocation,nodes):
    #Create Higher level Window
    UI = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    UI.geometry("300x80"+"+"+windowX+"+"+windowY)
    UI.configure(bg="white")
    UI.title('Modify Node')
    UI.windowMessage = tk.Label(UI, bg="white",fg='black', font='Arial 10 bold', text = "Choose Node to Modify")
    UI.windowMessage.pack()

    nodeList = []
    for node in nodes:
        nodeList.append(node.name)

    UI.combo = ttk.Combobox(UI,state="readonly",values = nodeList)
    UI.combo.pack()

    configureButton = tk.Button(UI, width=20,fg='white', font='Arial 10 bold', bg='#18A1CC' ,text="Select", command=lambda:CheckIfNullEntry(UI,windowLocation,nodes))
    configureButton.pack(side=tk.LEFT)

    cancelButton = tk.Button(UI, width=20,fg='white', font='Arial 10 bold', bg='#18A1CC' ,text="Cancel", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                                        UI.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    cancelButton.pack(side=tk.LEFT)