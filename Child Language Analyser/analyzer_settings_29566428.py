#Jaimon Thyparambil Thomas
#StudentID: 29566428
#Start Date: 25/09/2018
#Last Modifie Date: 25/09/2018
#Class contains various Settings required for cleaning, analysing and visualising Child naration data

from child_naration_analyzer_29566428 import ChildNarationAnalyzer as CNA
import display_utilities_29566428 as displayUtilities

#Common settings
visualizerSettingsHelpName = "settings_help_29566428.txt"
analyzerSettingsHelpName = "analyser_settings_help_29566428.txt"

#File Path Related Settings

#Default cleaned Directory Prefix for directory where cleaned files will be stored
cleanedDirectoryPrefix = "Cleaned-"
#Default extracted Directory Prefix for directory where extracted files will be stored
extractedDirectoryPrefix = "Extracted-"
#Default Directory Name where all the SLI files are present
sliDirectoryName = "SLI\\"
#Default TD directory name where all the TD files are present
tdDirectoryName = "TD\\"
#Default label for SLI dataset legends
sliLegendLabel = "SLI"
#Default label for TD dataset legends
tdLegendLabel = "TD"

#Data Type Related Settings ID
sliOnlyID = 1
tdOnlyID = 2
bothID = 3
defaultDataType = bothID

dataTypeIDPos = 0
dataTypeNamePos = 1

sli = (sliOnlyID,"SLI Only")
td = (tdOnlyID, "TD Only")
both = (bothID, "Both")

dataType = {
    sliOnlyID : sli,
    tdOnlyID : td,
    bothID : both
}

#Columns to be displayed
columnNamesList = [] #Empty Means Display Mean Data

#Plot Related Settings
barPlotID = 1
simplePlotID = 2
defaultPlotID = barPlotID

plotIDPos = 0
plotNamePos = 1

barPlot = (barPlotID, "Bar Plot")
simplePlot = (simplePlotID, "Simple Plot")

plot = {
    barPlotID : barPlot,
    simplePlotID : simplePlot
}

#Settings Menu ID
sliDirectoryNameSettingsID = 1
tdDirectoryNameSettingsID = 2
extractedDirectoryPrefixSettingsID = 3
cleanedDirectoryPrefixSettingsID = 4
dataTypeSettingsID = 5
sliLegendLabelSettingsID = 6
tdLegendLabelSettingsID = 7

plotSettingsID = 8
columnsNameSettingsID = 9

#Settings Pattern Pos
settingsIDPos = 0
settingsNamePos = 1
settingsDefaultValuePos = 2

#Settings details (settingsID,settings name, default value)

sliDirectoryNameSettings = (sliDirectoryNameSettingsID, "SLI Files Directory Path", sliDirectoryName)
tdDirectoryNameSettings = (tdDirectoryNameSettingsID, "TD Files Directory Path", tdDirectoryName)
extractedDirectoryPrefixSettings = (extractedDirectoryPrefixSettingsID, "Extracted Files Directory Prefix", extractedDirectoryPrefix)
cleanedDirectoryPrefixSettings = (cleanedDirectoryPrefixSettingsID, "Cleaned Files Directory Prefix", cleanedDirectoryPrefix)
dataTypeSettings = (dataTypeSettingsID, "Data Type", bothID)
sliLegendLabelSettings = (sliLegendLabelSettingsID, "SLI Legend Label", sliLegendLabel)
tdLegendLabelSettings = (tdLegendLabelSettingsID, "TD Legend Label", tdLegendLabel)

plotSettings = (plotSettingsID, "Plot Type", barPlotID)
columnNameSettings = (columnsNameSettingsID, "Column Name", [])

#Settings dictionary (key: settingsID , value: settings)
visualiserSettings = {
    sliDirectoryNameSettingsID: sliDirectoryNameSettings,
    tdDirectoryNameSettingsID: tdDirectoryNameSettings,
    extractedDirectoryPrefixSettingsID: extractedDirectoryPrefixSettings,
    cleanedDirectoryPrefixSettingsID: cleanedDirectoryPrefixSettings,
    dataTypeSettingsID: dataTypeSettings,
    sliLegendLabelSettingsID: sliLegendLabelSettings,
    tdLegendLabelSettingsID: tdLegendLabelSettings,
    plotSettingsID: plotSettings,
    columnsNameSettingsID: columnNameSettings
}

#Filter settings dictionary (key: filterID, value: settings)
analyserSettings = {
    sliDirectoryNameSettingsID: sliDirectoryNameSettings,
    tdDirectoryNameSettingsID: tdDirectoryNameSettings,
    extractedDirectoryPrefixSettingsID: extractedDirectoryPrefixSettings,
    cleanedDirectoryPrefixSettingsID: cleanedDirectoryPrefixSettings,
    dataTypeSettingsID: dataTypeSettings,
    sliLegendLabelSettingsID: sliLegendLabelSettings,
    tdLegendLabelSettingsID: tdLegendLabelSettings
}

