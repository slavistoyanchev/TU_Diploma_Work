
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

drinks_frame = LabelFrame(menu_frame, text='Напитки', font=('arial', 19, 'italic'), bd=10, relief=RIDGE)
drinks_frame.pack(side=LEFT)

dessert_frame = LabelFrame(menu_frame, text='Десерти', font=('arial', 19, 'italic'), bd=10, relief=RIDGE)
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

# Defining variables for text of the food
text_salad_v = StringVar()
text_soup_v = StringVar()
text_fish_v = StringVar()
text_steak_v = StringVar()
text_normal_potatoes_v = StringVar()
text_sweet_potatoes_v = StringVar()
text_spaghetti_v = StringVar()
text_pizza_v = StringVar()
text_burger_v = StringVar()

# Entry fields for Food
text_salad = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_salad_v)
text_salad.grid(row=0, column=1)

text_soup = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_soup_v)
text_soup.grid(row=1, column=1)

text_steak = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_fish_v)
text_steak.grid(row=2, column=1)

text_salad = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_steak_v)
text_salad.grid(row=3, column=1)

text_normal_potatoes = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                             textvariable=text_normal_potatoes_v)
text_normal_potatoes.grid(row=4, column=1)

text_sweet_potatoes = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                            textvariable=text_sweet_potatoes_v)
text_sweet_potatoes.grid(row=5, column=1)

text_spaghetti = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_spaghetti_v)
text_spaghetti.grid(row=6, column=1)

text_pizza = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_pizza_v)
text_pizza.grid(row=7, column=1)

text_burger = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_burger_v)
text_burger.grid(row=8, column=1)

# Defining variables for drinks
water_v = IntVar()
coke_v = IntVar()
ice_tea_v = IntVar()
sparkling_water_v = IntVar()
whisky_v = IntVar()
red_wine_v = IntVar()
white_wine_v = IntVar()
vodka_v = IntVar()
lemonade_v = IntVar()

# Drink Frame configure
water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=water_v)
water.grid(row=0, column=0, sticky=W)

coke = Checkbutton(drinks_frame, text='Кола',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=coke_v)
coke.grid(row=1, column=0, sticky=W)

ice_tea = Checkbutton(drinks_frame, text='Студен чай',
                      font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=ice_tea_v)
ice_tea.grid(row=2, column=0, sticky=W)

sparkling_water = Checkbutton(drinks_frame, text='Газирана вода',
                              font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=sparkling_water_v)
sparkling_water.grid(row=3, column=0, sticky=W)

whisky = Checkbutton(drinks_frame, text='Уиски',
                     font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=whisky_v)
whisky.grid(row=4, column=0, sticky=W)

red_wine = Checkbutton(drinks_frame, text='Червено вино',
                       font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=red_wine_v)
red_wine.grid(row=5, column=0, sticky=W)

white_wine = Checkbutton(drinks_frame, text='Бяло вино',
                         font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=white_wine_v)
white_wine.grid(row=6, column=0, sticky=W)

vodka = Checkbutton(drinks_frame, text='Водка',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=vodka_v)
vodka.grid(row=7, column=0, sticky=W)

lemonade = Checkbutton(drinks_frame, text='Лимонада',
                       font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=lemonade_v)
lemonade.grid(row=8, column=0, sticky=W)

# Defining variables for text of the drinks
text_water_v = StringVar()
text_coke_v = StringVar()
text_ice_tea_v = StringVar()
text_sparkling_water_v = StringVar()
text_whisky_v = StringVar()
text_red_wine_v = StringVar()
text_white_wine_v = StringVar()
text_vodka_v = StringVar()
text_lemonade_v = StringVar()

# Entry fields for Drinks
text_water = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_water_v)
text_water.grid(row=0, column=1)

text_coke = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_coke_v)
text_coke.grid(row=1, column=1)

text_ice_tea = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                     textvariable=text_ice_tea_v)
text_ice_tea.grid(row=2, column=1)

text_sparkling_water = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                             textvariable=text_sparkling_water_v)
text_sparkling_water.grid(row=3, column=1)

text_whisky = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_whisky_v)
text_whisky.grid(row=4, column=1)

text_red_wine = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                      textvariable=text_red_wine_v)
text_red_wine.grid(row=5, column=1)

text_white_wine = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                        textvariable=text_white_wine_v)
text_white_wine.grid(row=6, column=1)

text_vodka = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_vodka_v)
text_vodka.grid(row=7, column=1)

text_lemonade = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                      textvariable=text_lemonade_v)
text_lemonade.grid(row=8, column=1)

# Defining variables for desserts
strawberry_cake_v = IntVar()
biscuit_cake_v = IntVar()
brownie_v = IntVar()
souffle_v = IntVar()
pie_v = IntVar()
ice_cream_v = IntVar()
milkshake_v = IntVar()
fondue_v = IntVar()
fruits_v = IntVar()

# Dessert Frame configure
strawberry_cake = Checkbutton(dessert_frame, text='Ягодова торта',
                              font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=strawberry_cake_v)
strawberry_cake.grid(row=0, column=0, sticky=W)

biscuit_cake = Checkbutton(dessert_frame, text='Бисквитена торта',
                           font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=biscuit_cake_v)
biscuit_cake.grid(row=1, column=0, sticky=W)

brownie = Checkbutton(dessert_frame, text='Брауни',
                      font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=brownie_v)
brownie.grid(row=2, column=0, sticky=W)

souffle = Checkbutton(dessert_frame, text='Суфле',
                      font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=souffle_v)
souffle.grid(row=3, column=0, sticky=W)

pie = Checkbutton(dessert_frame, text='Пай',
                  font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=pie_v)
pie.grid(row=4, column=0, sticky=W)

ice_cream = Checkbutton(dessert_frame, text='Сладолед',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=ice_cream_v)
ice_cream.grid(row=5, column=0, sticky=W)

milkshake = Checkbutton(dessert_frame, text='Млечен шейк',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=milkshake_v)
milkshake.grid(row=6, column=0, sticky=W)

fondue = Checkbutton(dessert_frame, text='Фондю',
                     font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=fondue_v)
fondue.grid(row=7, column=0, sticky=W)

fruits = Checkbutton(dessert_frame, text='Плодове',
                     font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=fruits_v)
fruits.grid(row=8, column=0, sticky=W)

# Defining variables for text of the desserts
text_strawberry_cake_v = StringVar()
text_biscuit_cake_v = StringVar()
text_brownie_v = StringVar()
text_souffle_v = StringVar()
text_pie_v = StringVar()
text_ice_cream_v = StringVar()
text_milkshake_v = StringVar()
text_fondue_v = StringVar()
text_fruits_v = StringVar()

# Entry fields for Desserts
text_strawberry_cake = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                             textvariable=text_strawberry_cake_v)
text_strawberry_cake.grid(row=0, column=1)

text_biscuit_cake = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                          textvariable=text_biscuit_cake_v)
text_biscuit_cake.grid(row=1, column=1)

text_brownie = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                     textvariable=text_brownie_v)
text_brownie.grid(row=2, column=1)

text_souffle = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                     textvariable=text_souffle_v)
text_souffle.grid(row=3, column=1)

text_pie = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=text_pie_v)
text_pie.grid(row=4, column=1)

text_ice_cream = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_ice_cream_v)
text_ice_cream.grid(row=5, column=1)

text_milkshake = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_milkshake_v)
text_milkshake.grid(row=6, column=1)

text_fondue = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                    textvariable=text_fondue_v)
text_fondue.grid(row=7, column=1)

text_fruits = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                    textvariable=text_fruits_v)
text_fruits.grid(row=8, column=1)
