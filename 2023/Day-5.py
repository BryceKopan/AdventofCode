import math


def unitTests():
    print("Checking for Errors ...")
    if testGetLowestSoil():
        print("... No Errors Found")
    else:
        print("... Error Found")
        exit(1)


def testGetLowestSoil():
    testAnswer = 35
    testResult = getLowestLocation('InputTextFiles/input-5-mock')

    return testResult == testAnswer


def getLowestLocation(filePath):
    mapsList = loadPlantingMaps(filePath)

    # ask user if it's part 1 or 2
    part = input("Is this Day 5 Part 1 or Day 5 Part 2? Enter 1 or 2 \n")
    if int(part) == 1:
        seedsList = loadSeedsPart1(filePath)
    elif int(part) == 2:
        seedsList = loadSeedsPart2(filePath)
    else:
        print("Invalid choice.")
        exit(1)

    # a seed chain will be the numbers of each step in the mapping process [Seed number, soil number, fertilizer number,  ..., location]
    seedChains = []
    for seed in seedsList:
        seedChains.append([seed])

    currentMap = 1
    for map in mapsList:
        currentMap += 1
        for entry in map:
            # Seed map entries are in the format [destination range start, source range start, range length]
            destinationStart, sourceStart, rangeLength = entry

            for seedChain in seedChains:
                # checking to see if the newest entry in the seed chain is within source range start -- source range start + range length
                # if so the current entry in the seed chain = (seed Chain Entry - source range start) + destination range start
                latestLink = seedChain[-1]
                if len(seedChain) < currentMap and sourceStart <= latestLink < sourceStart + rangeLength:
                    seedChain.append((latestLink - sourceStart) + destinationStart)

        # if there is no mapping present for a number then it's mapped 1:1
        for seedChain in seedChains:
            if len(seedChain) < currentMap:
                seedChain.append(seedChain[-1])

    # determine and return lowest location (should be the last element in the seed chains)
    lowestLocation = math.inf
    for seedChain in seedChains:
        location = seedChain[-1]
        if location < lowestLocation:
            lowestLocation = location

    return lowestLocation


def loadSeedsPart1(filePath):
    file = open(filePath)
    seedLine = file.readline().strip()
    lineIdentifier, seedsString = seedLine.split(':')
    seedsString = seedsString.strip()
    seeds = seedsString.split(' ')
    seeds = [int(seed) for seed in seeds]
    file.close()
    return seeds


def loadSeedsPart2(filePath):
    rawSeeds = loadSeedsPart1(filePath)
    seeds = []

    for i in range(0, len(rawSeeds), 2):
        seedStart = rawSeeds[i]
        rangeLength = rawSeeds[i + 1]

        for j in range(seedStart, seedStart + rangeLength):
            seeds.append(j)

    return seeds


def loadPlantingMaps(filePath):
    file = open(filePath)
    maps = []

    foundMap = False
    currentMap = -1
    for line in file:
        line = line.strip()
        if 'map' in line:
            foundMap = True
            maps.append([])
            currentMap += 1
        elif foundMap and line.strip() == '':
            foundMap = False
        elif foundMap:
            entry = line.split(' ')
            entry = [int(number) for number in entry]
            maps[currentMap].append(entry)

    return maps


if __name__ == "__main__":
    unitTests()
    filePath = 'InputTextFiles/input-5'
    lowestSoilValidForASeed = getLowestLocation(filePath)
    print("The closest plot that can support a seed is: " + str(lowestSoilValidForASeed))
