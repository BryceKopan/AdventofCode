def parseCalibrationValue(nLine):
    firstDigit, lastDigit = None, None
    validWords = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    curWord = ''
    i = 0
    while firstDigit is None:
        if nLine[i].isnumeric():
            firstDigit = int(nLine[i])
        else:
            curWord += nLine[i]
            if curWord in validWords:
                firstDigit = validWords[curWord]
            elif not any(curWord in s for s in validWords):
                i -= len(curWord) - 1
                curWord = ''
        i += 1

    curWord = ''
    i = len(nLine) - 1
    while lastDigit is None:
        if nLine[i].isnumeric():
            lastDigit = int(nLine[i])
        else:
            curWord = nLine[i] + curWord
            if curWord in validWords:
                lastDigit = validWords[curWord]
            elif not any(curWord in s for s in validWords):
                i += len(curWord) - 1
                curWord = ''
        i -= 1

    return (firstDigit * 10) + lastDigit


def testParseCalibrationValue():
    isCorrect = True
    testValuesResults = {'1abc2': 12, 'pqr3stu8vwx': 38, 'a1b2c3d4e5f': 15, 'treb7uchet': 77}

    for key in testValuesResults:
        # print(str(testValuesResults[key]) + ':' + str(parseCalibrationValue(key)))
        if testValuesResults[key] != parseCalibrationValue(key):
            isCorrect = False

    return isCorrect


def testWordParsing():
    isCorrect = True
    testValuesResults = {'two1nine': 29, 'eightwothree': 83, 'abcone2threexyz': 13,
                         'xtwone3four': 24, '4nineeightseven2': 42, 'zoneight234': 14,
                         '7pqrstsixteen': 76}

    for key in testValuesResults:
        # print(str(testValuesResults[key]) + ':' + str(parseCalibrationValue(key)))
        if testValuesResults[key] != parseCalibrationValue(key):
            isCorrect = False

    return isCorrect


if __name__ == "__main__":
    print("Checking for Errors ...")
    if testParseCalibrationValue() and testWordParsing():
        print("... No Errors Found")
    else:
        print("... Error Found")
        exit(1)

    inputFilePath = input("Enter the input .txt filepath: ")
    f = open(inputFilePath, "r")

    calibrationValues = []
    for line in f:
        calibrationValues.append(parseCalibrationValue(line))

    f.close()

    print(str(sum(calibrationValues)))