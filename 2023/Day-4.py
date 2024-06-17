def unitTests():
    print("Checking for Errors ...")
    if testGetCardPointValue():
        print("... No Errors Found")
    else:
        print("... Error Found")
        exit(1)

def testGetCardPointValue():
    testCardValues = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
                        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
                        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
                        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
                        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
                        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
    testAnswer = 13

    testSum = 0
    for line in testCardValues:
        testSum += getCardPointValue(line)

    print(testSum)
    return testSum == testAnswer


def getFilePath():
    return input("Enter the file path for the .txt card data:")


def getCardPointValue(line):
    cardValue = 0
    winningNumbers, pickedNumbers = getCardNumbers(line)

    numberOfWinningNumbers = 0
    for number in pickedNumbers:
        if number in winningNumbers:
            numberOfWinningNumbers += 1

    cardValue = pow(numberOfWinningNumbers, 2)
    return cardValue


def getCardNumbers(line):
    line = line.strip()
    gameIdentifier, numbers = line.split(':')
    winningNumbers, chosenNumbers = numbers.split('|')
    winningNumbersList = getNumberList(winningNumbers)
    chosenNumbersList = getNumberList(chosenNumbers)
    return winningNumbersList, chosenNumbersList


def getNumberList(numberString):
    rawNumberList = numberString.strip().split(' ')
    numberList = [int(n.strip()) for n in rawNumberList if n != '']
    return numberList


if __name__ == "__main__":
    unitTests()

    cardDataFilePath = getFilePath()
    cardFile = open(cardDataFilePath, 'r')

    cardPointSum = 0
    for line in cardFile:
        cardPointValue = getCardPointValue(line)
        cardPointSum += cardPointValue

    print("Card Point Sum: " + str(cardPointSum))