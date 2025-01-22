from math import radians, cos, sin, asin, sqrt

# haversine formula from https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def geo_match(array1, array2): 
    matches = []

    for location1 in array1:  # Loop through array1
        closest_location = None 
        min_dist = float('inf') 

        for location2 in array2:  # Loop through array2
            # Extract latitude and longitude from both points
            lat1, lon1 = location1
            lat2, lon2 = location2

            # Calculate distance using the custom haversine function
            dist = haversine(lat1, lon1, lat2, lon2)

            # Check for new minimum distance
            if dist < min_dist:
                min_dist = dist
                closest_location = location2
        
        # Append closest match for each location in array1
        matches.append((location1, closest_location))

    return matches