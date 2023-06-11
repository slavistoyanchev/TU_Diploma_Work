import tkinter as tk

status = False


def open_window():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        if username == "admin" and password == "password":
            global status
            status = True
            window.destroy()
        else:
            label_result.config(text="Грешно име или парола", fg="red")

    # Create main window
    window = tk.Tk()
    window.title("Вход")
    window.geometry("300x200")

    # Create username  and password label
    label_username = tk.Label(window, text="Потребителско име:")
    label_username.pack()

    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Парола:")
    label_password.pack()

    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    # Create Login button
    button_login = tk.Button(window, text="Вход", command=login)
    button_login.pack()

    label_result = tk.Label(window, text="")
    label_result.pack()

    # Start the window
    window.mainloop()
