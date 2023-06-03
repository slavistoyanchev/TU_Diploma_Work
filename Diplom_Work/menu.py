from tkinter import *
import menu_gui as menu

# Calculator methods
calculator_field = Entry
operator = ''


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
        menu.text_salad.config(state=NORMAL)
        text_salad_v.set('1')
        menu.text_salad.focus()
    else:
        menu.text_salad.config(state=DISABLED)
        text_salad_v.set('0')


def soup():
    if soup_v.get() == 1:
        menu.text_soup.config(state=NORMAL)
        text_soup_v.set('1')
        menu.text_soup.focus()
    else:
        menu.text_soup.config(state=DISABLED)
        text_soup_v.set('0')


def fish():
    if fish_v.get() == 1:
        menu.text_fish.config(state=NORMAL)
        text_fish_v.set('1')
        menu.text_fish.focus()
    else:
        menu.text_fish.config(state=DISABLED)
        text_fish_v.set('0')


def steak():
    if steak_v.get() == 1:
        menu.text_steak.config(state=NORMAL)
        text_steak_v.set('1')
        menu.text_steak.focus()
    else:
        menu.text_steak.config(state=DISABLED)
        text_steak_v.set('0')


def normal_potatoes():
    if normal_potatoes_v.get() == 1:
        menu.text_normal_potatoes.config(state=NORMAL)
        text_normal_potatoes_v.set('1')
        menu.text_normal_potatoes.focus()
    else:
        menu.text_normal_potatoes.config(state=DISABLED)
        text_normal_potatoes_v.set('0')


def sweet_potatoes():
    if sweet_potatoes_v.get() == 1:
        menu.text_sweet_potatoes.config(state=NORMAL)
        text_sweet_potatoes_v.set('1')
        menu.text_sweet_potatoes.focus()
    else:
        menu.text_sweet_potatoes.config(state=DISABLED)
        text_sweet_potatoes_v.set('0')


def spaghetti():
    if spaghetti_v.get() == 1:
        menu.text_spaghetti.config(state=NORMAL)
        text_spaghetti_v.set('1')
        menu.text_spaghetti.focus()
    else:
        menu.text_spaghetti.config(state=DISABLED)
        text_spaghetti_v.set('0')


def pizza():
    if pizza_v.get() == 1:
        menu.text_pizza.config(state=NORMAL)
        text_pizza_v.set('1')
        menu.text_pizza.focus()
    else:
        menu.text_pizza.config(state=DISABLED)
        text_pizza_v.set('0')


def burger():
    if burger_v.get() == 1:
        menu.text_burger.config(state=NORMAL)
        text_burger_v.set('1')
        menu.text_burger.focus()
    else:
        menu.text_burger.config(state=DISABLED)
        text_burger_v.set('0')


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
