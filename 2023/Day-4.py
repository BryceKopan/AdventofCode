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

    return testSum == testAnswer


def getFilePath():
    return input("Enter the file path for the .txt card data:")


def getCardPointValue(line):
    winningNumbers, pickedNumbers = getCardNumbers(line)

    pointValue = 0
    for number in pickedNumbers:
        if number in winningNumbers:
            if pointValue == 0:
                pointValue = 1
            else:
                pointValue = pointValue * 2

    return pointValue


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


def getAllCardsPointSum():
    cardDataFilePath = getFilePath()
    cardFile = open(cardDataFilePath, 'r')

    cardPointSum = 0
    for line in cardFile:
        cardPointValue = getCardPointValue(line)
        cardPointSum += cardPointValue

    return cardPointSum


def getTotalNumberOfCards():
    cardDataFilePath = getFilePath()
    cardFile = open(cardDataFilePath, 'r')

    numberOfSubsequentBonusCards = []
    numberOfCards = 0
    for line in cardFile:
        print(numberOfSubsequentBonusCards)
        timesToCountCard = 1
        if len(numberOfSubsequentBonusCards) > 0:
            timesToCountCard += numberOfSubsequentBonusCards.pop(0)
        numberOfCards += timesToCountCard

        for i in range(timesToCountCard):
            winningNumbers, chosenNumbers = getCardNumbers(line)

            correctNumbers = 0
            for number in chosenNumbers:
                if number in winningNumbers:
                    correctNumbers += 1

            for i in range(correctNumbers):
                if len(numberOfSubsequentBonusCards) <= i:
                    numberOfSubsequentBonusCards.append(0)
                numberOfSubsequentBonusCards[i] += 1

    return numberOfCards


if __name__ == "__main__":
    unitTests()

    desiredSum = int(input("Choose 1 or 2.\n 1: Card Points Sum\n 2: Total number of cards\n"))
    if desiredSum == 1:
        print("Card Point Sum: " + str(getAllCardsPointSum()))
    elif desiredSum == 2:
        print("Total number of Cards: " + str(getTotalNumberOfCards()))
    else:
        print("Invalid Choice")

