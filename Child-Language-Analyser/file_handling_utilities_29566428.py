from os import listdir
from os import path
from os import mkdir

#Function used to retrive all txt files name in the given directory as a list
#Parameter:
#   directoryName: name of the directory whose file name is going to be returned
#Return Value:
#   List of names of files in the given directory
def getTxtFileNamesAsList(directoryName = ""):
    res = []
    for fileName in listdir(directoryName):
        if ".txt" in fileName:
            res.append(fileName)
    return res

#This Function Creating a directory if doesnt exist
#Parameter:
#   directoryName: name of the directory that you wish to create
def handleDirectoryExistance(directoryName = ""):
    if not directoryExists(directoryName):
        mkdir(directoryName)
    return

#This Function check whether the given directory exists of not
#Parameter:
#   directorName: Name of the directory that we wish to check whether it exists or not
#Return value:
#   Returns True or False based on whether the directory exists or not
def directoryExists(directoryName = ""):
    return path.exists(directoryName)