#Function used to return settings value
#Parameters:
#   SettingsID : unique ID used to identify particular settings
#   isFormattedValue: if True returns display value else returns actual value.
def getSettingsValue(settingsID, isFormattedValue = False):
    if settingsID == sliDirectoryNameSettingsID:
        return sliDirectoryName
    elif settingsID == tdDirectoryNameSettingsID:
        return tdDirectoryName
    elif settingsID == extractedDirectoryPrefixSettingsID:
        return extractedDirectoryPrefix
    elif settingsID == cleanedDirectoryPrefixSettingsID:
        return cleanedDirectoryPrefix
    elif settingsID == plotSettingsID:
        if isFormattedValue:
            return plot[defaultPlotID][plotNamePos]
        return defaultPlotID
    elif settingsID == dataTypeSettingsID:
        if isFormattedValue:
            return dataType[defaultDataType][dataTypeNamePos]
        return defaultDataType
    elif settingsID == columnsNameSettingsID:
        if isFormattedValue and len(columnNamesList) == 0:
            return "Mean Data"
        return columnNamesList
    elif settingsID == sliLegendLabelSettingsID:
        return sliLegendLabel
    elif settingsID == tdLegendLabelSettingsID:
        return tdLegendLabel
    return

#Function used to set settings value
#Parameters:
#   SettingsID : unique ID used to identify particular settings
def setSettingsValue(settingsID):
    if settingsID == sliDirectoryNameSettingsID:
        global sliDirectoryName
        sliDirectoryName = processSettings(settingsID)
    elif settingsID == tdDirectoryNameSettingsID:
        global tdDirectoryName
        tdDirectoryName = processSettings(settingsID)
    elif settingsID == extractedDirectoryPrefixSettingsID:
        global extractedDirectoryPrefix
        extractedDirectoryPrefix = processSettings(settingsID)
    elif settingsID == cleanedDirectoryPrefixSettingsID:
        global cleanedDirectoryPrefix
        cleanedDirectoryPrefix = processSettings(settingsID)
    elif settingsID == plotSettingsID:
        global defaultPlotID
        defaultPlotID = processSettings(settingsID)
    elif settingsID == dataTypeSettingsID:
        global defaultDataType
        defaultDataType = processSettings(settingsID)
    elif settingsID == columnsNameSettingsID:
        global columnNamesList
        columnNamesList = processSettings(settingsID)
    elif settingsID == sliLegendLabelSettingsID:
        global sliLegendLabel
        sliLegendLabel = processSettings(settingsID)
    elif settingsID == tdLegendLabelSettingsID:
        global tdLegendLabel
        tdLegendLabel = processSettings(settingsID)
    return

#Function used to reset settings to default value
def resetSettings():
    global sliDirectoryName
    global tdDirectoryName
    global extractedDirectoryPrefix
    global cleanedDirectoryPrefix
    global defaultPlotID
    global defaultDataType
    global columnNamesList
    global sliLegendLabel
    global tdLegendLabel
    sliDirectoryName = sliDirectoryNameSettings[settingsDefaultValuePos]
    tdDirectoryName = tdDirectoryNameSettings[settingsDefaultValuePos]
    extractedDirectoryPrefix = extractedDirectoryPrefixSettings[settingsDefaultValuePos]
    cleanedDirectoryPrefix = cleanedDirectoryPrefixSettings[settingsDefaultValuePos]
    defaultPlotID = plotSettings[settingsDefaultValuePos]
    defaultDataType = dataTypeSettings[settingsDefaultValuePos]
    columnNamesList = columnNameSettings[settingsDefaultValuePos]
    sliLegendLabel = sliLegendLabelSettings[settingsDefaultValuePos]
    tdLegendLabel = tdLegendLabelSettings[settingsDefaultValuePos]
    return

#Function for displaying settings for visualiser
def visualiserSettingsMenu():
    settingsMenu(visualiserSettings, visualizerSettingsHelpName,displayUtilities.childNarrationVisualiserHeading)
    return

#Function for displaying settings for Analyser
def analyserSettingsMenu():
    settingsMenu(analyserSettings, analyzerSettingsHelpName,displayUtilities.childNarrationAnalyserHeading)
    return

#Function for displaying main settings menu
#Parameters:
#   settings: settings details which is been displayed
#   helpFileName: Help file name for the current settings
def settingsMenu(settings = visualiserSettings, helpFileName = "",mainHeadingStr = ""):
    displayUtilities.mainHeading(mainHeadingStr)
    print("\n Settings")
    print(" ----------\n\n")
    #This block read all the settings from the settings dictionary
    #Also displays its values along with option Number
    for (key,value) in settings.items():
        print(str(key) + "." + value[settingsNamePos] + ": ",getSettingsValue(key,True))

    #Adding rest of the common settings
    settingsLength = len(settings)
    print("")
    print(str(settingsLength + 1) + ".Restore to Default Settings")
    print(str(settingsLength + 2) + ".Help")
    print(str(settingsLength + 3) + ".Go back to previous menu")
    choice = input("\nChoose any of the above options to continue:")

    # This block validates whether the choice entered is correct or not
    while(not choice.isdigit() or (int(choice) < 1 or int(choice) > settingsLength + 4)):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    choice = int(choice)

    #processing settings as per the choice entered by the user
    if choice in settings.keys():
        setSettingsValue(choice)
        settingsMenu(settings)
    elif choice == settingsLength + 1:
        resetSettings()
        settingsMenu(settings)
    elif choice == settingsLength + 2:
        displayUtilities.help(helpFileName)
        settingsMenu(settings)
    elif choice == settingsLength + 3:
        return
    return

