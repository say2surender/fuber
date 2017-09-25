import math

def h_loc(latlong):
    return latlong[0]+latlong[1]

def eu_distance(loc1, loc2):
    ed =  math.hypot(loc2["lat"] - loc1["lat"], loc2["long"] - loc1["long"])
    return ed
