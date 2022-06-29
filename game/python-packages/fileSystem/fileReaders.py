import csv


def readCSVFile(filename):
    #returns tuple (header, data)
    #check filename is string
    assert isinstance(filename, str)
    
    #open file
    file = open(filename)
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
