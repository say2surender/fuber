import pytest
import utils

def test_h_loc():
    assert utils.h_loc({"lat": 2, "long": 4}) == 6

def test_eu_distance():
    assert utils.eu_distance({"lat": 2, "long": 4}, {"lat": 2, "long": 6}) == 2
