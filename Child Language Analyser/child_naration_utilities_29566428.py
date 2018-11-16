#Jaimon Thyparambil Thomas
#StudentID: 29566428
#Start Date: 25/09/2018
#Last Modifie Date: 25/09/2018
#Class contains various Utilities used for analysing and visualising and filtering child naration

from filter_conversation_29566428 import FilterConversation
import analyzer_settings_29566428 as AnalyzerSettings
from child_naration_analyzer_29566428 import ChildNarationAnalyzer as CNA
from child_naration_visualizer_29566428 import ChildNarationVisualizer as CNV
import file_handling_utilities_29566428 as fileUtilities
import matplotlib.pyplot as plt
import numpy as np

#Function used to extract and apply various filters in child naration for SLI and TD files.
def cleanData():
    filter = FilterConversation()
    try:
        if AnalyzerSettings.defaultDataType == AnalyzerSettings.sliOnlyID or \
                AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID:
            # Sli files is been filtered
            filter.cleanFiles(AnalyzerSettings.sliDirectoryName, AnalyzerSettings.extractedDirectoryPrefix,
                          AnalyzerSettings.cleanedDirectoryPrefix)
        if AnalyzerSettings.defaultDataType == AnalyzerSettings.tdOnlyID or \
            AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID:
            # TD files is been filtered
            filter.cleanFiles(AnalyzerSettings.tdDirectoryName, AnalyzerSettings.extractedDirectoryPrefix,
                              AnalyzerSettings.cleanedDirectoryPrefix)
        print("Cleaning was successful")
    except FileNotFoundError:
        print("Sorry Invalid Directory Name in Settings")
        print("Cleaning was unsuccessful")
    return

    # Function used to extract and apply various filters in child naration for SLI and TD files.
def extractData():
    filter = FilterConversation()
    try:
        if AnalyzerSettings.defaultDataType == AnalyzerSettings.sliOnlyID or \
                AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID:
            # Sli files is been filtered
            filter.extractFiles(AnalyzerSettings.sliDirectoryName, AnalyzerSettings.extractedDirectoryPrefix)
        if AnalyzerSettings.defaultDataType == AnalyzerSettings.tdOnlyID or \
                AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID:
            # TD files is been filtered
            filter.extractFiles(AnalyzerSettings.tdDirectoryName, AnalyzerSettings.extractedDirectoryPrefix)
        print("Extraction was successful")
    except FileNotFoundError:
        print("Sorry Invalid Directory Name in Settings")
        print("Extraction was unsuccessful")
    return

#Function used to analyse the data as per the vaious settings configured in the analyser settings
def visualizeData():
    dataSet = []
    if(AnalyzerSettings.defaultDataType == AnalyzerSettings.sliOnlyID or
            AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID):
        #Processing SLI Files
        directoryName = AnalyzerSettings.cleanedDirectoryPrefix + AnalyzerSettings.sliDirectoryName
        if not fileUtilities.directoryExists(directoryName):
            printDataNotCleanedMessage()
            return
        #Extracting list of formatted dict value of Child narration analyser's class for every file in the SLI Directory
        sliDictList = getAnalysedObjectsList(directoryName)
        #creating a Visaliser class for Sli data
        sliVisualizer = CNV(sliDictList, AnalyzerSettings.sliLegendLabel)
        dataSet.append(sliVisualizer)
    if(AnalyzerSettings.defaultDataType == AnalyzerSettings.tdOnlyID or
            AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID):
        # Processing TD Files
        directoryName = AnalyzerSettings.cleanedDirectoryPrefix + AnalyzerSettings.tdDirectoryName
        if not fileUtilities.directoryExists(directoryName):
            printDataNotCleanedMessage()
            return
        # Extracting list of formatted dict value of Child narration analyser's class for every file in the TD Directory
        tdDictList = getAnalysedObjectsList(directoryName)
        #creating a Visaliser class for TD data
        tdVisualizer = CNV(tdDictList, AnalyzerSettings.tdLegendLabel)
        dataSet.append(tdVisualizer)
    #Entire dataset is been visualised
    CNV.visualize(dataSet)
    return

def analyzeData():
    if (AnalyzerSettings.defaultDataType == AnalyzerSettings.sliOnlyID or
            AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID):
        directoryName = AnalyzerSettings.cleanedDirectoryPrefix + AnalyzerSettings.sliDirectoryName
        if not fileUtilities.directoryExists(directoryName):
            printDataNotCleanedMessage()
            return
        print(AnalyzerSettings.sliLegendLabel)
        print(len(AnalyzerSettings.sliLegendLabel) * '-')
        displayAnalyzerObject(directoryName)
    if (AnalyzerSettings.defaultDataType == AnalyzerSettings.tdOnlyID or
            AnalyzerSettings.defaultDataType == AnalyzerSettings.bothID):
        directoryName = AnalyzerSettings.cleanedDirectoryPrefix + AnalyzerSettings.tdDirectoryName
        if not fileUtilities.directoryExists(directoryName):
            printDataNotCleanedMessage()
            return
        print(AnalyzerSettings.tdLegendLabel)
        print(len(AnalyzerSettings.tdLegendLabel) * '-')
        displayAnalyzerObject(directoryName)
    return

