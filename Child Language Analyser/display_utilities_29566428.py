
#Jaimon Thyparambil Thomas
#StudentID: 29566428
#Start Date: 25/09/2018
#Last Modifie Date: 25/09/2018
#Class contains various Display Utilities used for child narration

import analyzer_settings_29566428 as AnalyzerSettings
import child_naration_utilities_29566428 as utilities

exitMsg = "\nBye Bye See You Later"
continueMsg = "\n Press Any Key to continue"
modesContinueMsg = "\nChoose any of these mode to continue: "
childNarrationVisualiserHeading = "Child Narration Visualizer"
childNarrationAnalyserHeading = "Child narration Analyser"
childNarrationFilterHeading = "Child Narration Filter"
visualizerMenuHelpFileName = "visualizer_menu_help_29566428.txt"
analyserMenuHelpFileName = "analyzer_menu_help_29566428.txt"
filterMenuHelpFileName = "filter_menu_help_29566428.txt"


#function to clear current screen
def clearScreen( n = 100):
    print("\n"*n)
    return

#Function prints Child Narration visualiser main Heading
def mainHeading(heading = childNarrationVisualiserHeading):
    clearScreen()
    print(heading)
    print("-" * len(heading))
    print("\n")
    return

#Function displays main menu for filter
def filterMainMenu():
    mainHeading(childNarrationFilterHeading)
    print("1.Extract Data")
    print("2.Clean Data")
    print("3.Settings")
    print("4.Help")
    print("5.Exit")
    choice = input(modesContinueMsg)
    while (not choice.isdigit() or int(choice) < 1 or int(choice) > 6):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    choice = int(choice)

    if choice == 1:
        mainHeading(childNarrationFilterHeading)
        utilities.extractData()
        input(continueMsg)
        filterMainMenu()
    elif choice == 2:
        mainHeading(childNarrationFilterHeading)
        utilities.cleanData()
        input(continueMsg)
        filterMainMenu()
    elif choice == 3:
        AnalyzerSettings.analyserSettingsMenu()
        filterMainMenu()
    elif choice == 4:
        help(filterMenuHelpFileName)
        filterMainMenu()
    elif choice == 5:
        print(exitMsg)
    return

#Function displays main menu for Analyser
def analyzerMainMenu():
    mainHeading(childNarrationFilterHeading)
    print("1.Analyze Data")
    print("2.Clean Data")
    print("3.Settings")
    print("4.Help")
    print("5.Exit")
    choice = input(modesContinueMsg)
    while (not choice.isdigit() or int(choice) < 1 or int(choice) > 5):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    choice = int(choice)

    if choice == 1:
        mainHeading(childNarrationFilterHeading)
        utilities.analyzeData()
        input(continueMsg)
        analyzerMainMenu()
    elif choice == 2:
        mainHeading(childNarrationFilterHeading)
        utilities.cleanData()
        input(continueMsg)
        analyzerMainMenu()
    elif choice == 3:
        AnalyzerSettings.analyserSettingsMenu()
        analyzerMainMenu()
    elif choice == 4:
        help(analyserMenuHelpFileName)
        analyzerMainMenu()
    elif choice == 5:
        print(exitMsg)
    return


#Function displays main menu for visualiser
def mainMenu():
    mainHeading()
    print("1.Visualise Data")
    print("2.Clean Data")
    print("3.Settings")
    print("4.Help")
    print("5.Exit")
    choice = input(modesContinueMsg)
    while(not choice.isdigit() or int(choice) < 1 or int(choice) > 5):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    choice = int(choice)

    if choice == 1:
        utilities.visualizeData()
        mainMenu()
    elif choice == 2:
        mainHeading()
        utilities.cleanData()
        print("We have succesfully cleaned the data")
        input(continueMsg)
        mainMenu()
    elif choice == 3:
        AnalyzerSettings.visualiserSettingsMenu()
        mainMenu()
    elif choice == 4:
        help(visualizerMenuHelpFileName)
        mainMenu()
    elif choice == 5:
        print(exitMsg)
    return

#Function displays help content in the file
#Parameters:
#   fileName: name along with actual path of the help file
def help(fileName):
    mainHeading()
    file = open(fileName,'r')
    print(file.read())
    input(continueMsg)
    return