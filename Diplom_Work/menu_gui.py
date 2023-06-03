from tkinter import *

root = Tk()
import menu

root.geometry('1350x670+0+0')  # Set up the window size
root.resizable(FALSE, FALSE)  # Remove option to resize the window

root.title('Информационна система Ресторант')
root.config(bg='#808000')  # Set the background color

top_frame = Frame(root, bd=10, relief=RIDGE, bg='#808000')  # Create top frame
top_frame.pack(side=TOP)
label_title = Label(top_frame, text='Информационна система Ресторант',
                    font=('arial', 30, 'bold'), bd=9, fg='black', bg='#8A8841', width=58)
label_title.grid(row=0, column=0)

# Creating Frames
menu_frame = Frame(root, bd=7, relief=RIDGE, bg='#808000')
menu_frame.pack(side=LEFT)

cost_frame = Frame(menu_frame, bd=7, relief=RIDGE, bg='#8A8841', pady=10, padx=55)
cost_frame.pack(side=BOTTOM)

food_frame = LabelFrame(menu_frame, text='Храна',
                        font=('arial', 19, 'italic'), bd=5, relief=RIDGE, fg='black')
food_frame.pack(side=LEFT)

drinks_frame = LabelFrame(menu_frame, text='Напитки', font=('arial', 19, 'italic'), bd=10, relief=RIDGE)
drinks_frame.pack(side=LEFT)

dessert_frame = LabelFrame(menu_frame, text='Десерти', font=('arial', 19, 'italic'), bd=10, relief=RIDGE)
dessert_frame.pack(side=LEFT)

right_frame = Frame(root, bd=7, relief=RIDGE, bg='#8A8841')
right_frame.pack(side=RIGHT)

calculator_frame = Frame(right_frame, bd=1, relief=RIDGE)
calculator_frame.pack()

receipt_frame = Frame(right_frame, bd=4, relief=RIDGE)
receipt_frame.pack()

button_frame = Frame(right_frame, bd=3, relief=RIDGE)
button_frame.pack()

# Food Frame configure
salad = Checkbutton(food_frame, text='Салата',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.salad_v, command=menu.salad)
salad.grid(row=0, column=0, sticky=W)

soup = Checkbutton(food_frame, text='Супа',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.soup_v, command=menu.soup)
soup.grid(row=1, column=0, sticky=W)

fish = Checkbutton(food_frame, text='Риба',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.fish_v, command=menu.fish)
fish.grid(row=2, column=0, sticky=W)

steak = Checkbutton(food_frame, text='Пържола',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.steak_v, command=menu.steak)
steak.grid(row=3, column=0, sticky=W)

normal_potatoes = Checkbutton(food_frame, text='Картофи', font=('arial', 18, 'bold'),
                              onvalue=1, offvalue=0, variable=menu.normal_potatoes_v, command=menu.normal_potatoes)
normal_potatoes.grid(row=4, column=0, sticky=W)

sweet_potatoes = Checkbutton(food_frame, text='Картофи сл.', font=('arial', 18, 'bold'),
                             onvalue=1, offvalue=0, variable=menu.sweet_potatoes_v, command=menu.sweet_potatoes)
sweet_potatoes.grid(row=5, column=0, sticky=W)

spaghetti = Checkbutton(food_frame, text='Спагети', font=('arial', 18, 'bold'),
                        onvalue=1, offvalue=0, variable=menu.spaghetti_v, command=menu.spaghetti)
spaghetti.grid(row=6, column=0, sticky=W)

pizza = Checkbutton(food_frame, text='Пица',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.pizza_v, command=menu.pizza)
pizza.grid(row=7, column=0, sticky=W)

burger = Checkbutton(food_frame, text='Бургер',
                     font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.burger_v, command=menu.burger)
burger.grid(row=8, column=0, sticky=W)

# Entry fields for Food
text_salad = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                   textvariable=menu.text_salad_v)
text_salad.grid(row=0, column=1)

text_soup = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                  textvariable=menu.text_soup_v)
text_soup.grid(row=1, column=1)

text_fish = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                  textvariable=menu.text_fish_v)
text_fish.grid(row=2, column=1)

text_steak = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                   textvariable=menu.text_steak_v)
text_steak.grid(row=3, column=1)

text_normal_potatoes = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                             textvariable=menu.text_normal_potatoes_v)
text_normal_potatoes.grid(row=4, column=1)

text_sweet_potatoes = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                            textvariable=menu.text_sweet_potatoes_v)
text_sweet_potatoes.grid(row=5, column=1)

text_spaghetti = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=menu.text_spaghetti_v)
text_spaghetti.grid(row=6, column=1)

text_pizza = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                   textvariable=menu.text_pizza_v)
text_pizza.grid(row=7, column=1)

text_burger = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                    textvariable=menu.text_burger_v)
text_burger.grid(row=8, column=1)

