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


def water():
    if water_v.get() == 1:
        menu.text_water.config(state=NORMAL)
        text_water_v.set('1')
        menu.text_water.focus()
    else:
        menu.text_water.config(state=DISABLED)
        text_water_v.set('0')


def coke():
    if coke_v.get() == 1:
        menu.text_coke.config(state=NORMAL)
        text_coke_v.set('1')
        menu.text_coke.focus()
    else:
        menu.text_coke.config(state=DISABLED)
        text_coke_v.set('0')


def ice_tea():
    if ice_tea_v.get() == 1:
        menu.text_ice_tea.config(state=NORMAL)
        text_ice_tea_v.set('1')
        menu.text_ice_tea.focus()
    else:
        menu.text_ice_tea.config(state=DISABLED)
        text_ice_tea_v.set('0')


def sparkling_water():
    if sparkling_water_v.get() == 1:
        menu.text_sparkling_water.config(state=NORMAL)
        text_sparkling_water_v.set('1')
        menu.text_sparkling_water.focus()
    else:
        menu.text_sparkling_water.config(state=DISABLED)
        text_sparkling_water_v.set('0')


def whisky():
    if whisky_v.get() == 1:
        menu.text_whisky.config(state=NORMAL)
        text_whisky_v.set('1')
        menu.text_whisky.focus()
    else:
        menu.text_whisky.config(state=DISABLED)
        text_whisky_v.set('0')


def red_wine():
    if red_wine_v.get() == 1:
        menu.text_red_wine.config(state=NORMAL)
        text_red_wine_v.set('1')
        menu.text_red_wine.focus()
    else:
        menu.text_red_wine.config(state=DISABLED)
        text_red_wine_v.set('0')


def white_wine():
    if white_wine_v.get() == 1:
        menu.text_white_wine.config(state=NORMAL)
        text_white_wine_v.set('1')
        menu.text_white_wine.focus()
    else:
        menu.text_white_wine.config(state=DISABLED)
        text_white_wine_v.set('0')


def vodka():
    if vodka_v.get() == 1:
        menu.text_vodka.config(state=NORMAL)
        text_vodka_v.set('1')
        menu.text_vodka.focus()
    else:
        menu.text_vodka.config(state=DISABLED)
        text_vodka_v.set('0')


def lemonade():
    if lemonade_v.get() == 1:
        menu.text_lemonade.config(state=NORMAL)
        text_lemonade_v.set('1')
        menu.text_lemonade.focus()
    else:
        menu.text_lemonade.config(state=DISABLED)
        text_lemonade_v.set('0')


def strawberry_cake():
    if strawberry_cake_v.get() == 1:
        menu.text_strawberry_cake.config(state=NORMAL)
        text_strawberry_cake_v.set('1')
        menu.text_strawberry_cake.focus()
    else:
        menu.text_strawberry_cake.config(state=DISABLED)
        text_strawberry_cake_v.set('0')


def biscuit_cake():
    if biscuit_cake_v.get() == 1:
        menu.text_biscuit_cake.config(state=NORMAL)
        text_biscuit_cake_v.set('1')
        menu.text_biscuit_cake.focus()
    else:
        menu.text_biscuit_cake.config(state=DISABLED)
        text_biscuit_cake_v.set('0')


def brownie():
    if brownie_v.get() == 1:
        menu.text_brownie.config(state=NORMAL)
        text_brownie_v.set('1')
        menu.text_brownie.focus()
    else:
        menu.text_brownie.config(state=DISABLED)
        text_brownie_v.set('0')


def souffle():
    if souffle_v.get() == 1:
        menu.text_souffle.config(state=NORMAL)
        text_souffle_v.set('1')
        menu.text_souffle.focus()
    else:
        menu.text_souffle.config(state=DISABLED)
        text_souffle_v.set('0')


def pie():
    if pie_v.get() == 1:
        menu.text_pie.config(state=NORMAL)
        text_pie_v.set('1')
        menu.text_pie.focus()
    else:
        menu.text_pie.config(state=DISABLED)
        text_pie_v.set('0')


def ice_cream():
    if ice_cream_v.get() == 1:
        menu.text_ice_cream.config(state=NORMAL)
        text_ice_cream_v.set('1')
        menu.text_ice_cream.focus()
    else:
        menu.text_ice_cream.config(state=DISABLED)
        text_ice_cream_v.set('0')


def milkshake():
    if milkshake_v.get() == 1:
        menu.text_milkshake.config(state=NORMAL)
        text_milkshake_v.set('1')
        menu.text_milkshake.focus()
    else:
        menu.text_milkshake.config(state=DISABLED)
        text_milkshake_v.set('0')


def fondue():
    if fondue_v.get() == 1:
        menu.text_fondue.config(state=NORMAL)
        text_fondue_v.set('1')
        menu.text_fondue.focus()
    else:
        menu.text_fondue.config(state=DISABLED)
        text_fondue_v.set('0')


def fruits():
    if fruits_v.get() == 1:
        menu.text_fruits.config(state=NORMAL)
        text_fruits_v.set('1')
        menu.text_fruits.focus()
    else:
        menu.text_fruits.config(state=DISABLED)
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
