from tkinter import *

root = Tk()

root.geometry('1270x690+0+0')  # Set up the window size
root.resizable(FALSE, FALSE)  # Remove option to resize the window

root.title('Информационна система Ресторант')
root.config(bg='#808000')  # Set the background color

top_frame = Frame(root, bd=10, relief=RIDGE, bg='#808000')
top_frame.pack(side=TOP)
label_title = Label(top_frame, text='Информационна система Ресторант',
                    font=('arial', 30, 'bold'), bd=9, fg='black', bg='#8A8841', width=51)
label_title.grid(row=0, column=0)

# Creating Frames
cost_frame = Frame(root, bd=10, relief=RIDGE)
cost_frame.pack(side=BOTTOM)

menu_frame = Frame(root, bd=7, relief=RIDGE, bg='#808000')
menu_frame.pack(side=LEFT)

food_frame = LabelFrame(menu_frame, text='Храна',
                        font=('arial', 19, 'italic'), bd=5, relief=RIDGE, fg='black')
food_frame.pack(side=LEFT)

drinks_frame = LabelFrame(menu_frame, text='Напитки', font=('arial', 19, 'bold'), bd=10, relief=RIDGE)
drinks_frame.pack(side=LEFT)

dessert_frame = LabelFrame(menu_frame, text='Десерти', font=('arial', 19, 'bold'), bd=10, relief=RIDGE)
dessert_frame.pack(side=LEFT)

right_frame = Frame(root, bd=15, relief=RIDGE)
right_frame.pack(side=RIGHT)

calculator_frame = Frame(right_frame, bd=1, relief=RIDGE)
calculator_frame.pack()

receipt_frame = Frame(right_frame, bd=4, relief=RIDGE)
receipt_frame.pack()

button_frame = Frame(right_frame, bd=3, relief=RIDGE)
button_frame.pack()

# Defining variables for food
salad_v = IntVar()
soup_v = IntVar()
fish_v = IntVar()
# Food Frame configure
salad = Checkbutton(food_frame, text='Салата',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=salad_v)
salad.grid(row=0, column=0, sticky=W)

soup = Checkbutton(food_frame, text='Супа',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=soup_v)
soup.grid(row=1, column=0, sticky=W)

fish = Checkbutton(food_frame, text='Риба',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=fish_v)
fish.grid(row=1, column=0, sticky=W)

root.mainloop()
