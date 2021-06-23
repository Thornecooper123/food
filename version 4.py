# Fast Food gui
# Thorne

"""
Ted31 fast food project
"""

# import libraries
from appJar import gui

# variables
current_item = 'chips'
total = 0
dict = {
    "chips": 0,
    "burger": 0,
    "pizza": 0,
    "coke": 0,
    "sprite": 0,
    "fanta": 0,
    "cake": 0,
    "ice cream": 0
}



# class definitions

# gui
class Gui:
    """
    main Gui class
    """
    global dict

    def __init__(self):
        """
        main init function for class
        """

        app = gui("Menu", "800x600")

        def setRadioButton(button):
            """
            Radio button dictionary for Gui
            :param button:
            :return:
            """
            global current_item
            app.setLabel("counter", dict[app.getRadioButton('verb_1')])
            current_item = app.getRadioButton('verb_1')

        self._app = app
        app.setFont(20)
        # Frames to pick set menu items
        with app.toggleFrame("Food"):
            app.addRadioButton('verb_1', "chips", 2, 1)
            app.addRadioButton('verb_1', "burger", 3, 1)
            app.addRadioButton('verb_1', "pizza", 4, 1)
            app.setRadioButtonChangeFunction('verb_1', setRadioButton)
        with app.toggleFrame("Drinks"):
            app.addRadioButton('verb_1', "coke", 2, 1)
            app.addRadioButton('verb_1', "sprite", 3, 1)
            app.addRadioButton('verb_1', "fanta", 4, 1)
            app.setRadioButtonChangeFunction('verb_1', setRadioButton)
        with app.toggleFrame("Extra"):
            app.addRadioButton('verb_1', "cake", 2, 1)
            app.addRadioButton('verb_1', "ice cream", 3, 1)
            app.setRadioButtonChangeFunction('verb_1', setRadioButton)
        app.addButton('+', self.press)
        app.addButton('-', self.press)
        app.addLabel("counter", dict['ice cream'])
        app.addButton("Submit", self.press)

        # close application
        app.addButton('Cancel', app.stop)
        app.getAllEntries()
        print()
        app.go()

        # buttons and what they do

    def press(self, button):
        """
        Button functions for first Gui
        :param button:
        :return:
        """
        global dict
        global current_item

        # buttons for 2nd gui
        def innerPress(button2):
            """
            Press functions for second Gui
            :param button2:
            :return:
            """
            # stops gui
            if button2 == "wrong":
                app1.stop()
            if button2 == "Correct":
                global total
                print('-------Costs-------')


                print('Total:', total)
                app1.stop()
                app2 = gui("Order", "200x150")
                app2.addLabel("order complete", "order complete")
                app2.go()

                print(dict)

                print('chips =', '$' + str(dict["chips"] * 2.5))
                print('burger =', '$' + str(dict["burger"] * 6))
                print('pizza =', '$' + str(dict["pizza"] * 5))
                print('coke =', '$' + str(dict["coke"] * 2))
                print('sprite =', '$' + str(dict["sprite"] * 2))
                print('fanta =', '$' + str(dict["fanta"] * 2))
                print('cake =', '$' + str(dict["cake"] * 4))
                print('ice cream =', '$' + str(dict["ice cream"] * 5))

        # submit order or cancel
        if button == "Submit":
            global total
            print('\n\n -------Amount-------')
            for item, key in enumerate(dict):
                print(key + ':', dict[key])

            cost_string = 'Is this your order? \n'

            print('\n\n')
            # stop gui
            self._app.stop()
            # 2nd gui
            app1 = gui("Order", "400x300")
            # app1.addLabel("order", "")

            app1.addLabel("test", cost_string)
            app1.addButtons(["Correct", "wrong"], innerPress)
            app1.go()

        elif button == "+":
            dict[current_item] += 1
            self._app.setLabel("counter", dict[current_item])
        elif button == "-":
            # self._app.setRadioButton("minus", )
            if dict[current_item] != 0:
                dict[current_item] -= 1
                self._app.setLabel("counter", dict[current_item])


Fast_food = Gui()
