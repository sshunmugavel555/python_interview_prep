""" def greeter(names):
    Greets contents of the passed in list to the user
    for eachName in names:
        print(f"Hello! {eachName.title()}, welcome to da club")


nameList=['Shankar','Abee','Nik','Kin']
greeter(nameList) """



def printModels(unprinted_models,printed_models):
    """ Function to simulate printing of models from a given list """
    while unprinted_models:
        model=unprinted_models.pop()
        print(f"Making model {model} now")
        printed_models.append(model)
    return printed_models

def showFinishedModels(finModelList):
    """ Function to show the finished models from a given list """
    print(f"Printing the finished models now...")
    for eachModel in finModelList:
        print(eachModel)


unprinted_models=['aaa','bbb','ccc','ddd']
printed_models=[]

finModelList=printModels(unprinted_models[:],printed_models)
showFinishedModels(finModelList)

