import openrouteservice
from openrouteservice import distance_matrix
import destinations
import optimalCycle
import os
from dotenv import load_dotenv

"""
This is a walking route planner for Bozeman, MT.  Given a list of addresses in "destination.txt", it will calculate the 
optimal order to visit those locations, and return that path and travel time.  It uses the Held-Karp dynamic programming
algorithm to find this route in exponential time, which is a big improvement over the brute force solution.  Eventually, 
I plan on adding the Streamline bus routes, to further reduce travel time.
"""


def main():

    # Loads the ORS api key from .env.  To use this yourself, add a .env to the root of the project, get an api key,
    # and add a line to that file saying ORS_KEY="your key"
    load_dotenv()
    client = openrouteservice.Client(key=os.environ.get("ORS_KEY"))

    """
    destinationList is the latitude/longitude of the addresses.
    destinationNames is a list of the addresses in plain text.
    destinationDurations is a list of the time you plan to spend at each destination.  This currently isn't used, but
    when I add the Streamline bus routes, it will be necessary.
    
    This line just reads that information in from the text file.
    """""

    destinationList, destinationNames, destinationDurations = destinations.getDestinations(client, "destinations.txt")

    # Converts the coordinates into a distance matrix expressed as time in seconds.
    travelDurations = distance_matrix.distance_matrix(client, destinationList, profile='foot-walking')['durations']

    # Calculates the optimal order in which to visit the destinations.
    bestPath = optimalCycle.findOptimalCycle(travelDurations)

    print("Your itinerary is the following:\n--------------------------------")
    for destination in bestPath[1]:
        print(destinationNames[destination])
    print("Overall Travel Time: " + str(round(bestPath[0] / 60, 1)) + " minutes")


if __name__ == "__main__":
    main()
