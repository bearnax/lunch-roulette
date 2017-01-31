import pytest
from lunch_roulette import roulette as rl

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_is_json_loading():
    """the data type of the participants variable is a dictionary"""
    assert(type(rl.participant_dict) == dictionary)
    assert(type(rl.lunch_dict) == dictionary)
