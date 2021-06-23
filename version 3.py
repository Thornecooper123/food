# Fast Food gui
# Thorne

"""
Program description
"""

# import libraries
from appJar import gui

# variables
Order = 1  # storing order
slide = 0
chips = 0
burger = 0
pizza = 0
coke = 0
sprite = 0
fanta = 0
cake = 0
icecream = 0


# class definitions

# gui
class Gui:
    global icecream

    def __init__(self):
        app = gui("Menu", "800x600")
        self._app = app
        app.setFont(20)
        # Frames to pick set menu items
        with app.toggleFrame("Food"):
            app.addRadioButton('verb_1', "chips", 2, 1)
            app.addRadioButton('verb_1', "burger", 3, 1)
            app.addRadioButton('verb_1', "pizza", 4, 1)
        with app.toggleFrame("Drinks"):
            app.addRadioButton('verb_1', "coke", 2, 1)
            app.addRadioButton('verb_1', "sprite", 3, 1)
            app.addRadioButton('verb_1', "fanta", 4, 1)
        with app.toggleFrame("Extra"):
            app.addRadioButton('verb_1', "cake", 2, 1)
            app.addRadioButton('verb_1', "ice cream", 3, 1)
        app.addButton('left', self.press)
        app.addButton('right', self.press)
        app.addLabel("counter", icecream)
        app.addButton("Submit", self.press)

        while slide == 1:
            for x in Order:
                print(x)

            # close application
        app.addButton('Cancel', app.stop)
        app.getAllEntries()
        print()
        app.go()

        # buttons and what they do

    def press(self, button):
        global icecream
        global slide

        def innerPress(button2):
            if button2 == "wrong":
                app1.stop()
            if button2 == "Correct":
                print(Order)

        # submit order or cancel
        if button == "Submit":
            # stop gui
            self._app.stop()
            # 2nd gui
            app1 = gui("Order", "800x600")
            app1.addButtons(["Correct", "wrong"], innerPress)
            app1.go()
        elif button == "left":
            icecream += 1
            self._app.setLabel("counter", icecream)
        elif button == "right":
            self._app.setRadioButton("minus",)
            icecream -= 1
            self._app.setLabel("counter", icecream)


Fast_food = Gui()
