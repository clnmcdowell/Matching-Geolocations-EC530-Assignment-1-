from haversine import haversine, Unit

def geo_match(array1, array2): 
    matches = []

    for location1 in array1: # Loop through each point in array 1
        closest_loc = None 
        min_dist = float('inf') 
