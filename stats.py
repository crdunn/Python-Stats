userArray = []

def meanFunction (numList):
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    
    return total/len(numList)

def medianFunction(numList):

    if (len(numList) % 2 == 0):
        return numList[len(numList)/2]
    else:
        highHalfList = int((len(numList)/2) +.5)
        lowHalfList = int((len(numList)/2) - .5)
        return ((numList[highHalfList]+numList[lowHalfList])/2)

def modeFunction (numList):
    holdDict = {}
    for i in range(len(numList)):
        if (numList[i] not in holdDict):
            holdDict[numList[i]] = 1
        else:
            holdDict[numList[i]] += 1

    greatest = 0
   
    for key in holdDict:

        if holdDict[key] > greatest:
            greatest = holdDict[key]
            num = key
            
        
    return num

def varianceFunction(numList):
    meanList = meanFunction(numList)
    total = 0
    for i in range(len(numList)):
        total += (numList[i] - meanList)**2
    return total

def stdevFunction(numList):
    variance = varianceFunction(numList)
    return len(numList)/variance**(1/2)

def zscoreFunction(numList, numInput):
    return ((numInput-meanFunction(numList))/stdevFunction(numList))

def printStats(numArray):
    userChoice = input(f"{numArray} \nWhat stat of the list would you like to see? \n(mean, median, mode, variance, stdev, zscore, 'c' to close the program) ")

    if (userChoice == "mean"):
        print(f'The mean of the list is {meanFunction(numArray)}')
        printStats(userArray)
    elif (userChoice == "median"):
        print(f'The median of the list is {medianFunction(numArray)}')
        printStats(userArray)
    elif (userChoice == "mode"):
        print(f'The mode of the list is {modeFunction(numArray)}')
        printStats(userArray)
    elif(userChoice == "variance"):
        print(f'The variance of the list is {varianceFunction(numArray)}')
        printStats(userArray)
    elif(userChoice == "stdev"):
        print(f'The standard deviantion of the list is {stdevFunction(numArray)}')
        printStats(userArray)
    elif(userChoice == "zscore"):
        userinput = int(input(f"What value would you like the zscore of {numArray}? "))
        if(userinput not in numArray):
            print("That value is not in the list")
            printStats(userArray)
        else: 
            print(f'The z score of the value is {zscoreFunction(numArray, userinput)}')
            printStats(userArray)

    elif(userChoice == "c"):
        print("Bye!")
    else:
        print("I don't recodnize that function.  Perhaps check your spelling?")
        printStats(userArray)

def begin():
    initial = input("Welcome to a simple statstistics calculator!  Would you like to input your own data (y/n)? " )

    if (initial == "y"):
        appendArray()
    else:
        printStats([0,1,1,1,2,3,4,5,6,7,8,9,10,10])

def appendArray():
    x = input("Add next number (input 's' to begin stats)")
    if (x == "s"):
        printStats(userArray)
    elif(type(x) == type("")):
        print("please enter a number")
        appendArray()
    else:
        userArray.append(x)
        print(userArray)
        print(type(x))
        appendArray()

begin()