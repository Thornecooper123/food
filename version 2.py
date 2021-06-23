# Fast Food gui
# Thorne

"""
Program description
"""

# import libraries
from appJar import gui


# variables

# class definitions


class Gui:
    def __init__(self):
        app = gui("Menu", "800x600")
        app.setFont(20)
        # Frames to pick set menu items
        with app.toggleFrame("Food", row=0, column=0):
            app.addRadioButton('verb_1', "chips", 2, 0)
            app.addRadioButton('verb_1', "burger", 3, 0)
            app.addRadioButton('verb_1', "pizza", 4, 0)
        with app.toggleFrame("Drinks"):
            app.addRadioButton('verb_1', "coke", 2, 0)
            app.addRadioButton('verb_1', "sprite", 3, 0)
            app.addRadioButton('verb_1', "fanta", 4, 0)
        with app.toggleFrame("Extra"):
            app.addRadioButton('verb_1', "cake", 2, 0)
            app.addRadioButton('verb_1', "ice cream", 3, 0)
            # close application
        app.addButton('Cancel', app.stop)

        # buttons and what they do
        def press(button):
            # submit order
            if button == "Submit":
                def innerPress(button):
                    if button == "wrong":
                        app1.stop()
                    if button == "Correct":
                        app1.stop()

                app.stop()
                app1 = gui("Order", "800x600")
                app1.addButtons(["Correct", "wrong"], innerPress)
                app1.go()

        app.addButton("Submit", press)

        app.go()


# functions

# main routine

Fast_food = Gui()
