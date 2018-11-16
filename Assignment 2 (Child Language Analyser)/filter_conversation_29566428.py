#Jaimon Thyparambil Thomas
#StudentID: 29566428
#Start Date: 25/09/2018
#Last Modifie Date: 25/09/2018
#Class used to filter and extract child naration

import file_handling_utilities_29566428 as fileUtilities

class FilterConversation:

    #Various unique IDs for the filter settings
    parathesisID = 0
    squareBracketID = 1
    angleBracketID = 2

    #Vasrious Filter settings Exceptions
    paranthesisException = ("(.)",)
    squareBracketException = ("[//]","[/]","[*")

    #various Filter settings details
    #Content Format: (filterSettingsID , startSymbol, endSymbol , exceptions ,isContentRemovalRequired)
    paranthesis = (parathesisID, '(', ')', paranthesisException, False)
    squareBracket = (squareBracketID, '[', ']', squareBracketException, True)
    angleBracket = (angleBracketID, '<', '>', [], False)

    # Postion Number for various filter settings features in filter details
    idPos = 0 #Pos of unique ID used idetify each settings
    startSymbolPos = 1 #Pos of start symbol of the filter settings
    endSymbolPos = 2 #Pos of end symbol of the filter settings
    exceptionListPos = 3 #Pos of exceptions in the filter settings
    contentRemovalPos = 4 #Pos of feature in filter settings which decides whether the content is required or not

    #various Filter Settings
    #Content Format: Filter settingsID vs FilterDetails
    filterSettings = {
        parathesisID: paranthesis,
        squareBracketID: squareBracket,
        angleBracketID: angleBracket
    }

    prefixRemovalSymbols = ('&','+')

    #Funtion which initialises the filter conversation class for extracting child naration
    #Parameter:
    #   childNarationPrefix: unique prefix used to identify the child naration
    def __init__(self, childNarationPrefix = "*CHI:"):
        self.childNarationPrefix = childNarationPrefix
        return

    #Function used to extract child conversation alone from one file and write it to another file
    #Parameters:
    #   OldFileName: actual file name along with path from which we have to extract the content
    #   newFileName: actual file name along with path to which we are going to write the extracted content
    def extractChildConversation(self, oldFileName, newFileName):
        oldFile = open(oldFileName, "r+")
        newFile = open(newFileName, "w+")

        punctutaionNotFound = False
        #This block is been executed for each and every line in the oldFile
        for line in oldFile:
            #by default the punctutaionNotFound will be false untill it has encountered a child prefix
            #some times a child naration can be present in more than one line.
            #End of a child naration statement can be identified using a punctuation.
            # So it will enter the block present below only if the current line is a child naration or
            # The current line is a continuation of a child naration which has not yet ended
            if(self.childNarationPrefix in line or punctutaionNotFound):
                punctutaionNotFound = True
                if("." in line or "?" in line or "!" in line):
                    punctutaionNotFound = False
                newFile.write(line)

        oldFile.close()
        newFile.close()
        return

    #This function is used to apply various filters in the child naration
    #parameters:
    #   OldFileName: actual file name along with path on which we have to apply various filters
    #   newFileName: actual file name along with path to which we are going to write after aplying various filters
    def filterChildConversation(self, oldFileName, newFileName):
        oldFile = open(oldFileName, "r+")
        newFile = open(newFileName, "w+")

        #this block will run for each and every line in the old file
        for line in oldFile:
            line = line.replace(self.childNarationPrefix,'')
            line = line.strip() # used to remove unecessary spaces in the end and begining
            line = self.applyPrefixRemoval(line)
            line = self.applyFilterSettings(line)
            line += "\n"
            newFile.write(line)
        oldFile.close()
        newFile.close()
        return

    #Function used to apply various filter settings
    #Parameter:
    #   line: line in which all the filter settings has to be applied
    #Return Value:
    #   new line after applying all filters
    def applyFilterSettings(self, line):
        linesList  = line.split()

        #The following block is been executed for each settings in Filter Settings
        for (key,value) in FilterConversation.filterSettings.items():
            symbolFound = False
            changeFound = True
            #This loop has to be executed more than once inorder to handle cases like two or more [[]]
            #where content is to be saved
            while changeFound:
                changeFound = False
                newLinesList = []
                for each in linesList:
                    newString = ""

                    #handling Case when we found the start symbol and it is not an exception
                    #By filtering the word by
                    #creating a new string till the start symbol
                    #+ content from start symbol till end symbol if content restoration is required
                    #+ string from end pos till the end of the word
                    if(value[FilterConversation.startSymbolPos] in each and
                            each not in value[FilterConversation.exceptionListPos]):
                        symbolFound = True
                        changeFound = True
                        startPos = each.find(value[FilterConversation.startSymbolPos])
                        newString = each[:startPos]
                        endPos = each.find(value[FilterConversation.endSymbolPos])
                        if endPos != -1 :
                            symbolFound = False
                            if (not value[FilterConversation.contentRemovalPos]):
                                newString += each[startPos+1:endPos]
                            newString += each[endPos+1:]
                        elif (not value[FilterConversation.contentRemovalPos]):
                            newString += each[startPos+1:]
                    #handling case when start symbol was found but end symbol is not found yet
                    elif symbolFound and value[FilterConversation.endSymbolPos] in each:
                            symbolFound = False
                            endPos = each.find(value[FilterConversation.endSymbolPos])
                            if (not value[FilterConversation.contentRemovalPos]):
                                newString += each[:endPos]
                            newString += each[endPos + 1:]
                    #handling cases when neither start symbol is found nor end symbol is found
                    elif (not symbolFound) or (not value[FilterConversation.contentRemovalPos]):
                        newString = each

                    if (len(newString) > 0):
                        newLinesList.append(newString)
                #line list is been changed to new line list for the next iteration
                linesList = newLinesList

        return " ".join(linesList)

    #Function used to remove words with certain prefix
    #Parameter:
    #   line: line in which prefix word removal is to be applied
    #Return value:
    #   line after applying prefix word removal
    def applyPrefixRemoval(self, line):
        linesList = line.split()
        res = ""
        for each in linesList:
            if each[0] not in FilterConversation.prefixRemovalSymbols:
                res += (" " + each)
        res = res.strip()
        return res

    #Function used to extract and filter child naration data and
    #save it in extracted directory name and cleaned directoryname resepectively
    #Paramenter:
    #   directoryName: directory name whose files are going to be processed
    #   extractedDirectoryPrefixName: Prefix for the directory where extracted files are stored
    #   cleanedDirectoryPrefixName: Prefix for the directory where cleaned files are stored
    def cleanFiles(self, directoryName = "", extractedDirectoryPrefixName = "", cleanedDirectoryPrefixName = ""):
        fileUtilities.handleDirectoryExistance(extractedDirectoryPrefixName +directoryName)
        fileUtilities.handleDirectoryExistance(cleanedDirectoryPrefixName +directoryName)
        for fileName in fileUtilities.getTxtFileNamesAsList(directoryName):
            self.extractChildConversation(directoryName + fileName, extractedDirectoryPrefixName +directoryName + fileName)
            self.filterChildConversation(extractedDirectoryPrefixName +directoryName + fileName,
                                                 cleanedDirectoryPrefixName +directoryName + fileName)
        return
    #Function used to extract child naration data and save it in extracted directory name
    #Paramenter:
    #   directoryName: directory name whose files are going to be processed
    #   extractedDirectoryPrefixName: Prefix for the directory where extracted files are stored
    def extractFiles(self, directoryName="", extractedDirectoryPrefixName=""):
        fileUtilities.handleDirectoryExistance(extractedDirectoryPrefixName + directoryName)
        # The following block will run for all files with exxtension .txt ie it will extract and clean those files
        for fileName in fileUtilities.getTxtFileNamesAsList(directoryName):
            self.extractChildConversation(directoryName + fileName,
                                          extractedDirectoryPrefixName + directoryName + fileName)
        return