#Jaimon Thyparambil Thomas
#StudentID: 29566428
#Start Date: 25/09/2018
#Last Modifie Date: 25/09/2018
#Class used to analyse and store various data related to a child naration

import file_handling_utilities_29566428 as fileUtilities

class ChildNarationAnalyzer:

    #Various Analyser feature identifier Symbol
    pauseSymbols = "(.)"
    grammaticalErrorSymbols = ("[*",)
    retracingWordSymbols = ("[//]",)
    repetitiveWordSymbols = ("[/]",)
    statementSymbols = ('.','?','!')

    #Various Analyser feature exception values
    statementException = ("(.)",)
    uniqueWordsExceptions = (pauseSymbols, grammaticalErrorSymbols, retracingWordSymbols, repetitiveWordSymbols, statementSymbols)

    #Various Analyser feature Names
    statementsStr = "Statements"
    uniqueWordsStr = "Unique Words"
    repetitiveWordsStr = "Repeated Words"
    retracingWordsStr = "Retracing Words"
    grammaticalErrorStr = "Grammatical Errors"
    pausesMadeStr = "Pauses Made"

    #Postion Number for various analyser features
    featureIDPos = 0
    featureNamePos = 1
    featureSymbolPos = 2
    featureExceptionPos = 3

    # various Analyser feature ID
    pauseID = 1
    grammaticalErrorID = 2
    retracingWordID = 3
    repetitiveWordID = 4
    statementID = 5
    uniqueWordsID = 6

    #Various Analyser Feature details
    pause = (pauseID, pausesMadeStr , pauseSymbols, () )
    grammaticalError = (grammaticalErrorID, grammaticalErrorStr, grammaticalErrorSymbols, ())
    retracingWords = (retracingWordID, retracingWordsStr, retracingWordSymbols, ())
    repetitiveWords = (repetitiveWordID, repetitiveWordsStr, repetitiveWordSymbols, ())
    statements = (statementID, statementsStr, statementSymbols, statementException)
    uniqueWords = (uniqueWordsID, uniqueWordsStr, retracingWordSymbols, uniqueWordsExceptions)

    #Various Features
    analyzerFeatures = {
        pauseID: pause,
        grammaticalErrorID: grammaticalError,
        retracingWordID: retracingWords,
        repetitiveWordID: repetitiveWords,
        statementID: statements,
        uniqueWordsID: uniqueWords
    }

    #initializer function for the analyzer object
    def __init__(self):

        self.currentValues = {
            ChildNarationAnalyzer.pauseID: 0,
            ChildNarationAnalyzer.grammaticalErrorID: 0,
            ChildNarationAnalyzer.retracingWordID: 0,
            ChildNarationAnalyzer.repetitiveWordID: 0,
            ChildNarationAnalyzer.statementID: 0,
            ChildNarationAnalyzer.uniqueWordsID: 0,
        }
        self.uniqueWordsSet = set()
        return

    #overloaded str function for the analyzer object
    #Displays various features values for current object
    def __str__(self):
        res = ""
        for (key,value) in self.currentValues.items():
            res += "Number of "+ ChildNarationAnalyzer.analyzerFeatures[key][ChildNarationAnalyzer.featureNamePos] \
                   +": "+ str(value) + "\n"
        return res

    #This function reads all the file name in the meta file and and analyze those files details
    #parameter:
    #   directoryName: Name of the Directory whose files are going to be analysed
    def analyseFilesInDir(self, directoryName=""):
        if not fileUtilities.directoryExists(directoryName):
            return
        for each in fileUtilities.getTxtFileNamesAsList(directoryName):
            self.analyse(directoryName + each)
        return

    #This function analyses various feature values in the current file
    #Parameter:
    #   fileName: actual file name along with path whose features is to be analysed
    def analyse(self, fileName):
        file = open(fileName, "r+")
        for line in file:
            linesList = line.split()
            for each in linesList:
                self.uniqueWordsSet.add(each)
                for (key,value) in self.currentValues.items():
                    if key == ChildNarationAnalyzer.uniqueWordsID:
                        #unique words count is calculated in a different approach
                        continue
                    self.currentValues[key] += self.numberOfOccurences(each, key)

        self.removeUnwantedWordsFromVocabulary()
        self.currentValues[ChildNarationAnalyzer.uniqueWordsID] = len(self.uniqueWordsSet)
        file.close()
        return

    #This function removes the unwanted words from the unique words set like punctuations
    def removeUnwantedWordsFromVocabulary(self):
        for each in ChildNarationAnalyzer.uniqueWordsExceptions:
            for entry in each:
                self.uniqueWordsSet.discard(entry)
        return

    #This function finds the number of occurences of respective feature in the given string
    #Parameters:
    #   mainString: The string in which we are going to search for the feature
    #   featureID: UniqueID of the feature whose number of occurrences we are going to analyse
    def numberOfOccurences(self, mainString, featureID):
        feature = ChildNarationAnalyzer.analyzerFeatures[featureID]
        subString = feature[ChildNarationAnalyzer.featureSymbolPos]
        exceptions = feature[ChildNarationAnalyzer.featureExceptionPos]
        count = 0
        for entry in subString:
            #For each symbol in the feature
            beg = mainString.find(entry)
            while beg != -1:
                if(len(exceptions) > 0):
                    for each in exceptions:
                        #For each exception in the feature symbol
                        pos = each.find(entry)
                        if pos > -1 and (beg - pos) > -1 and (beg - pos + len(each)) < len(mainString) \
                                and each == mainString[beg - pos:beg - pos + len(each)]:
                            #if the exception is present in the current fetaure symbol
                            # and if the finding is equal to exception
                            #then we will reduce that count
                            count -= 1
                            break
                count += 1
                beg = mainString.find(entry, beg + 1)
        return count

    #This function returns formatted value of current value object ie feature name vs feature value
    def getFormattedCurrentValue(self):
        res = {}
        for (key, value) in self.currentValues.items():
            res[ChildNarationAnalyzer.analyzerFeatures[key][ChildNarationAnalyzer.featureNamePos]] = value
        return res