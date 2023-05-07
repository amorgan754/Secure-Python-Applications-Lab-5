"""This program is to display histograms based off of csv files"""

#imports
import sys
import matplotlib.pyplot as plt
import pandas as pd



POP_CHANGE = "PopChange.csv"
HOUSING = "Housing.csv"
pop_data = pd.read_csv(POP_CHANGE)
house_data = pd.read_csv(HOUSING)


#population data function
def population_menu():
    """This function is to display the menu for the population data"""
    print("Please pick what data you would like to decide from: ")
    print("Option a: April 1 population")
    print("Option b: July 1 population")
    print("Option c: Average population change")
    print("Option z: Return to main selection")


#april population information function
def population_april():
    """This function is to display information for Apr population"""
    print("For April 1:")
    print("Count = ", pop_data["Pop Apr 1"].count())
    print("Mean = ", pop_data["Pop Apr 1"].mean())
    print("Standard Deviation = ",  pop_data["Pop Apr 1"].std())
    print("Minimum = ",  pop_data["Pop Apr 1"].min())
    print("Maximum = ",  pop_data["Pop Apr 1"].max())
    print("Histogram: ", pop_data["Pop Apr 1"].plot(kind="hist"), plt.show())

#july population information function
def population_july():
    """This function is to display information for Jul population"""
    print("For July 1:")
    print("Count = ", pop_data["Pop Jul 1"].count())
    print("Mean = ", pop_data["Pop Jul 1"].mean())
    print("Standard Deviation = ", pop_data["Pop Jul 1"].std())
    print("Minimum = ", pop_data["Pop Jul 1"].min())
    print("Maximum = ", pop_data["Pop Jul 1"].max())
    print("Histogram: ", pop_data["Pop Jul 1"].plot(kind="hist"), plt.show())

#population change function
def population_change():
    """This function is to display information on population change"""
    print("For population change:")
    print("Count = ", pop_data["Change Pop"].count())
    print("Mean = ", pop_data["Change Pop"].mean())
    print("Standard Deviation = ", pop_data["Change Pop"].std())
    print("Minimum = ", pop_data["Change Pop"].min())
    print("Maximum = ", pop_data["Change Pop"].max())
    print("Histogram: ", pop_data["Change Pop"].plot(kind="hist"), plt.show())


#housing menu functiu
def house_menu():
    """This function is to display the housing menu"""
    print("Please pick what data you would like to decide from: ")
    print("Option a: Age average")
    print("Option b: Bedroom average")
    print("Option c: Year built average")
    print("Option d: Rooms average")
    print("Option e: Utility average")
    print("Option z: Return to main selection")

#house age function
def house_age():
    """This function is to display information about housing age"""
    print("For age average:")
    print("Count = ", house_data["AGE"].count())
    print("Mean = ", house_data["AGE"].mean())
    print("Standard Deviation = ", house_data["AGE"].std())
    print("Minimum = ", house_data["AGE"].min())
    print("Maximum = ", house_data["AGE"].max())
    print("Histogram: ", house_data["AGE"].plot(kind = "hist"), plt.show())

#house bedroom function
def house_bed():
    """This function is to display information about bedrooms"""
    print("For bedroom average:")
    print("Count = ", house_data["BEDRMS"].count())
    print("Mean = ", house_data["BEDRMS"].mean())
    print("Standard Deviation = ", house_data["BEDRMS"].std())
    print("Minimum = ", house_data["BEDRMS"].min())
    print("Maximum = ", house_data["BEDRMS"].max())
    print("Histogram: ", house_data["BEDRMS"].plot(kind = "hist"), plt.show())

#house built function
def house_built():
    """This function is to dispaly information about the year built"""
    print("For year built average:")
    print("Count = ", house_data["BUILT"].count())
    print("Mean = ", house_data["BUILT"].mean())
    print("Standard Deviation = ", house_data["BUILT"].std())
    print("Minimum = ", house_data["BUILT"].min())
    print("Maximum = ", house_data["BUILT"].max())
    print("Histogram: ", house_data["BUILT"].plot(kind = "hist"), plt.show())

#house room function
def house_rooms():
    """This function is to display information about room average"""
    print("For room average:")
    print("Count = ", house_data["ROOMS"].count())
    print("Mean = ", house_data["ROOMS"].mean())
    print("Standard Deviation = ", house_data["ROOMS"].std())
    print("Minimum = ", house_data["ROOMS"].min())
    print("Maximum = ", house_data["ROOMS"].max())
    print("Histogram: ", house_data["ROOMS"].plot(kind = "hist"), plt.show())

#house utility function
def house_utility():
    """This function is to display information about the utilities"""
    print("For utility average:")
    print("Count = ", house_data["UTILITY"].count())
    print("Mean = ", house_data["UTILITY"].mean())
    print("Standard Deviation = ", house_data["UTILITY"].std())
    print("Minimum = ", house_data["UTILITY"].min())
    print("Maximum = ", house_data["UTILITY"].max())
    print("Histogram: ", house_data["UTILITY"].plot(kind = "hist"), plt.show())

#exit function
def exit_program():
    """This function is to exit the program"""
    print("Thank you for using our program!")
    sys.exit()



#menu function
def menu():
    """This function is to display the main menu"""
    print("Option 1: Display population data")
    print("Option 2: Display housing data")
    print("Option 0: Exit program")


CHOICE = None
CHOICE_TWO = None

while CHOICE != "0":
    menu()

    CHOICE = input("Please select a menu choice: \n")

    if CHOICE == "1":
        while CHOICE_TWO != "z":
            population_menu()
            CHOICE_TWO = input("Please select a menu choice: \n")
            if CHOICE_TWO == "a":
                population_april()
            elif CHOICE_TWO == "b":
                population_july()
            elif CHOICE_TWO == "c":
                population_change()
            elif CHOICE_TWO == "z":
                break
            else:
                print("Please make a valid choice: ")
    elif CHOICE == "2":
        while CHOICE_TWO != "z":
            house_menu()
            CHOICE_TWO = input("Please select a menu choice: \n")
            if CHOICE_TWO == "a":
                house_age()
            elif CHOICE_TWO == "b":
                house_bed()
            elif CHOICE_TWO == "c":
                house_built()
            elif CHOICE_TWO == "d":
                house_rooms()
            elif CHOICE_TWO == "e":
                house_utility()
            elif CHOICE_TWO == "z":
                break
            else:
                print("Please make a valid choice: ")
    elif CHOICE == "0":
        exit_program()
    else:
        print("Please make a valid choice: ")
