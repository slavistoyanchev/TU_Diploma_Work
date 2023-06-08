import tkinter as tk


def open_window():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        if username == "admin" and password == "password":
            label_result.config(text="Вход успешен", fg="green")
            window.destroy()
        else:
            label_result.config(text="Грешно име или парола", fg="red")

    # Създаване на главното прозорец на приложението
    window = tk.Tk()
    window.title("Вход")
    window.geometry("300x200")

    # Създаване на етикети
    label_username = tk.Label(window, text="Потребителско име:")
    label_username.pack()

    # Създаване на поле за въвеждане на потребителско име
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Парола:")
    label_password.pack()

    # Създаване на поле за въвеждане на парола
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    # Създаване на бутон за вход
    button_login = tk.Button(window, text="Вход", command=login)
    button_login.pack()

    # Създаване на етикет за резултата от входа
    label_result = tk.Label(window, text="")
    label_result.pack()

    # Стартиране на главната нишка на приложението

    window.mainloop()
