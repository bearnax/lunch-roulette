from app import load_lunch_spots


def test_location_loading():
    temp_list = load_lunch_spots("data/lunch_spots_test.json")
    assert len(temp_list) == 4
