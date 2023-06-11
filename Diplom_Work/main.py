import login

login.open_window()
if login.status:
    import menu_gui

    menu_gui.open_new_window()
