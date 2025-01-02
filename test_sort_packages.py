import pytest
from sort_packages import sort

def test_standard():
    # Neither bulky nor heavy
    # Volume = 10×10×10 = 1,000 (<1,000,000), dimensions <150, mass <20
    assert sort(10.0, 10.0, 10.0, 10.0) == "STANDARD"

def test_bulky():
    # Bulky but not heavy
    # Dimensions >=150 or volume >=1,000,000, but mass <20
    assert sort(200.0, 200.0, 200.5, 10.0) == "SPECIAL"

def test_heavy():
    # Heavy but not bulky
    # mass >=20, but volume <1,000,000 and dimensions <150
    assert sort(10.0, 10.0, 10.0, 25.5) == "SPECIAL"

def test_rejected():
    # Both bulky and heavy
    # volume >=1,000,000 or dimension>=150, plus mass>=20
    assert sort(200.5, 200.5, 200.5, 25.5) == "REJECTED"

def test_edge_case_bulky():
    # Exactly at the bulky threshold for dimension
    # dimension = 150 => bulky, mass <20 => not heavy
    assert sort(150.0, 100.0, 100.0, 19.5) == "SPECIAL"

def test_edge_case_heavy():
    # Exactly at the heavy threshold
    # mass=20 => heavy, but we keep volume <1,000,000 => not bulky
    assert sort(149.0, 149.0, 1.0, 20.0) == "SPECIAL"

def test_edge_case_standard():
    # Just below thresholds for bulky and heavy
    # All dimensions <150, volume <1,000,000, mass<20
    assert sort(149.0, 100.0, 50.0, 19.0) == "STANDARD"

def test_large_bulky():
    # Large bulky dimensions
    # Volume >>1,000,000 => bulky, mass<20 => not heavy
    assert sort(1000.0, 1000.0, 1000.0, 10.0) == "SPECIAL"

def test_large_heavy():
    # Very heavy but not bulky
    # mass=100 => heavy, but volume<1,000,000 => not bulky
    assert sort(100.0, 100.0, 99.0, 100.0) == "SPECIAL"

def test_invalid_input_negative():
    # Negative values => ValueError
    with pytest.raises(ValueError):
        sort(-100.0, 100.0, 100.0, 10.0)

def test_invalid_input_zero():
    # Zero values => ValueError
    with pytest.raises(ValueError):
        sort(0.0, 100.0, 100.0, 10.0)
