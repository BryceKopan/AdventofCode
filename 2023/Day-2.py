def sumViableGames(nGameDictionary, maxValueDictionary):
    gameIDSum = 0

    gameIsValid = True
    for game in nGameDictionary:
        # print(game)
        for color in nGameDictionary[game]:
            # print(color)
            for nResult in nGameDictionary[game][color]:
                # print(game + ":" + str(nResult) + ':' + str(maxValueDictionary[color]) + ":" + str(nResult > maxValueDictionary[color]))
                if nResult > maxValueDictionary[color]:
                    gameIsValid = False

        if gameIsValid:
            gameIDSum += int(game.split(' ')[1])
            # print(game.split(' ')[1])

        gameIsValid = True

    return gameIDSum


def sumMinPower(nGameDictionary):
    minPowerSum = 0

    for game in nGameDictionary:
        minPower = 1
        for color in nGameDictionary[game]:
            minPower = minPower * max(nGameDictionary[game][color])
        minPowerSum += minPower

    return minPowerSum


def testSumViableGames():
    isCorrect = True
    testGames = {'Game 1': {'red': [4, 1], 'green': [2, 2], 'blue': [3, 6]},
                 'Game 2': {'red': [1], 'green': [2, 3, 1], 'blue': [1, 4, 1]},
                 'Game 3': {'red': [20, 4, 1], 'green': [8, 13, 5], 'blue': [6, 5]},
                 'Game 4': {'red': [3, 6, 14], 'green': [1, 3, 3], 'blue': [6, 15]},
                 'Game 5': {'red': [6, 1], 'green': [3, 2], 'blue': [1, 2]}}
    testParameters = {'red': 12, 'green': 13, 'blue': 14}
    testAnswer = 8

    if sumViableGames(testGames, testParameters) != testAnswer:
        isCorrect = False

    return isCorrect


def testSumMinPower():
    isCorrect = True
    testGames = {'Game 1': {'red': [4, 1], 'green': [2, 2], 'blue': [3, 6]},
                 'Game 2': {'red': [1], 'green': [2, 3, 1], 'blue': [1, 4, 1]},
                 'Game 3': {'red': [20, 4, 1], 'green': [8, 13, 5], 'blue': [6, 5]},
                 'Game 4': {'red': [3, 6, 14], 'green': [1, 3, 3], 'blue': [6, 15]},
                 'Game 5': {'red': [6, 1], 'green': [3, 2], 'blue': [1, 2]}}
    testAnswer = 2286

    if sumMinPower(testGames) != testAnswer:
        isCorrect = False

    return isCorrect


if __name__ == '__main__':
    print("Checking for Errors ...")
    if testSumViableGames() and testSumMinPower():
        print("... No Errors Found")
    else:
        print("... Error Found")
        exit(1)

    gameDataPath = input("Enter the file path for the .txt game data:")
    gameData = open(gameDataPath, 'r')

    gameDictionary = {}

    for line in gameData:
        splitLine = line.split(':')
        gameDictionary[splitLine[0]] = {'red': [], 'green': [],'blue': []}
        gamePulls = splitLine[1].split(';')
        for results in gamePulls:
            pullResults = results.split(',')
            for result in pullResults:
                cubeResults = result.split(' ')
                cubeResults[:] = [x.strip('\n') for x in cubeResults if x]
                gameDictionary[splitLine[0]][cubeResults[1]].append(int(cubeResults[0]))

    gameData.close()

    parameterInput = input("Enter game parameters as comma separated ints(r, g ,b): ")
    if parameterInput:
        parameterList = parameterInput.split(',')
        parameterList[:] = [x.strip(' ') for x in parameterList]
        gameParameters = {'red': int(parameterList[0]), 'green': int(parameterList[1]), 'blue': int(parameterList[2])}

        # print(gameDictionary)
        # print(gameParameters)
        print(sumViableGames(gameDictionary, gameParameters))
    else:
        print(sumMinPower(gameDictionary))