#Function used to Plot graph based on the plot type selected in analyzer settings
#parameter:
#   yValuesArray: y axis values list of the various data's list which has to be plotted ie list of list
#   xValues: Column names of the x axis data for which respective y values is been plotted
#   legendList: legend name for each data type in yValuesArray
#   xLabel: x axis label for the plot
#   yLabel: y axis Label for the plot
#   title: title for the plot
#yValuesArray given for the data set
def plot(yValuesArray = [], xValues = [], legendList = [], xLabel = "", yLabel = "", title = ""):
    numberOfDivisions = len(yValuesArray) #determines total no of different data cases considered for plotting
    colors = getColorList(numberOfDivisions) #finds unique color for each case
    numberOfColumns = len(xValues)
    widthOfColumns = 1
    xticks = []
    centreTolerance = 0

    plt.figure(figsize = (20,10)) #define the size of the plot
    #Plot based on the settings choosen in analyzer settings
    if AnalyzerSettings.defaultPlotID == AnalyzerSettings.simplePlotID:
        simplePlotLineLength = 5
        # This block finds the xTicks for the entire data
        for i in range(numberOfDivisions):
            xticks.append(np.arange(0, (simplePlotLineLength * numberOfColumns), simplePlotLineLength))
        simplePlot(numberOfDivisions, xticks, yValuesArray, colors, legendList)
    else:
        # This block finds the xTicks for the entire data
        for i in range(numberOfDivisions):
            xticks.append(np.arange(i, ((numberOfDivisions + widthOfColumns) * numberOfColumns) + i,
                                    (numberOfDivisions + widthOfColumns)))

        centreTolerance = (numberOfDivisions - widthOfColumns) / 2
        barPlot(numberOfDivisions, xticks, yValuesArray, widthOfColumns, colors, legendList)

    plt.xticks(xticks[0] + centreTolerance, xValues, fontsize=15) #Plotting the xTicks
    if len(xLabel) > 0:
        plt.xlabel(xLabel, fontsize=18) #plotting xLabel
    if len(yLabel) > 0:
        plt.ylabel(yLabel, fontsize=18) #plotting yLabel
    if len(title) > 0:
        plt.title(title, fontsize=18) #plotting title
    if len(legendList) >0:
        plt.legend(loc='best', ncol=3, fancybox=True, shadow=True, fontsize=10) #Plotting legend
    plt.show()
    return

#function used to plot a bar plot
#Parameters:
#   numberOfDivisions: no of bars that will be present per column
#   xticks: xticks while ploting bars
#   yValuesArray: y values for which bar is been plotted
#   widthOfColumns: width of each bar
#   color: list of colors for each bar
#   legendList: legend name for the bar that has been plotted
def barPlot(numberOfDivisions, xticks, yValuesArray, widthOfColumns, colors, legendList):
    ax = plt.subplot(111)
    for i in range(numberOfDivisions):
        if len(legendList[i]) > i:
            ax.bar(xticks[i], yValuesArray[i], width=widthOfColumns, color=colors[i], align='center',
                   label=legendList[i])
        else:
            ax.bar(xticks[i], yValuesArray[i], width=widthOfColumns, color=colors[i], align='center')
    return

#function used to plot a Simple plot
#Parameters:
#   numberOfDivisions: no of simple plots to be drawn
#   xticks: xticks while plotting simple plot
#   yValuesArray: y values for which simple plot is been plotted
#   color: list of colors for each simple plot
#   legendList: legend name for the simple plot that has been plotted
def simplePlot(numberOfDivisions, xticks, yValuesArray, colors, legendList):
    for i in range(numberOfDivisions):
        plt.plot(xticks[i], yValuesArray[i], label=legendList[i], color = colors[i], linewidth=5.0)
    return

#Function used to randomly generate list of colors
#Parameter:
#   n: no of unique colors that has to be generated
#Return value:
#   list of unique colors with a size of n
def getColorList(n):
    color = []
    r = 0.0
    g = 0.0
    b = 0.0
    diff = 3*0.9
    if n > 3:
        diff = diff/n
    else:
        diff = diff/3
    for i in range(n):
        r += diff
        if (r > 0.9):
            r = r%0.9
            g += diff
        if (g > 0.9):
            g = g%0.9
            b += diff
        if (b > 0.9):
            b = b%0.9
        color.append((round(r,1),round(g,1),round(b,1)))
    return color

#Function used to analyse various files in a directory and return it as list of objects
#of child narration analyser class
#parameters:
#   directoryName: directory name whose files is going to be processed
#Return Value:
#   list of formatted dict value of Child narration analyser's class for every file in the meta file
def getAnalysedObjectsList(directoryName = ""):
    if not fileUtilities.directoryExists(directoryName):
        return
    res = []
    for each in fileUtilities.getTxtFileNamesAsList(directoryName):
        entry = CNA()
        entry.analyse(directoryName + each)
        res.append(entry.getFormattedCurrentValue())
    return res

#Function used to display the feature values of analyser class for for files in the given directory
#Parameter:
#   directoryName: name of the directory whose files are going to be processed
def displayAnalyzerObject(directoryName = ""):
    if not fileUtilities.directoryExists(directoryName):
        return
    for each in fileUtilities.getTxtFileNamesAsList(directoryName):
        entry = CNA()
        print(directoryName + each +"\n")
        entry.analyse(directoryName + each)
        print(entry)
    return

#Function used to display a common message when the data is uncleaned
def printDataNotCleanedMessage():
    print("Data not cleaned Please Clean Data.")
    input("Press Enter to go back to menu")
    return