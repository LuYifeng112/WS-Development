
init python:
    import csv


    def readCSVFile(filename):
        #returns tuple (header, data)
        #check filename is string
        assert isinstance(filename, str)
        
        #open file
        file = open(renpy.loader.transfn(filename), "r") #Important Bridging Func
        csvReader = csv.reader(file)
        # header = [] OLD CODE
        # header = tuple(next(csvReader))
        data = []
        for row in csvReader:
            data.append(tuple(row))
        file.close()
        #return list of tuples of data (integers)
        return data

    def listToDictionary(aList):
        #returns Dictionary
        #Dictionary in format id: data
        retDict = {}
        for tupleRow in aList:
            retDict[tupleRow[0]] = tupleRow[1:]

        return retDict
    this_Dictionary = listToDictionary(readCSVFile("csv/thisFile.csv"))
    ai_Dictionary = listToDictionary(readCSVFile("csv/ai.csv"))
    stat_Dictionary = listToDictionary(readCSVFile("csv/stat.csv"))
    #effect_Dictionary is in format id: (tuple of all function id's)
    effect_Dictionary = listToDictionary(readCSVFile("csv/effect.csv")) 
    