# Drink Frame configure
water = Checkbutton(drinks_frame, text='Вода',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.water_v)
water.grid(row=0, column=0, sticky=W)

coke = Checkbutton(drinks_frame, text='Кола',
                   font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.coke_v)
coke.grid(row=1, column=0, sticky=W)

ice_tea = Checkbutton(drinks_frame, text='Студен чай',
                      font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.ice_tea_v)
ice_tea.grid(row=2, column=0, sticky=W)

sparkling_water = Checkbutton(drinks_frame, text='Газ. вода',
                              font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.sparkling_water_v)
sparkling_water.grid(row=3, column=0, sticky=W)

whisky = Checkbutton(drinks_frame, text='Уиски',
                     font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.whisky_v)
whisky.grid(row=4, column=0, sticky=W)

red_wine = Checkbutton(drinks_frame, text='Червено вино',
                       font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.red_wine_v)
red_wine.grid(row=5, column=0, sticky=W)

white_wine = Checkbutton(drinks_frame, text='Бяло вино',
                         font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.white_wine_v)
white_wine.grid(row=6, column=0, sticky=W)

vodka = Checkbutton(drinks_frame, text='Водка',
                    font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.vodka_v)
vodka.grid(row=7, column=0, sticky=W)

lemonade = Checkbutton(drinks_frame, text='Лимонада',
                       font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.lemonade_v)
lemonade.grid(row=8, column=0, sticky=W)

# Entry fields for Drinks
text_water = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                   textvariable=menu.text_water_v)
text_water.grid(row=0, column=1)

text_coke = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                  textvariable=menu.text_coke_v)
text_coke.grid(row=1, column=1)

text_ice_tea = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                     textvariable=menu.text_ice_tea_v)
text_ice_tea.grid(row=2, column=1)

text_sparkling_water = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                             textvariable=menu.text_sparkling_water_v)
text_sparkling_water.grid(row=3, column=1)

text_whisky = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                    textvariable=menu.text_whisky_v)
text_whisky.grid(row=4, column=1)

text_red_wine = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                      textvariable=menu.text_red_wine_v)
text_red_wine.grid(row=5, column=1)

text_white_wine = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                        textvariable=menu.text_white_wine_v)
text_white_wine.grid(row=6, column=1)

text_vodka = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                   textvariable=menu.text_vodka_v)
text_vodka.grid(row=7, column=1)

text_lemonade = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                      textvariable=menu.text_lemonade_v)
text_lemonade.grid(row=8, column=1)

# Dessert Frame configure
strawberry_cake = Checkbutton(dessert_frame, text='Яг. торта',
                              font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.strawberry_cake_v)
strawberry_cake.grid(row=0, column=0, sticky=W)

biscuit_cake = Checkbutton(dessert_frame, text='Домашна торта',
                           font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.biscuit_cake_v)
biscuit_cake.grid(row=1, column=0, sticky=W)

brownie = Checkbutton(dessert_frame, text='Брауни',
                      font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.brownie_v)
brownie.grid(row=2, column=0, sticky=W)

souffle = Checkbutton(dessert_frame, text='Суфле',
                      font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.souffle_v)
souffle.grid(row=3, column=0, sticky=W)

pie = Checkbutton(dessert_frame, text='Пай',
                  font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.pie_v)
pie.grid(row=4, column=0, sticky=W)

ice_cream = Checkbutton(dessert_frame, text='Сладолед',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.ice_cream_v)
ice_cream.grid(row=5, column=0, sticky=W)

milkshake = Checkbutton(dessert_frame, text='Млечен шейк',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.milkshake_v)
milkshake.grid(row=6, column=0, sticky=W)

fondue = Checkbutton(dessert_frame, text='Фондю',
                     font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.fondue_v)
fondue.grid(row=7, column=0, sticky=W)

fruits = Checkbutton(dessert_frame, text='Плодове',
                     font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=menu.fruits_v)
fruits.grid(row=8, column=0, sticky=W)

# Entry fields for Desserts
text_strawberry_cake = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                             textvariable=menu.text_strawberry_cake_v)
text_strawberry_cake.grid(row=0, column=1)

text_biscuit_cake = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                          textvariable=menu.text_biscuit_cake_v)
text_biscuit_cake.grid(row=1, column=1)

text_brownie = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                     textvariable=menu.text_brownie_v)
text_brownie.grid(row=2, column=1)

text_souffle = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                     textvariable=menu.text_souffle_v)
text_souffle.grid(row=3, column=1)

text_pie = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED, textvariable=menu.text_pie_v)
text_pie.grid(row=4, column=1)

text_ice_cream = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=menu.text_ice_cream_v)
text_ice_cream.grid(row=5, column=1)

text_milkshake = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=menu.text_milkshake_v)
text_milkshake.grid(row=6, column=1)

