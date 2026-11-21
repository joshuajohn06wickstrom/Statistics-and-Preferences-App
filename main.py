#imports

import PySimpleGUI as sgui

#Home Window Function
def home_window():
    layout = [
        [sgui.Text("Welcome to SpotiRick")],
        [sgui.Button("Login")],
        [sgui.Button("Exit")]
    ]
    return sgui.Window("SpotiRick", layout, size=(300, 500), resizable=True, finalize=True)

def login_window():
    layout = [
        [sgui.Text("Login to SpotiRick")],
        [sgui.Text("Username"), sgui.Input(key="username")],
        [sgui.Text("Password"), sgui.Input(key="password", password_char="*")],
        [sgui.Button("Submit"), sgui.Button("Back")]
    ]
    return sgui.Window("Login", layout, size=(300, 500), resizable=True, finalize=True)

#making the home window
window = home_window()
#main loop
while True:
    event, values = window.read()
    
    if event == sgui.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Login":
        window.close()
        window = login_window()
    elif event == "Back":
        window.close()
        window = home_window()
    elif event == "Submit":
        username = values["username"]
        password = values["password"]

#Closing the window
window.close()
