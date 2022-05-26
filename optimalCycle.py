import copy


def findOptimalCycle(distanceMatrix, startingLocation):
    subsets = findSubsets(len(distanceMatrix))

    memo = {}

    for number in range(1, len(distanceMatrix)):
        memo[(number, tuple([]))] = (distanceMatrix[0][number], 0)

    subsets.pop(0)

    for subset in subsets:
        for num in range(1, len(distanceMatrix)):
            if num in subset:
                continue
            else:
                costs = []
                for k in subset:
                    temp = copy.copy(subset)
                    temp.remove(k)
                    costs.append(distanceMatrix[k][num] + memo[(k, tuple(temp))][0])
                memo[(num, tuple(subset))] = min(costs)



def findSubsets(num):
    subsets = [[]]

    while len(subsets) != 2 ** (num - 1):
        for subset in subsets:
            for n in range(1, num):
                if n in subset:
                    continue
                else:
                    newSet = copy.copy(subset)
                    newSet.append(n)
                    newSet.sort()
                    if newSet not in subsets:
                        subsets.append(newSet)

    print(subsets)
    return subsets
