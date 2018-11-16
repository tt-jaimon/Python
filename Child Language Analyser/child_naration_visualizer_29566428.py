#Jaimon Thyparambil Thomas
#StudentID: 29566428
#Start Date: 25/09/2018
#Last Modifie Date: 25/09/2018
#Class used to visualise child analyser data

import pandas as pd
from child_naration_analyzer_29566428 import ChildNarationAnalyzer as CNA
import analyzer_settings_29566428 as AnalyzerSettings
import child_naration_utilities_29566428 as utilities

class ChildNarationVisualizer:

    #Initialiser function for child Naration visualizer
    #parameters:
    #   data: data as a list of dictionary which has to be visualised
    #   name: Name for the data which will be used in generating legend while plotting
    def __init__(self, data = pd.DataFrame(), name = ""):
        self.df = pd.DataFrame(data)
        self.name = name
        self.meanData = {}
        self.computeAverage()
        return

    #Overloaded the str method to show the mean values of the current data available
    def __str__(self):
        res =  " Mean Data"
        res += "\n-----------"
        for (key,value) in self.meanData.items():
            res += "\n" + key + ": "+ str(value)
        return res

    #Overloaded the len method to produce length of the dataframe as length of visualiser class
    def __len__(self):
        return len(self.df)

    #Function used to check if visualiser class is empty
    def isEmpty(self):
        return self.len() == 0

    #Function used to print the entire content of the data frame
    def printDataFrame(self):
        return self.df.to_string()

    #Function used to get mean data as list of list of name and list of value array ie [[name][value]]
    #Return value:
    #   [[meanData keys][meanData values]]
    def getMeanAsList(self):
        names = []
        values = []
        for (key,value) in self.meanData.items():
            names.append(key)
            values.append(value)
        return [names,values]

    #Function used to calculate the mean of current data for various analyzer features
    def computeAverage(self):
        for (key,value) in CNA.analyzerFeatures.items():
            self.meanData[value[CNA.featureNamePos]] = self.df[value[CNA.featureNamePos]].agg('mean')
        return

    #Function used to visulaize current objects dataset based on settings
    def visualizeStatistics(self):
        dataSet = [self]
        ChildNarationVisualizer.visualize(dataSet)
        return

    #function used to visualize data for the current list of datasets
    #Parameters:
    #   cnvList: list of visualiser objects which has to be visualised
    def visualize(cnvList = []):
        if(len(cnvList) == 0):
            return

        columnNameList = AnalyzerSettings.columnNamesList
        yValuesArray = []
        xValues = []
        legendList = []
        xLabel = ""
        yLabel = "Data values"
        titleDataSet = set()
        for each in cnvList:
            titleDataSet.add(each.name)
            if(len(columnNameList) > 0):
                #handling cases when any of the particular columns are choosen to visualise
                for column in columnNameList:
                    yValuesArray.append(each.df[column])
                    legendList.append(each.name + " - " + column)
            else:
                #Handling default case that is visualising based on mean data
                temp = each.getMeanAsList()
                yValuesArray.append(temp[1])
                if(len(xValues) == 0):
                    xValues = temp[0]
                legendList.append(each.name + " - Mean Data")

        if(len(xValues) == 0 and len(yValuesArray) > 0):
            for i in range(len(yValuesArray[0])):
                xValues.append("Sample "+ str(i+1))

        if len(columnNameList) > 0:
            xLabel = "Sample Data Name"
        else:
            xLabel = "Column Names"

        title = yLabel + " Vs " + xLabel
        if(len(titleDataSet) > 0):
            title += " For "
            titleDataList = list(titleDataSet)
            titleListLen = len(titleDataList)
            for i in range(titleListLen):
                if(i != 0 and i != titleListLen -1):
                    title += ","
                elif i == titleListLen -1 and i != 0:
                    title += " and "
                title += titleDataList[i]

        utilities.plot(yValuesArray, xValues, legendList, xLabel, yLabel, title)
        return

