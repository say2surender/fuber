import math
import pytest

def h_loc(latlong):
    """Return the sum of x,y cco-ordinates.

    >>> h_loc({"lat": 2, "long": 4})
    6
    """
    return latlong["lat"]+latlong["long"]

def eu_distance(loc1, loc2):
    """Return the distance between two points in a cartesian plane(x1, y1), (x2, y2).

    >>> eu_distance({"lat": 2, "long": 2}, {"lat": 2, "long": 4})
    2
    """
    ed =  math.hypot(loc2["lat"] - loc1["lat"], loc2["long"] - loc1["long"])
    return ed


def test_h_loc():
    assert h_loc({"lat": 2, "long": 4}) == 6

def test_eu_distance():
    assert eu_distance({"lat": 2, "long": 4}, {"lat": 2, "long": 6}) == 2
