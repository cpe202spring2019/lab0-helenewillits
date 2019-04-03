def weight_on_planets():
    # input: the user's weight as an integer or float
    # output: the user's weight on Mars and on Jupiter
    validInput = False
    #while loop checks that the input is a number
    while(validInput == False):
        try:
            earth = int(input('What do you weigh on earth? '))
        except ValueError:
            pass
        else:
            validInput = True

    #calculate weight on other planets
    mars = earth * 0.38
    jupiter = earth * 2.34

    print("\nOn Mars you would weigh {0} pounds.".format(mars) + "\nOn Jupiter you would weigh {0} pounds.".format(jupiter))
