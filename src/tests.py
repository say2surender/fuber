import pytest
import utils
import service

# unit tests for utils-----------//
def test_h_loc():
    assert utils.h_loc({"lat": 2, "long": 4}) == 6

def test_eu_distance():
    assert utils.eu_distance({"lat": 2, "long": 4}, {"lat": 2, "long": 6}) == 2


# unit tests for service-----------//
def test_ping():
    assert service.ping() == "ping success"

def test_calculate_available_taxis():
    assert type(service.calculate_available_taxis()) == type([])

def test_attrs_calculate_available_taxis():
    assert not (hasattr(service.calculate_available_taxis()[0], "taxi_id") and hasattr(service.calculate_available_taxis()[0], "category") and hasattr(service.calculate_available_taxis()[0], "curr_loc")
)
