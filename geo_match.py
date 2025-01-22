from haversine import haversine, Unit

def geo_match(array1, array2): 
    matches = []

    for location1 in array1: # Loop through array1
        closest_location = None 
        min_dist = float('inf') 

        for location2 in array2: # Loop through array2
            # Find distance between locations using Haversine formula
            dist = haversine(location1, location2, unit=Unit.MILES)

            # Check for new minimum distance
            if dist < min_dist:
                min_dist = dist
                closest_location = location2
        
        # Append closest match for each location in array1
        matches.append((location1, closest_location))

    return matches