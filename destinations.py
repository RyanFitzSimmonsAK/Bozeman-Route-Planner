from openrouteservice.geocode import *


def getDestinations(client, file):
    """
    A function to read a text file containing the destinations and the duration of each stop, and returns critical
    information about each one.  It converts the locations into longitude and latitude coordinates, and returns
    lists for the coordinates, the addresses, and duration of each stop.
    :param client: The client to access the openrouteservice API.
    :param file: A text file containing our destinations and how long to spend at each one
    :return: Coordinates of each destination, the address of each destination, and how long to spend at each location
    """
    file = open("destination.txt")

    destinationList = []
    destinationNames = []
    destinationDurations = []

    for line in file:
        line = line.split(", ")

        # Appends the address to the names array.
        destinationNames.append(line[0].replace("\n", ""))

        # Adds the city and zip code for more accuracy, then calls the function to convert it to
        # coordinates before appending it to the array.
        line[0] += ", Bozeman, MT 59715"
        destinationList.append(addressToCoordinates(client, line[0]))

        # The first address doesn't have a duration since it's the start and end point, so we need a case
        # for that.  For the rest, we just append the duration.
        if len(line) > 1:
            destinationDurations.append(int(line[1][:-1]))
        else:
            destinationDurations.append(0)

    return destinationList, destinationNames, destinationDurations


def addressToCoordinates(client, address):
    """
    A function to convert a street address to coordinates, using the openrouteservice API.
    :param client: The client to access the openrouteservice API.
    :param address: A street address to be converted.
    :return: The longitude and latitude of the address.
    """
    # pelias_search is the function to geocode with openrouteservice.
    search = pelias_search(client, address)

    # openrouteservice returns a lot of information in JSON format, but we only need the coordinates.
    return search['features'][0]['geometry']['coordinates']
