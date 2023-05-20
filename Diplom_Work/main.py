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
steak_v = IntVar()
normal_potatoes_v = IntVar()
sweet_potatoes_v = IntVar()
spaghetti_v = IntVar()
pizza_v = IntVar()
burger_v = IntVar()

# Food Frame configure
salad = Checkbutton(food_frame, text='Салата',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=salad_v)
salad.grid(row=0, column=0, sticky=W)

soup = Checkbutton(food_frame, text='Супа',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=soup_v)
soup.grid(row=1, column=0, sticky=W)

fish = Checkbutton(food_frame, text='Риба',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=fish_v)
fish.grid(row=2, column=0, sticky=W)

steak = Checkbutton(food_frame, text='Пържола',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=steak_v)
steak.grid(row=3, column=0, sticky=W)

normal_potatoes = Checkbutton(food_frame, text='Пържени картофи',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=normal_potatoes_v)
normal_potatoes.grid(row=4, column=0, sticky=W)

sweet_potatoes = Checkbutton(food_frame, text='Сладки картофи',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=sweet_potatoes_v)
sweet_potatoes.grid(row=5, column=0, sticky=W)

spaghetti = Checkbutton(food_frame, text='Спагети',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=spaghetti_v)
spaghetti.grid(row=6, column=0, sticky=W)

pizza = Checkbutton(food_frame, text='Пица',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=pizza_v)
pizza.grid(row=7, column=0, sticky=W)

burger = Checkbutton(food_frame, text='Бургер',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=burger_v)
burger.grid(row=8, column=0, sticky=W)


# Defining variables for drinks
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()

# Drink Frame configure
water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=0, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=1, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=2, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=3, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=4, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=5, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=6, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=7, column=1, sticky=W)

water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= water_v)
water.grid(row=8, column=1, sticky=W)


# Defining variables for desserts
cake_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()
water_v = IntVar()

# Drink Frame configure
cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=0, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=1, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=2, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=3, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=4, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=5, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=6, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=7, column=2, sticky=W)

cake = Checkbutton(dessert_frame, text='Торта',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable= cake_v)
cake.grid(row=8, column=2, sticky=W)


root.mainloop()
