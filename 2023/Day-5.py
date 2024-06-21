def unitTests():
    print("Checking for Errors ...")
    if testGetLowestSoil():
        print("... No Errors Found")
    else:
        print("... Error Found")
        exit(1)

def testGetLowestSoil():

if __name__ == "__main__":
    unitTests()
    filePath = getFilePath()
    lowestSoilValidForASeed = getLowestSoil(filePath)
    print("The closest plot the can support a seed is: " + str(lowestSoilValidForASeed))
