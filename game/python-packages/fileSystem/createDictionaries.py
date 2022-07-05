import fileReaders as fr
#Load on startup
#Initialise tuples for use in entity classes

# def getAiTuple(id, a_Dictionary = None):
#     pass

# def getStatTuple(id):
#     pass

#Create respective dictionaries from files from fileReaders
ai_Dictionary = fr.listToDictionary(fr.readCSVFile("game/python-packages/fileSystem/ai.csv"))
stat_dictionary = fr.listToDictionary(fr.readCSVFile("game/python-packages/fileSystem/stat.csv"))
