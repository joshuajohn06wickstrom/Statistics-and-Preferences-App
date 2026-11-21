#imports

import PySimpleGUI as sgui

#Setting up the layout
home_layout = [[sgui.Text("Welcome to SpotiRick")], [sgui.Button("Login")], [sgui.Button("Exit")]]
login_layout = [[sgui.Text("Login to your account")], [sgui.InputText(key="username")], [sgui.InputText(key="password", password_char="*")], [sgui.Button("Submit")], [sgui.Button("Back")]]
#Creating the window
window = sgui.Window("SpotiRick", home_layout, size=(300, 200), resizable=True, finalize=True)
login = False
#Event loop
while True:
    event, values = window.read()
    
    if event == sgui.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Login":
        # Handle login logic here
        window.close()
        window = sgui.Window("SpotiRick", login_layout, size=(300, 200), resizable=True, finalize=True)
        login = True
        while login == True:
            event, values = window.read()
            if event == "Back":
                login = False
                window.close()
                window = sgui.Window("SpotiRick", home_layout, size=(300, 200), resizable=True, finalize=True)
            elif event == sgui.WINDOW_CLOSED:
                login = False
                break
        login = False

#Closing the window
window.close()
