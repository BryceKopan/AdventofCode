def sumPartNumbers(nEngineSchematic):
    sum = 0

    for lineI, line in enumerate(nEngineSchematic):
        startIndex = None
        endIndex = None
        for charI, char in enumerate(nEngineSchematic[lineI]):
            if char.isnumeric() and startIndex is None:
                startIndex = charI
            if charI == len(nEngineSchematic[lineI]) - 1 and startIndex is not None:
                endIndex = charI
            if not char.isnumeric() and startIndex is not None:
                endIndex = charI - 1

            if startIndex is not None and endIndex is not None:
                if isPartNumber(lineI, startIndex, endIndex, nEngineSchematic):
                    partNumber = ''
                    for index in range(startIndex, endIndex + 1):
                        partNumber += nEngineSchematic[lineI][index]
                    sum += int(partNumber)

                startIndex = None
                endIndex = None

    return sum


def isPartNumber(lineNumber, startIndex, endIndex, nEngineSchematic):
    foundAdjacentSymbol = False
    startAdjacentRange = startIndex
    endAdjacentRange = endIndex
    if startAdjacentRange > 0:
        startAdjacentRange -= 1
    if endAdjacentRange != len(nEngineSchematic[lineNumber]) - 1:
        endAdjacentRange += 1

    for i in range(startAdjacentRange, endAdjacentRange + 1):
        if isPartSymbol(nEngineSchematic[lineNumber][i]):
            foundAdjacentSymbol = True
        elif lineNumber > 0 and isPartSymbol(nEngineSchematic[lineNumber - 1][i]):
            foundAdjacentSymbol = True
        elif lineNumber < len(nEngineSchematic) - 1 and isPartSymbol(nEngineSchematic[lineNumber + 1][i]):
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

    return sumPartNumbers(testEngineSchematic) == testAnswer


# Part 2
def getEngineSchematic():
    engineSchematicPath = input("Enter the file path for the .txt game data:")
    engineSchematicData = open(engineSchematicPath, 'r')

    engineSchematic = []
    for line in engineSchematicData:
        engineSchematic.append([char for char in line.strip()])

    engineSchematicData.close()

    return engineSchematic


def isGear(lineNumber, index, nEngineSchematic):
    adjacentNumbers = {}
    startAdjacentRange = index
    endAdjacentRange = index
    if startAdjacentRange > 0:
        startAdjacentRange -= 1
    if endAdjacentRange != len(nEngineSchematic[lineNumber]) - 1:
        endAdjacentRange += 1

    for i in range(startAdjacentRange, endAdjacentRange + 1):
        if nEngineSchematic[lineNumber][i].isnumeric():
            partNumber, startIndex = getPartNumber(lineNumber, i, nEngineSchematic)
            adjacentNumbers[startIndex] = partNumber
        if lineNumber > 0 and nEngineSchematic[lineNumber - 1][i].isnumeric():
            partNumber, startIndex = getPartNumber(lineNumber - 1, i, nEngineSchematic)
            adjacentNumbers[startIndex * -1] = partNumber
        if lineNumber < len(nEngineSchematic) - 1 and nEngineSchematic[lineNumber + 1][i].isnumeric():
            partNumber, startIndex = getPartNumber(lineNumber + 1, i, nEngineSchematic)
            adjacentNumbers[startIndex + .5] = partNumber

    adjacentNumbers = list(adjacentNumbers.values())
    return len(adjacentNumbers) == 2, adjacentNumbers


def getNextGear(currentLine, currentIndex, nEngineSchematic):
    startingIndex = currentIndex
    for l in range(currentLine, len(nEngineSchematic)):
        for i in range(startingIndex, len(nEngineSchematic[l])):
            if nEngineSchematic[l][i] == '*':
                bordersTwoNumbers, partNumbers = isGear(l, i, nEngineSchematic)
                if bordersTwoNumbers:
                    return l, i, partNumbers
        startingIndex = 0


    return None, None, None


def getPartNumber(lineNumber, index, nEngineSchematic):
    partNumber = nEngineSchematic[lineNumber][index]
    startIndex = index

    # Check chars to the left
    i = 1
    foundNonNumeric = index == 0
    while not foundNonNumeric:
        if index - i < 0 or not nEngineSchematic[lineNumber][index - i].isnumeric():
            foundNonNumeric = True
        else:
            partNumber = nEngineSchematic[lineNumber][index - i] + partNumber
            startIndex -= 1
            i += 1

    # Check chars to the right
    i = 1
    foundNonNumeric = index == len(nEngineSchematic[lineNumber]) - 1
    while not foundNonNumeric:
        if index + i > len(nEngineSchematic[lineNumber]) - 1 or not nEngineSchematic[lineNumber][index + i].isnumeric():
            foundNonNumeric = True
        else:
            partNumber = partNumber + nEngineSchematic[lineNumber][index + i]
            i += 1

    return int(partNumber), startIndex


def sumGearRatio(nEngineSchematic):
    gearRatioSum = 0
    lineIndex = 0
    gearIndex = 0

    while lineIndex is not None and gearIndex is not None:
        lineIndex, gearIndex, adjacentPartNumbers = getNextGear(lineIndex, gearIndex, nEngineSchematic)

        if adjacentPartNumbers is not None:
            gearRatio = adjacentPartNumbers[0] * adjacentPartNumbers[1]
            gearRatioSum += gearRatio
            gearIndex += 1

    return gearRatioSum


def testSumGearRatio():
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
    testAnswer = 467835

    testResult = sumGearRatio(testEngineSchematic)
    return testResult == testAnswer


if __name__ == "__main__":
    print("Checking for Errors ...")
    if testSumPartNumbers() and testSumGearRatio():
        print("... No Errors Found")
    else:
        print("... Error Found")
        exit(1)

    currentEngineSchematic = getEngineSchematic()

    desiredSum = int(input("Choose 1 or 2.\n 1: Engine Part Sum\n 2: Gear Ratio Sum\n"))
    if desiredSum == 1:
        print(sumPartNumbers(currentEngineSchematic))
    elif desiredSum == 2:
        print(sumGearRatio(currentEngineSchematic))
    else:
        print("Invalid Choice")
