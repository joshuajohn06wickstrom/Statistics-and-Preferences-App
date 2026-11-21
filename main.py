#imports

import PySimpleGUI as sgui

sgui.theme_add_new("Spotify", {
    "BACKGROUND": "#121212",
    "TEXT": "#FFFFFF",
    "INPUT": "#282828",
    "TEXT_INPUT": "#FFFFFF",
    "SCROLL": "#282828",
    "BUTTON": ("#000000", "#1DB954"),   # (text colour, button colour)
    "PROGRESS": ("#1DB954", "#282828"),
    "BORDER": 0,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
})
sgui.theme("Spotify")
sgui.set_options(
    use_custom_titlebar=True,
    titlebar_background_color="#121212",
    titlebar_text_color="#1DB954",
    titlebar_font=("Helvetica", 11, "bold"),
)

home_screen = [
    [sgui.Text("Welcome to the Home Screen!")],
    [sgui.Button("Login")],
    [sgui.Button("Exit")]
]

login_screen = [
    [sgui.Text("Please enter your login credentials:")],
    [sgui.Text("Username:")],
    [sgui.Input(key="username")],
    [sgui.Text("Password:")],
    [sgui.Input(key="password", password_char="*")],
    [sgui.Button("Submit")],
    [sgui.Button("Back")]
]

layout = [
    [sgui.VPush()],
    [
    sgui.pin(sgui.Column(home_screen, key="HOME", visible=True, element_justification="center")),
    sgui.pin(sgui.Column(login_screen, key="LOGIN", visible=False, element_justification="center"))
],
[sgui.VPush()],
]

window = sgui.Window("SpotiRick", layout, size=(300, 500), resizable=True, finalize=True, element_justification="c")

def show_screen(name):
    for screen in ("HOME", "LOGIN"):
        window[screen].update(visible=(screen == name))
#main loop
while True:
    event, values = window.read()
    
    if event == sgui.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Login":
        show_screen("LOGIN")
    elif event == "Back":
        window["password"].update("")
        show_screen("HOME")
    elif event == "Submit":
        username = values["username"]
        password = values["password"]

#Closing the window
window.close()
