#import libraies
from tkinter import ttk
import tkinter as tk
import NT_User_Interface.NT_UI_Main
from NT_User_Interface.NT_UI_Error import ErrorGUI

def UpdateWindowLocation(UI,windowLocation):
    windowLocation[0],windowLocation[1]=UI.winfo_x(),UI.winfo_y()
    return windowLocation

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
def ConnectNodeGui(windowLocation,nodes,focusNode):
    #Create Higher level Window
    connectNodeWindow = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    connectNodeWindow.geometry("300x80"+"+"+windowX+"+"+windowY)
    connectNodeWindow.title('Connect Node')
    connectNodeWindow.configure(bg="white")
    windowMessage = tk.Label(connectNodeWindow,fg='white', font='Arial 10 bold', bg='#18A1CC',text = "Choose Node to connect")
    windowMessage.pack()

    nodeList = []
    for node in nodes:
        if(node.name == focusNode.name):
            None
        nodeList.append(node.name)

    connectedNodeList = []
    connectedNodeList.append(focusNode.name)
    for node in focusNode.connectedNodes:
        if(node.name == focusNode.name):
            None
        connectedNodeList.append(node.name)
        

    uniqueNodes = [x for x in nodeList if x not in connectedNodeList]

    connectNodeWindow.combo = ttk.Combobox(connectNodeWindow,state="readonly",values = uniqueNodes)
    connectNodeWindow.combo.pack()

    def CheckIfNullEntry():
        selectedNode = connectNodeWindow.combo.get()
        found = False
        for node in nodes:
            if(node.name == selectedNode):
                found = True
                focusNode.connectedNodes.append(node)
                node.connectedNodes.append(focusNode)
                UpdateWindowLocation(connectNodeWindow,windowLocation)
                connectNodeWindow.destroy()
                ChangeNodeConnectionsGui(windowLocation,nodes,focusNode)               
                break
        if(not found):
            ErrorGUI(UpdateWindowLocation(connectNodeWindow,windowLocation),"No Node Selected")

    connectButton = tk.Button(connectNodeWindow, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Connect", command=lambda:CheckIfNullEntry())
    connectButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(connectNodeWindow, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Cancel", command=lambda:(UpdateWindowLocation(connectNodeWindow,windowLocation),
                                                                                        connectNodeWindow.destroy(),
                                                                                        ChangeNodeConnectionsGui(windowLocation,nodes,focusNode)))
    cancelButton.pack(side=tk.LEFT)

