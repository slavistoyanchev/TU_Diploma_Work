from tkinter import *

operator = ''


def open_new_window():
    root = Tk()

    # Define methods
    def reset():
        text_receipt.delete(1.0, END)
        text_salad_v.set('0')
        text_fish_v.set('0')
        text_soup_v.set('0')
        text_steak_v.set('0')
        text_normal_potatoes_v.set('0')
        text_sweet_potatoes_v.set('0')
        text_spaghetti_v.set('0')
        text_pizza_v.set('0')
        text_burger_v.set('0')

        text_water_v.set('0')
        text_coke_v.set('0')
        text_ice_tea_v.set('0')
        text_sparkling_water_v.set('0')
        text_whisky_v.set('0')
        text_red_wine_v.set('0')
        text_white_wine_v.set('0')
        text_vodka_v.set('0')
        text_lemonade_v.set('0')

        text_strawberry_cake_v.set('0')
        text_biscuit_cake_v.set('0')
        text_brownie_v.set('0')
        text_souffle_v.set('0')
        text_pie_v.set('0')
        text_ice_cream_v.set('0')
        text_milkshake_v.set('0')
        text_fondue_v.set('0')
        text_fruits_v.set('0')

        text_salad.config(state=DISABLED)
        text_soup.config(state=DISABLED)
        text_fish.config(state=DISABLED)
        text_steak.config(state=DISABLED)
        text_normal_potatoes.config(state=DISABLED)
        text_sweet_potatoes.config(state=DISABLED)
        text_spaghetti.config(state=DISABLED)
        text_pizza.config(state=DISABLED)
        text_burger.config(state=DISABLED)

        text_water.config(state=DISABLED)
        text_coke.config(state=DISABLED)
        text_sparkling_water.config(state=DISABLED)
        text_ice_tea.config(state=DISABLED)
        text_whisky.config(state=DISABLED)
        text_red_wine.config(state=DISABLED)
        text_white_wine.config(state=DISABLED)
        text_vodka.config(state=DISABLED)
        text_lemonade.config(state=DISABLED)

        text_strawberry_cake.config(state=DISABLED)
        text_biscuit_cake.config(state=DISABLED)
        text_brownie.config(state=DISABLED)
        text_ice_cream.config(state=DISABLED)
        text_souffle.config(state=DISABLED)
        text_pie.config(state=DISABLED)
        text_milkshake.config(state=DISABLED)
        text_fondue.config(state=DISABLED)
        text_fruits.config(state=DISABLED)

        salad_v.set(0)
        soup_v.set(0)
        fish_v.set(0)
        steak_v.set(0)
        normal_potatoes_v.set(0)
        sweet_potatoes_v.set(0)
        spaghetti_v.set(0)
        pizza_v.set(0)
        burger_v.set(0)
        water_v.set(0)
        coke_v.set(0)
        ice_tea_v.set(0)
        sparkling_water_v.set(0)
        whisky_v.set(0)
        red_wine_v.set(0)
        white_wine_v.set(0)
        vodka_v.set(0)
        lemonade_v.set(0)
        strawberry_cake_v.set(0)
        biscuit_cake_v.set(0)
        brownie_v.set(0)
        souffle_v.set(0)
        pie_v.set(0)
        ice_cream_v.set(0)
        milkshake_v.set(0)
        fondue_v.set(0)
        fruits_v.set(0)

        cost_of_drinks.set('')
        cost_of_food.set('')
        cost_of_desserts.set('')
        sub_total.set('')
        service_tax.set('')
        total_cost.set('')

    def button_click(numbers):
        global operator
        operator = operator + numbers
        calculator_field.delete(0, END)
        calculator_field.insert(END, operator)

    def clear():
        global operator
        operator = ''
        calculator_field.delete(0, END)

    def answer():
        global operator
        result = str(eval(operator))
        calculator_field.delete(0, END)
        calculator_field.insert(0, result)
        operator = ''

    # Methods for the menu items
    def salad():
        if salad_v.get() == 1:
            text_salad.config(state=NORMAL)
            text_salad_v.set('1')
            text_salad.focus()
        else:
            text_salad.config(state=DISABLED)
            text_salad_v.set('0')

    def soup():
        if soup_v.get() == 1:
            text_soup.config(state=NORMAL)
            text_soup_v.set('1')
            text_soup.focus()
        else:
            text_soup.config(state=DISABLED)
            text_soup_v.set('0')

    def fish():
        if fish_v.get() == 1:
            text_fish.config(state=NORMAL)
            text_fish_v.set('1')
            text_fish.focus()
        else:
            text_fish.config(state=DISABLED)
            text_fish_v.set('0')

    def steak():
        if steak_v.get() == 1:
            text_steak.config(state=NORMAL)
            text_steak_v.set('1')
            text_steak.focus()
        else:
            text_steak.config(state=DISABLED)
            text_steak_v.set('0')

    def normal_potatoes():
        if normal_potatoes_v.get() == 1:
            text_normal_potatoes.config(state=NORMAL)
            text_normal_potatoes_v.set('1')
            text_normal_potatoes.focus()
        else:
            text_normal_potatoes.config(state=DISABLED)
            text_normal_potatoes_v.set('0')

    def sweet_potatoes():
        if sweet_potatoes_v.get() == 1:
            text_sweet_potatoes.config(state=NORMAL)
            text_sweet_potatoes_v.set('1')
            text_sweet_potatoes.focus()
        else:
            text_sweet_potatoes.config(state=DISABLED)
            text_sweet_potatoes_v.set('0')

    def spaghetti():
        if spaghetti_v.get() == 1:
            text_spaghetti.config(state=NORMAL)
            text_spaghetti_v.set('1')
            text_spaghetti.focus()
        else:
            text_spaghetti.config(state=DISABLED)
            text_spaghetti_v.set('0')

    def pizza():
        if pizza_v.get() == 1:
            text_pizza.config(state=NORMAL)
            text_pizza_v.set('1')
            text_pizza.focus()
        else:
            text_pizza.config(state=DISABLED)
            text_pizza_v.set('0')

    def burger():
        if burger_v.get() == 1:
            text_burger.config(state=NORMAL)
            text_burger_v.set('1')
            text_burger.focus()
        else:
            text_burger.config(state=DISABLED)
            text_burger_v.set('0')

    def water():
        if water_v.get() == 1:
            text_water.config(state=NORMAL)
            text_water_v.set('1')
            text_water.focus()
        else:
            text_water.config(state=DISABLED)
            text_water_v.set('0')

    def coke():
        if coke_v.get() == 1:
            text_coke.config(state=NORMAL)
            text_coke_v.set('1')
            text_coke.focus()
        else:
            text_coke.config(state=DISABLED)
            text_coke_v.set('0')

    def ice_tea():
        if ice_tea_v.get() == 1:
            text_ice_tea.config(state=NORMAL)
            text_ice_tea_v.set('1')
            text_ice_tea.focus()
        else:
            text_ice_tea.config(state=DISABLED)
            text_ice_tea_v.set('0')

    def sparkling_water():
        if sparkling_water_v.get() == 1:
            text_sparkling_water.config(state=NORMAL)
            text_sparkling_water_v.set('1')
            text_sparkling_water.focus()
        else:
            text_sparkling_water.config(state=DISABLED)
            text_sparkling_water_v.set('0')

    def whisky():
        if whisky_v.get() == 1:
            text_whisky.config(state=NORMAL)
            text_whisky_v.set('1')
            text_whisky.focus()
        else:
            text_whisky.config(state=DISABLED)
            text_whisky_v.set('0')

    def red_wine():
        if red_wine_v.get() == 1:
            text_red_wine.config(state=NORMAL)
            text_red_wine_v.set('1')
            text_red_wine.focus()
        else:
            text_red_wine.config(state=DISABLED)
            text_red_wine_v.set('0')

    def white_wine():
        if white_wine_v.get() == 1:
            text_white_wine.config(state=NORMAL)
            text_white_wine_v.set('1')
            text_white_wine.focus()
        else:
            text_white_wine.config(state=DISABLED)
            text_white_wine_v.set('0')

    def vodka():
        if vodka_v.get() == 1:
            text_vodka.config(state=NORMAL)
            text_vodka_v.set('1')
            text_vodka.focus()
        else:
            text_vodka.config(state=DISABLED)
            text_vodka_v.set('0')

    def lemonade():
        if lemonade_v.get() == 1:
            text_lemonade.config(state=NORMAL)
            text_lemonade_v.set('1')
            text_lemonade.focus()
        else:
            text_lemonade.config(state=DISABLED)
            text_lemonade_v.set('0')

    def strawberry_cake():
        if strawberry_cake_v.get() == 1:
            text_strawberry_cake.config(state=NORMAL)
            text_strawberry_cake_v.set('1')
            text_strawberry_cake.focus()
        else:
            text_strawberry_cake.config(state=DISABLED)
            text_strawberry_cake_v.set('0')

    def biscuit_cake():
        if biscuit_cake_v.get() == 1:
            text_biscuit_cake.config(state=NORMAL)
            text_biscuit_cake_v.set('1')
            text_biscuit_cake.focus()
        else:
            text_biscuit_cake.config(state=DISABLED)
            text_biscuit_cake_v.set('0')

    def brownie():
        if brownie_v.get() == 1:
            text_brownie.config(state=NORMAL)
            text_brownie_v.set('1')
            text_brownie.focus()
        else:
            text_brownie.config(state=DISABLED)
            text_brownie_v.set('0')

    def souffle():
        if souffle_v.get() == 1:
            text_souffle.config(state=NORMAL)
            text_souffle_v.set('1')
            text_souffle.focus()
        else:
            text_souffle.config(state=DISABLED)
            text_souffle_v.set('0')

    def pie():
        if pie_v.get() == 1:
            text_pie.config(state=NORMAL)
            text_pie_v.set('1')
            text_pie.focus()
        else:
            text_pie.config(state=DISABLED)
            text_pie_v.set('0')

    def ice_cream():
        if ice_cream_v.get() == 1:
            text_ice_cream.config(state=NORMAL)
            text_ice_cream_v.set('1')
            text_ice_cream.focus()
        else:
            text_ice_cream.config(state=DISABLED)
            text_ice_cream_v.set('0')

    def milkshake():
        if milkshake_v.get() == 1:
            text_milkshake.config(state=NORMAL)
            text_milkshake_v.set('1')
            text_milkshake.focus()
        else:
            text_milkshake.config(state=DISABLED)
            text_milkshake_v.set('0')

    def fondue():
        if fondue_v.get() == 1:
            text_fondue.config(state=NORMAL)
            text_fondue_v.set('1')
            text_fondue.focus()
        else:
            text_fondue.config(state=DISABLED)
            text_fondue_v.set('0')

    def fruits():
        if fruits_v.get() == 1:
            text_fruits.config(state=NORMAL)
            text_fruits_v.set('1')
            text_fruits.focus()
        else:
            text_fruits.config(state=DISABLED)
            text_fruits_v.set('0')

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

    # Defining variables for text of the food
    text_salad_v = StringVar()
    text_salad_v.set('0')
    text_soup_v = StringVar()
    text_soup_v.set('0')
    text_fish_v = StringVar()
    text_fish_v.set('0')
    text_steak_v = StringVar()
    text_steak_v.set('0')
    text_normal_potatoes_v = StringVar()
    text_normal_potatoes_v.set('0')
    text_sweet_potatoes_v = StringVar()
    text_sweet_potatoes_v.set('0')
    text_spaghetti_v = StringVar()
    text_spaghetti_v.set('0')
    text_pizza_v = StringVar()
    text_pizza_v.set('0')
    text_burger_v = StringVar()
    text_burger_v.set('0')

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

    # Defining variables for text of the drinks
    text_water_v = StringVar()
    text_water_v.set('0')
    text_coke_v = StringVar()
    text_coke_v.set('0')
    text_ice_tea_v = StringVar()
    text_ice_tea_v.set('0')
    text_sparkling_water_v = StringVar()
    text_sparkling_water_v.set('0')
    text_whisky_v = StringVar()
    text_whisky_v.set('0')
    text_red_wine_v = StringVar()
    text_red_wine_v.set('0')
    text_white_wine_v = StringVar()
    text_white_wine_v.set('0')
    text_vodka_v = StringVar()
    text_vodka_v.set('0')
    text_lemonade_v = StringVar()
    text_lemonade_v.set('0')

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

    # Defining variables for text of the desserts
    text_strawberry_cake_v = StringVar()
    text_strawberry_cake_v.set('0')
    text_biscuit_cake_v = StringVar()
    text_biscuit_cake_v.set('0')
    text_brownie_v = StringVar()
    text_brownie_v.set('0')
    text_souffle_v = StringVar()
    text_souffle_v.set('0')
    text_pie_v = StringVar()
    text_pie_v.set('0')
    text_ice_cream_v = StringVar()
    text_ice_cream_v.set('0')
    text_milkshake_v = StringVar()
    text_milkshake_v.set('0')
    text_fondue_v = StringVar()
    text_fondue_v.set('0')
    text_fruits_v = StringVar()
    text_fruits_v.set('0')

    # Defining variables for cost labels and entry fields
    cost_of_food = StringVar()
    cost_of_drinks = StringVar()
    cost_of_desserts = StringVar()
    sub_total = StringVar()
    service_tax = StringVar()
    total_cost = StringVar()

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
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=salad_v, command=salad)
    salad.grid(row=0, column=0, sticky=W)

    soup = Checkbutton(food_frame, text='Супа',
                       font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=soup_v, command=soup)
    soup.grid(row=1, column=0, sticky=W)

    fish = Checkbutton(food_frame, text='Риба',
                       font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=fish_v, command=fish)
    fish.grid(row=2, column=0, sticky=W)

    steak = Checkbutton(food_frame, text='Пържола',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=steak_v, command=steak)
    steak.grid(row=3, column=0, sticky=W)

    normal_potatoes = Checkbutton(food_frame, text='Картофи', font=('arial', 18, 'bold'),
                                  onvalue=1, offvalue=0, variable=normal_potatoes_v, command=normal_potatoes)
    normal_potatoes.grid(row=4, column=0, sticky=W)

    sweet_potatoes = Checkbutton(food_frame, text='Картофи сл.', font=('arial', 18, 'bold'),
                                 onvalue=1, offvalue=0, variable=sweet_potatoes_v, command=sweet_potatoes)
    sweet_potatoes.grid(row=5, column=0, sticky=W)

    spaghetti = Checkbutton(food_frame, text='Спагети', font=('arial', 18, 'bold'),
                            onvalue=1, offvalue=0, variable=spaghetti_v, command=spaghetti)
    spaghetti.grid(row=6, column=0, sticky=W)

    pizza = Checkbutton(food_frame, text='Пица',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=pizza_v, command=pizza)
    pizza.grid(row=7, column=0, sticky=W)

    burger = Checkbutton(food_frame, text='Бургер',
                         font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=burger_v, command=burger)
    burger.grid(row=8, column=0, sticky=W)

    # Entry fields for Food
    text_salad = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_salad_v)
    text_salad.grid(row=0, column=1)

    text_soup = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                      textvariable=text_soup_v)
    text_soup.grid(row=1, column=1)

    text_fish = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                      textvariable=text_fish_v)
    text_fish.grid(row=2, column=1)

    text_steak = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_steak_v)
    text_steak.grid(row=3, column=1)

    text_normal_potatoes = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                                 textvariable=text_normal_potatoes_v)
    text_normal_potatoes.grid(row=4, column=1)

    text_sweet_potatoes = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                                textvariable=text_sweet_potatoes_v)
    text_sweet_potatoes.grid(row=5, column=1)

    text_spaghetti = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                           textvariable=text_spaghetti_v)
    text_spaghetti.grid(row=6, column=1)

    text_pizza = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_pizza_v)
    text_pizza.grid(row=7, column=1)

    text_burger = Entry(food_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                        textvariable=text_burger_v)
    text_burger.grid(row=8, column=1)

    # Drink Frame configure
    water = Checkbutton(drinks_frame, text='Вода',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=water_v, command=water)
    water.grid(row=0, column=0, sticky=W)

    coke = Checkbutton(drinks_frame, text='Кола',
                       font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=coke_v, command=coke)
    coke.grid(row=1, column=0, sticky=W)

    ice_tea = Checkbutton(drinks_frame, text='Студен чай',
                          font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=ice_tea_v, command=ice_tea)
    ice_tea.grid(row=2, column=0, sticky=W)

    sparkling_water = Checkbutton(drinks_frame, text='Газ. вода', font=('arial', 18, 'bold'),
                                  onvalue=1, offvalue=0, variable=sparkling_water_v, command=sparkling_water)
    sparkling_water.grid(row=3, column=0, sticky=W)

    whisky = Checkbutton(drinks_frame, text='Уиски',
                         font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=whisky_v, command=whisky)
    whisky.grid(row=4, column=0, sticky=W)

    red_wine = Checkbutton(drinks_frame, text='Червено вино', font=('arial', 18, 'bold'),
                           onvalue=1, offvalue=0, variable=red_wine_v, command=red_wine)
    red_wine.grid(row=5, column=0, sticky=W)

    white_wine = Checkbutton(drinks_frame, text='Бяло вино', font=('arial', 18, 'bold'),
                             onvalue=1, offvalue=0, variable=white_wine_v, command=white_wine)
    white_wine.grid(row=6, column=0, sticky=W)

    vodka = Checkbutton(drinks_frame, text='Водка',
                        font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=vodka_v, command=vodka)
    vodka.grid(row=7, column=0, sticky=W)

    lemonade = Checkbutton(drinks_frame, text='Лимонада', font=('arial', 18, 'bold'),
                           onvalue=1, offvalue=0, variable=lemonade_v, command=lemonade)
    lemonade.grid(row=8, column=0, sticky=W)

    # Entry fields for Drinks
    text_water = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_water_v)
    text_water.grid(row=0, column=1)

    text_coke = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                      textvariable=text_coke_v)
    text_coke.grid(row=1, column=1)

    text_ice_tea = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                         textvariable=text_ice_tea_v)
    text_ice_tea.grid(row=2, column=1)

    text_sparkling_water = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                                 textvariable=text_sparkling_water_v)
    text_sparkling_water.grid(row=3, column=1)

    text_whisky = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                        textvariable=text_whisky_v)
    text_whisky.grid(row=4, column=1)

    text_red_wine = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                          textvariable=text_red_wine_v)
    text_red_wine.grid(row=5, column=1)

    text_white_wine = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                            textvariable=text_white_wine_v)
    text_white_wine.grid(row=6, column=1)

    text_vodka = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                       textvariable=text_vodka_v)
    text_vodka.grid(row=7, column=1)

    text_lemonade = Entry(drinks_frame, font=('arial', 18, 'bold'), bd=5, width=6, state=DISABLED,
                          textvariable=text_lemonade_v)
    text_lemonade.grid(row=8, column=1)

    # Dessert Frame configure
    strawberry_cake = Checkbutton(dessert_frame, text='Яг. торта', font=('arial', 18, 'bold'),
                                  onvalue=1, offvalue=0, variable=strawberry_cake_v, command=strawberry_cake)
    strawberry_cake.grid(row=0, column=0, sticky=W)

    biscuit_cake = Checkbutton(dessert_frame, text='Домашна торта', font=('arial', 18, 'bold'),
                               onvalue=1, offvalue=0, variable=biscuit_cake_v, command=biscuit_cake)
    biscuit_cake.grid(row=1, column=0, sticky=W)

    brownie = Checkbutton(dessert_frame, text='Брауни',
                          font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=brownie_v, command=brownie)
    brownie.grid(row=2, column=0, sticky=W)

    souffle = Checkbutton(dessert_frame, text='Суфле',
                          font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=souffle_v, command=souffle)
    souffle.grid(row=3, column=0, sticky=W)

    pie = Checkbutton(dessert_frame, text='Пай',
                      font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=pie_v, command=pie)
    pie.grid(row=4, column=0, sticky=W)

    ice_cream = Checkbutton(dessert_frame, text='Сладолед', font=('arial', 18, 'bold'),
                            onvalue=1, offvalue=0, variable=ice_cream_v, command=ice_cream)
    ice_cream.grid(row=5, column=0, sticky=W)

    milkshake = Checkbutton(dessert_frame, text='Млечен шейк', font=('arial', 18, 'bold'),
                            onvalue=1, offvalue=0, variable=milkshake_v, command=milkshake)
    milkshake.grid(row=6, column=0, sticky=W)

    fondue = Checkbutton(dessert_frame, text='Фондю',
                         font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=fondue_v, command=fondue)
    fondue.grid(row=7, column=0, sticky=W)

    fruits = Checkbutton(dessert_frame, text='Плодове',
                         font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=fruits_v, command=fruits)
    fruits.grid(row=8, column=0, sticky=W)

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

    # Creating Cost labels and Entry fields
    label_cost_of_food = Label(cost_frame, text='Cost of Food', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
    label_cost_of_food.grid(row=0, column=0)

    text_cost_of_food = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                              textvariable=cost_of_food)
    text_cost_of_food.grid(row=0, column=1, padx=41)

    label_cost_of_drinks = Label(cost_frame, text='Cost of Drinks', font=('arial', 16, 'bold'), bg='#8A8841',
                                 fg='white')
    label_cost_of_drinks.grid(row=1, column=0)

    text_cost_of_drinks = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                                textvariable=cost_of_drinks)
    text_cost_of_drinks.grid(row=1, column=1, padx=41)

    label_cost_of_desserts = Label(cost_frame, text='Cost of Cakes', font=('arial', 16, 'bold'), bg='#8A8841',
                                   fg='white')
    label_cost_of_desserts.grid(row=2, column=0)

    text_cost_of_cakes = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                               textvariable=cost_of_desserts)
    text_cost_of_cakes.grid(row=2, column=1, padx=41)

    label_sub_total = Label(cost_frame, text='Sub Total', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
    label_sub_total.grid(row=0, column=2)

    text_sub_total = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                           textvariable=sub_total)
    text_sub_total.grid(row=0, column=3, padx=41)

    label_service_tax = Label(cost_frame, text='Service Tax', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
    label_service_tax.grid(row=1, column=2)

    text_service_tax = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                             textvariable=service_tax)
    text_service_tax.grid(row=1, column=3, padx=41)

    label_total_cost = Label(cost_frame, text='Total Cost', font=('arial', 16, 'bold'), bg='#8A8841', fg='white')
    label_total_cost.grid(row=2, column=2)

    text_total_cost = Entry(cost_frame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                            textvariable=total_cost)
    text_total_cost.grid(row=2, column=3, padx=41)

    # Buttons
    button_total = Button(button_frame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3,
                          padx=5)
    button_total.grid(row=0, column=0)

    button_receipt = Button(button_frame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3,
                            padx=5)
    button_receipt.grid(row=0, column=1)

    button_save = Button(button_frame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3, padx=5)
    button_save.grid(row=0, column=2)

    button_send = Button(button_frame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3, padx=5)
    button_send.grid(row=0, column=3)

    button_reset = Button(button_frame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='#8A8841', bd=3,
                          padx=5, command=reset)
    button_reset.grid(row=0, column=4)

    # Receipt
    text_receipt = Text(receipt_frame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
    text_receipt.grid(row=0, column=0)

    # Calculator
    calculator_field = Entry(calculator_frame, font=('arial', 16, 'bold'), width=32, bd=4)
    calculator_field.grid(row=0, column=0, columnspan=4)

    button7 = Button(calculator_frame, text='7', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: button_click('7'))
    button7.grid(row=1, column=0)

    button8 = Button(calculator_frame, text='8', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: button_click('8'))
    button8.grid(row=1, column=1)

    button9 = Button(calculator_frame, text='9', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: button_click('9'))
    button9.grid(row=1, column=2)

    button_plus = Button(calculator_frame, text='+', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6,
                         width=6,
                         command=lambda: button_click('+'))
    button_plus.grid(row=1, column=3)

    button4 = Button(calculator_frame, text='4', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: button_click('4'))
    button4.grid(row=2, column=0)

    button5 = Button(calculator_frame, text='5', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                     command=lambda: button_click('5'))
    button5.grid(row=2, column=1)

    button6 = Button(calculator_frame, text='6', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                     command=lambda: button_click('6'))
    button6.grid(row=2, column=2)

    button_minus = Button(calculator_frame, text='-', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6,
                          width=6,
                          command=lambda: button_click('-'))
    button_minus.grid(row=2, column=3)

    button1 = Button(calculator_frame, text='1', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: button_click('1'))
    button1.grid(row=3, column=0)

    button2 = Button(calculator_frame, text='2', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                     command=lambda: button_click('2'))
    button2.grid(row=3, column=1)

    button3 = Button(calculator_frame, text='3', font=('arial', 16, 'bold'), fg='grey', bg='white', bd=6, width=6,
                     command=lambda: button_click('3'))
    button3.grid(row=3, column=2)

    button_mult = Button(calculator_frame, text='*', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6,
                         width=6,
                         command=lambda: button_click('*'))
    button_mult.grid(row=3, column=3)

    button_ans = Button(calculator_frame, text='Ans', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6,
                        width=6,
                        command=answer)
    button_ans.grid(row=4, column=0)

    button_clear = Button(calculator_frame, text='Clear', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6,
                          width=6, command=clear)
    button_clear.grid(row=4, column=1)

    button0 = Button(calculator_frame, text='0', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                     command=lambda: button_click('0'))
    button0.grid(row=4, column=2)

    button_div = Button(calculator_frame, text='/', font=('arial', 16, 'bold'), fg='black', bg='#8A8841', bd=6, width=6,
                        command=lambda: button_click('/'))
    button_div.grid(row=4, column=3)

    root.mainloop()
