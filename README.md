# Bozeman Route Planner
This is a walking route planner for Bozeman, MT.  Given a list of addresses in "destination.txt", it will calculate the 
optimal order to visit those locations, and return that path and travel time.  It uses the Held-Karp dynamic programming
algorithm to find this route in exponential time, which is a big improvement over the brute force solution.  Eventually, 
I plan on adding the Streamline bus routes, to further reduce travel time.

# Usage

Download the project as a zip file, and open it in your IDE of choice, and ensure openrouteservices is in your virutal environment.  Go to https://openrouteservice.org/ and get an API key.  Create a .env file in the root, and add a line to that file saying ORS_KEY="your key".  Add a list of destinations to destination.txt, without the city, state, or zip code.  Those will be added automatically.  Run main.

# Future

I plan to add the Bozeman Streamline bus routes, further reducing travel time.  
