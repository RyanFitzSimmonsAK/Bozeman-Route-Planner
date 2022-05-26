import openrouteservice
import destinations
from openrouteservice import distance_matrix

import optimalCycle


def main():
    client = openrouteservice.Client(key='5b3ce3597851110001cf6248f6a2ef3c1fca445091e8bba78f2ed80a')

    destinationList, destinationNames, destinationDurations = destinations.getDestinations(client, "destinations.txt")

    travelDurations = distance_matrix.distance_matrix(client, destinationList, profile='foot-walking')['durations']

    for line in travelDurations:
        print(line)

    testData = [
        [0, 1, 15, 6],
        [2, 0, 7, 3],
        [9, 6, 0, 12],
        [10, 4, 8, 0]
    ]


    optimalCycle.findOptimalCycle(testData, 0)


if __name__ == "__main__":
    main()