text_fondue = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                    textvariable=menu.text_fondue_v)
text_fondue.grid(row=7, column=1)

text_fruits = Entry(dessert_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                    textvariable=menu.text_fruits_v)
text_fruits.grid(row=8, column=1)

# Creating Cost labels and Entry fields
label_cost_of_food = Label(cost_frame, text='Cost of Food', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
label_cost_of_food.grid(row=0, column=0)

text_cost_of_food = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                          textvariable=menu.cost_of_food)
text_cost_of_food.grid(row=0, column=1, padx=41)

label_cost_of_drinks = Label(cost_frame, text='Cost of Drinks', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
label_cost_of_drinks.grid(row=1, column=0)

text_cost_of_drinks = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                            textvariable=menu.cost_of_drinks)
text_cost_of_drinks.grid(row=1, column=1, padx=41)

label_cost_of_desserts = Label(cost_frame, text='Cost of Cakes', font=('arial', 16, 'bold'), bg='#8A8841',
                               fg='white')
label_cost_of_desserts.grid(row=2, column=0)

text_cost_of_cakes = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                           textvariable=menu.cost_of_desserts)
text_cost_of_cakes.grid(row=2, column=1, padx=41)

label_sub_total = Label(cost_frame, text='Sub Total', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
label_sub_total.grid(row=0, column=2)

text_sub_total = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=menu.sub_total)
text_sub_total.grid(row=0, column=3, padx=41)

label_service_tax = Label(cost_frame, text='Service Tax', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
label_service_tax.grid(row=1, column=2)

text_service_tax = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                         textvariable=menu.service_tax)
text_service_tax.grid(row=1, column=3, padx=41)

label_total_cost = Label(cost_frame, text='Total Cost', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
label_total_cost.grid(row=2, column=2)

text_total_cost = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                        textvariable=menu.total_cost)
text_total_cost.grid(row=2, column=3, padx=41)

# Buttons
button_total = Button(button_frame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3, padx=5)
button_total.grid(row=0, column=0)

button_receipt = Button(button_frame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3,
                        padx=5)
button_receipt.grid(row=0, column=1)

button_save = Button(button_frame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3, padx=5)
button_save.grid(row=0, column=2)

button_send = Button(button_frame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3, padx=5)
button_send.grid(row=0, column=3)

button_reset = Button(button_frame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3, padx=5)
button_reset.grid(row=0, column=4)

# Receipt
textReceipt = Text(receipt_frame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0, column=0)

# Calculator

menu.calculator_field = Entry(calculator_frame, font=('arial', 16, 'bold'), width=32, bd=4)
menu.calculator_field.grid(row=0, column=0, columnspan=4)

button7 = Button(calculator_frame, text='7', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                 command=lambda: menu.button_click('7'))
button7.grid(row=1, column=0)

button8 = Button(calculator_frame, text='8', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                 command=lambda: menu.button_click('8'))
button8.grid(row=1, column=1)

button9 = Button(calculator_frame, text='9', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                 command=lambda: menu.button_click('9'))
button9.grid(row=1, column=2)

button_plus = Button(calculator_frame, text='+', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: menu.button_click('+'))
button_plus.grid(row=1, column=3)

button4 = Button(calculator_frame, text='4', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                 command=lambda: menu.button_click('4'))
button4.grid(row=2, column=0)

button5 = Button(calculator_frame, text='5', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                 command=lambda: menu.button_click('5'))
button5.grid(row=2, column=1)

button6 = Button(calculator_frame, text='6', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                 command=lambda: menu.button_click('6'))
button6.grid(row=2, column=2)

button_minus = Button(calculator_frame, text='-', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                      command=lambda: menu.button_click('-'))
button_minus.grid(row=2, column=3)

button1 = Button(calculator_frame, text='1', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                 command=lambda: menu.button_click('1'))
button1.grid(row=3, column=0)

button2 = Button(calculator_frame, text='2', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                 command=lambda: menu.button_click('2'))
button2.grid(row=3, column=1)

button3 = Button(calculator_frame, text='3', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                 command=lambda: menu.button_click('3'))
button3.grid(row=3, column=2)

button_mult = Button(calculator_frame, text='*', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: menu.button_click('*'))
button_mult.grid(row=3, column=3)

button_ans = Button(calculator_frame, text='Ans', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                    command=menu.answer)
button_ans.grid(row=4, column=0)

button_clear = Button(calculator_frame, text='Clear', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6,
                      width=6, command=menu.clear)
button_clear.grid(row=4, column=1)

button0 = Button(calculator_frame, text='0', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                 command=lambda: menu.button_click('0'))
button0.grid(row=4, column=2)

button_div = Button(calculator_frame, text='/', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                    command=lambda: menu.button_click('/'))
button_div.grid(row=4, column=3)