#Function used for editing a settings
#Parameter:
#   SettingsID : unique ID used to identify particular settings
def processSettings(settingsID):
    settingsDetails = visualiserSettings[settingsID]
    previousValue = getSettingsValue(settingsID)
    #Displaying various choices available for processing settings
    print("\n")
    print("Press e to edit " + settingsDetails[settingsNamePos])
    print("Press r to reset " + settingsDetails[settingsNamePos] + " to default Value.")
    print("Press l to leave " + settingsDetails[settingsNamePos] + " as it is.")
    choice = input("\nChoose any of the above options : ")
    #This block validates whether the choice entered is correct or not
    while (choice != 'e' and choice != 'r' and choice != 'l'):
        choice = input("Invalid Input!!!. Please Enter a valid choice (e/r/l): ")

    #Processing as per the choice entered by the user
    if choice == 'l':
        return previousValue
    elif choice == 'r':
        return settingsDetails[settingsDefaultValuePos]
    elif choice == 'e' and settingsDetails[settingsIDPos] == columnsNameSettingsID:
        return getDesiredColumnNameList(previousValue)
    else :
        #handling case when choice is edit mode ('e')
        print("\n")
        if(settingsDetails[settingsIDPos] == plotSettingsID):
            return getDesiredValueFromValueSet(plot)
        elif(settingsDetails[settingsIDPos] == dataTypeSettingsID):
            return getDesiredValueFromValueSet(dataType)
        elif (settingsDetails[settingsIDPos] == sliDirectoryNameSettingsID):
            return input("Enter New SLI Directory Name: ")
        elif (settingsDetails[settingsIDPos] == tdDirectoryNameSettingsID):
            return input("Enter New TD Directory Name: ")
        elif (settingsDetails[settingsIDPos] == extractedDirectoryPrefixSettingsID):
            return input("Enter New Extracted Directory Prefix: ")
        elif (settingsDetails[settingsIDPos] == cleanedDirectoryPrefixSettingsID):
            return input("Enter New Cleaned Directory Prefix: ")
        elif (settingsDetails[settingsIDPos] == sliLegendLabelSettingsID):
            return input("Enter New SLI Legend Label: ")
        elif (settingsDetails[settingsIDPos] == tdLegendLabelSettingsID):
            return input("Enter New TD Legend Label: ")
    return

#Function used for getting desired option from available options
#Parameter:
#   valueSet: Available list of values
def getDesiredValueFromValueSet(valueSet):
    for (key, value) in valueSet.items():
        print(str(key) + "." + value[settingsNamePos])
    choice = input("Choose any of the above options to continue:")
    # This block validates whether the choice entered is correct or not
    while (not choice.isdigit() or (int(choice) not in valueSet.keys())):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    return int(choice)

#Function used for getting desired value for column list
#Parameter:
#   previousValue: previous value for columnList
def getDesiredColumnNameList(previousValue):
    print("\n1.Show Mean Data")
    print("2.Choose Columns Manually")
    print("3.Go back to Settings")
    choice = input("Choose any of the above options to continue:")
    # This block validates whether the choice entered is correct or not
    while (not choice.isdigit() or (int(choice) < 1 or int(choice) > 3)):
        choice = input("Invalid Input!!!. Please Enter a valid choice : ")
    choice = int(choice)
    if choice == 1:
        #Mean data is identified by an empty list
        return []
    elif choice == 3:
        return previousValue
    else:
        currentSet = set()
        #This block will break only When
        #The user is done selecting values
        #The user wishes to go back to previous menu by restoring default values
        while True:
            displayUtilities.mainHeading()
            print("\n Current Column list Selected : ",currentSet)
            for (key,value) in CNA.analyzerFeatures.items():
                print(str(key) + "." + value[CNA.featureNamePos])
            featuresLength = len(CNA.analyzerFeatures)
            print("")
            print(str(featuresLength + 1)+".Done Selecting Columns")
            print(str(featuresLength + 2)+".Go back To Settings Menu")
            print("")
            choice = input("Choose any of the above options to continue: ")
            #This block validates whether the choice entered is correct or not
            while (not choice.isdigit() or (int(choice) < 1 or int(choice) > featuresLength + 2)):
                choice = input("Invalid Input!!!. Please Enter a valid choice : ")
            choice = int(choice)

            if choice == featuresLength + 1:
                return list(currentSet)
            elif choice == featuresLength + 2:
                return previousValue
            else:
                currentSet.add(CNA.analyzerFeatures[choice][CNA.featureNamePos])
        return list(currentSet)
    return
