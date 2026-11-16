#imports

import PySimpleGUI as sgui

#Setting up the layout
layout = [[sgui.Text("Welcome to SpotiRick")], [sgui.Button("Login")], [sgui.Button("Exit")]]

#Creating the window
window = sgui.Window("SpotiRick", layout, size=(300, 200), resizable=True, finalize=True)

#Event loop
while True:
    event, values = window.read()
    
    if event == sgui.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Login":
        # Handle login logic here
        pass 

#Closing the window
window.close()
