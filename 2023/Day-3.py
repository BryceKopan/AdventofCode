def sumPartNumbers(nEngineSchematic):
    sum = 0

    for lineI, line in enumerate(nEngineSchematic):
        startIndex = None
        endIndex = None
        for charI, char in enumerate(nEngineSchematic[lineI]):
            if char.isnumeric() and not startIndex:
                startIndex = charI
            if charI == len(nEngineSchematic[lineI]) - 1 and startIndex:
                endIndex = charI
            if not char.isnumeric() and startIndex:
                endIndex = charI - 1

            if startIndex and endIndex:
                print(startIndex, endIndex)
                if isPartNumber(lineI, startIndex, endIndex, nEngineSchematic):
                    partNumber = ''
                    for index in range(startIndex, endIndex + 1):
                        partNumber += nEngineSchematic[lineI][index]
                    sum += int(partNumber)
                    print(partNumber)

                startIndex = None
                endIndex = None

    return sum


def isPartNumber(lineNumber, startIndex, endIndex, nEngineSchematic):
    foundAdjacentSymbol = False

    for i in range(startIndex - 1, endIndex + 1):
        if isPartSymbol(nEngineSchematic[lineNumber][i]):
            foundAdjacentSymbol = True
        elif lineNumber > 0 and isPartSymbol(nEngineSchematic[lineNumber - 1][i]):
            foundAdjacentSymbol = True
        elif lineNumber < len(nEngineSchematic) - 1:
            foundAdjacentSymbol = True

    return foundAdjacentSymbol


def isPartSymbol(char):
    return not char.isnumeric() and not char == '.'


def testSumPartNumbers():
    testEngineSchematic = [['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
                           ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
                           ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
                           ['6', '1', '7', '*', '.', '.', '.', '.', '7', '2'],
                           ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
                           ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
                           ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
                           ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']]
    testAnswer = 4361

    print(sumPartNumbers(testEngineSchematic))
    return sumPartNumbers(testEngineSchematic) == testAnswer


if __name__ == "__main__":
    print("Checking for Errors ...")
    if testSumPartNumbers():
        print("... No Errors Found")
    else:
        print("... Error Found")
        exit(1)

    engineSchematicPath = input("Enter the file path for the .txt game data:")
    gameData = open(engineSchematicPath, 'r')

    engineSchematic = []
    for i, line in enumerate(engineSchematic):
        engineSchematic[i] = [char.strip() for char in line]