#Define a function to close the window with confirmation window
def DisconnectNodeGui(windowLocation,nodes,focusNode):
    #Create Higher level Window
    disconnectNodeWindow = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    disconnectNodeWindow.geometry("300x80"+"+"+windowX+"+"+windowY)
    disconnectNodeWindow.configure(bg="white")
    disconnectNodeWindow.title('Remove Node')
    windowMessage = tk.Label(disconnectNodeWindow,fg='white', font='Arial 10 bold', bg='#18A1CC',text = "Choose Node to remove")
    windowMessage.pack()

    nodeList = []
    for node in focusNode.connectedNodes:
        if(node.name == focusNode.name):
            None
        nodeList.append(node.name)

    disconnectNodeWindow.combo = ttk.Combobox(disconnectNodeWindow,state="readonly",values = nodeList)
    disconnectNodeWindow.combo.pack()

    def CheckIfNullEntry():
        selectedNode = disconnectNodeWindow.combo.get()
        found = False
        for node in nodes:
            if(node.name == selectedNode):
                found = True
                focusNode.connectedNodes.remove(node)
                node.connectedNodes.remove(focusNode)
                UpdateWindowLocation(disconnectNodeWindow,windowLocation)
                disconnectNodeWindow.destroy()
                ChangeNodeConnectionsGui(windowLocation,nodes,focusNode)               
                break
        if(not found):
                ErrorGUI(UpdateWindowLocation(disconnectNodeWindow,windowLocation),"No Node Selected")

    deleteButton = tk.Button(disconnectNodeWindow, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Delete", command=lambda:CheckIfNullEntry())
    deleteButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(disconnectNodeWindow, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Cancel", command=lambda:(UpdateWindowLocation(disconnectNodeWindow,windowLocation),
                                                                                        disconnectNodeWindow.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    cancelButton.pack(side=tk.LEFT)
    

#Define a function to close the window with confirmation window
def ChangeNodeConnectionsGui(windowLocation,nodes,focusNode):
    #Create Higher level Window
    UI = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    UI.geometry("+"+windowX+"+"+windowY)
    UI.title('Modify Node connections')
    UI.title('Remove Node')

    connectedNodeList = []
    for node in focusNode.connectedNodes:
        connectedNodeList.append(node.name)

    #Node Name Input Section
    totalColums = 3

    UI.windowMessage = tk.Label(UI,fg='white', font='Arial 10 bold', bg='#18A1CC',text = "Chosen Node")
    UI.windowMessage.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)
    UI.windowMessage = tk.Label(UI,text = focusNode.name)
    UI.windowMessage.grid(row = 1, column = 0, columnspan = totalColums, pady = 2)

    UI.windowMessage3 = tk.Label(UI,fg='white', font='Arial 10 bold', bg='#18A1CC',text = "Connected Nodes")
    UI.windowMessage3.grid(row = 2, column = 0, columnspan = totalColums, pady = 2)

    UI.windowMessage4 = tk.Label(UI,fg='white', font='Arial 10 bold', bg='#18A1CC',text = str(connectedNodeList))
    UI.windowMessage4.grid(row = 3, column = 0, columnspan = totalColums, pady = 2)

    UI.Addbutton = tk.Button(UI, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Connect a node", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                                UI.destroy(),
                                                                                ConnectNodeGui(windowLocation,nodes,focusNode)))
    UI.Addbutton.grid(row = 4, column = 0, pady = 2)
    UI.Removebutton = tk.Button(UI, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Disconnect a node", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                                 UI.destroy(),
                                                                                 DisconnectNodeGui(windowLocation,nodes,focusNode)))
    UI.Removebutton.grid(row = 4, column = 1, pady = 2)
    UI.cancelButton = tk.Button(UI, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Back", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                             UI.destroy(),
                                                                             NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    UI.cancelButton.grid(row = 4, column = 2, pady = 2)

#Define a function to close the window with confirmation window
def NodeConnectionsGui(windowLocation,nodes):

    #Create Higher level Window
    UI = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    UI.geometry("300x80"+"+"+windowX+"+"+windowY)
    UI.configure(bg="white")
    UI.title('Select Node')
    UI.windowMessage = tk.Label(UI,fg='white', font='Arial 10 bold', bg='#18A1CC',text = "Choose a node to change")
    UI.windowMessage.pack()

    nodeList = []
    for node in nodes:
        nodeList.append(node.name)

    UI.combo = ttk.Combobox(UI,state="readonly",values = nodeList)
    UI.combo.pack()

    def CheckIfNullEntry(UI,windowLocation,nodes):
        selectedNode = UI.combo.get()
        found = False
        for node in nodes:
            if(node.name == selectedNode):
                found = True
                #pass through Target Node
                ChangeNodeConnectionsGui(UpdateWindowLocation(UI,windowLocation),nodes,node)
                UI.destroy()
                break
        if(not found):
            ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No Node Selected")

    configureButton = tk.Button(UI, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Select", command=lambda:CheckIfNullEntry(UI,windowLocation,nodes))
    configureButton.pack(side=tk.LEFT)

    cancelButton = tk.Button(UI, width=20 ,fg='white', font='Arial 10 bold', bg='#18A1CC',text="Cancel", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                                        UI.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    cancelButton.pack(side=tk.LEFT)