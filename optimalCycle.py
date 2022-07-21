import copy


def findOptimalCycle(distanceMatrix):
    """
    A function that utilizes the Held-Karp algorithm to solve the traveling salesman problem using dynamic programming.
    :param distanceMatrix: The distance matrix expressed as time in seconds.
    :return: The travel time, and the indices of the destinations in optimal travel order.
    """

    # Find all subsets of the set containing every non-origin index.
    subsets = findSubsets(len(distanceMatrix))

    # Dictionary used for memoization.
    # Keys are stored as a tuple of (target node, nodes passed through to reach target node).
    # Values are stored as a tuple of (cost to travel that path, parent node).
    memo = {}

    # Memoizes the base case into the dictionary.  The base case is the empty set.
    for number in range(1, len(distanceMatrix)):
        memo[(number, tuple([]))] = (distanceMatrix[0][number], 0)

    # Removes the empty set from the subsets.
    subsets.pop(0)

    # Iterates through the subsets, eventually reaching the last set, which is the solution.
    for subset in subsets:

        # If it's on the last subset, then it needs to compare to the origin, so we need a special case.
        if subset == subsets[-1]:
            # An array that contains the cost for each option of parent destination.
            costs = []
            for k in subset:
                temp = copy.copy(subset)
                temp.remove(k)
                # The cost for any particular path is the cost to travel that edge (comes from the distance
                # matrix), and the cost to reach that vertex passing through certain other vertices (comes
                # from the memoization).
                costs.append(distanceMatrix[k][0] + memo[(k, tuple(temp))][0])
            # The minimum cost is the solution in this case, since this is the final subset.
            memo[(0, tuple(subset))] = (min(costs), subset[costs.index(min(costs))])

        # This is the main part of the algorithm, covering every case other than the base and final case.
        else:
            # Each set is compared against all possible destination nodes.
            for num in range(1, len(distanceMatrix)):
                # If a node is already in the subset, then it can't be a target node.
                if num in subset:
                    continue
                else:
                    # An array that contains the cost for each option of parent destination.
                    costs = []
                    for k in subset:
                        temp = copy.copy(subset)
                        temp.remove(k)
                        # The cost for any particular path is the cost to travel that edge (comes from the distance
                        # matrix), and the cost to reach that vertex passing through certain other vertices (comes
                        # from the memoization).
                        costs.append(distanceMatrix[k][num] + memo[(k, tuple(temp))][0])
                    # The memoized value is whichever path is cheapest.
                    memo[(num, tuple(subset))] = (min(costs), subset[costs.index(min(costs))])

    # This part of the algorithm retraces the path.  We start with [0], since we always end at the origin.
    optimalPath = [0]

    # We start with the last subset (the entire set), with the target as our target.
    lastVisitedNode = (0, tuple(subsets[-1]))

    while len(optimalPath) != len(distanceMatrix):
        # Appends the parent node.
        optimalPath.append(memo[lastVisitedNode][1])
        # We need to convert it to a list, since tuples are immutable.
        # We remove the parent node from the subset, and make it the new parent node.
        pathList = list(lastVisitedNode[1])
        pathList.remove(optimalPath[-1])
        lastVisitedNode = (optimalPath[-1], tuple(pathList))

    # We finish by adding the origin, and reversing the list to get the list in the order we'd actally traverse it.
    optimalPath.append(0)
    optimalPath.reverse()

    return memo[0, tuple(subsets[-1])][0], optimalPath


def findSubsets(num):
    """

    :param num: The number of elements in the set.
    :return: A list containing every subset with N elements, where the first element is 1 and the last element is N.
    """

    # We start with the empty set.
    subsets = [[]]

    # There are 2^N subsets of a set with N elements.
    while len(subsets) != 2 ** (num - 1):
        # We can do this in one pass, since this for-loop will also look at subsets that are added in the loop.
        for subset in subsets:
            for n in range(1, num):
                # A subset can't have more than one instance of a single value, so we skip any of those.
                if n in subset:
                    continue
                else:
                    newSet = copy.copy(subset)
                    # Adds the number to the subset, and if it's a new subset, adds it to the list.
                    newSet.append(n)
                    newSet.sort()
                    # We also don't want repeats of subsets.
                    if newSet not in subsets:
                        subsets.append(newSet)

    return subsets
