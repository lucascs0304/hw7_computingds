
import unittest
import pytest
from pandas.testing import assert_frame_equal
import datetime
from liblucas.hw5_solutions import *
from geopy.distance import geodesic

#from src.hw5 import *
#import pandas as pd
#from datetime import datetime

#import sys
#sys.path.insert(0, '../src')
#import unittest
#from hw5 import *




################## 1 ###############

class Test_func1(unittest.TestCase):
    
    def test_car_at_light_g(self):
        assert car_at_light("green") == "go"
    
    def test_car_at_light_y(self):
        assert car_at_light("yellow") == "wait"
    
    def test_car_at_light_r(self):
        assert car_at_light("read") == "stop"
    
    def test_car_at_light_wrong(self):
        assert car_at_light("purple") == Exception("Undefined instruction for color: purple")

# This last one is probably wrong because exception isn't like that syntax   


############## 2 ####################

class Test_func2(unittest.TestCase):
    
    def test_safe_subtract1(self):
        assert safe_subtract(5, 3) == 2
        
        



################ 3 ####################

dicio1 = {'name': 'Renato', 'last_name': 'Vassalo', 'birth': 1994}
dicio2 = {'name': 'Vicente', 'last_name': 'Lisboa', 'gender': 'male'}


def retrieve_age_eafp(dictionary):
    try:
        birth_year = dictionary["birth"]
    except KeyError:
        print("Input is missing birth key.")
        return None
    return datetime.datetime.now().year - birth_year


def retrieve_age_lbyl(dictionary):
    if "birth" in dictionary.keys():
        return datetime.datetime.now().year - dictionary["birth"]
    else:
        print("Input is missing birth key.")
        return None
    
#class Test_func3(unittest.TestCase):
#    def test_retrieve_age_eafp(self):
#        assert 





############# 8 #############


class Test_func8(unittest.TestCase):
        
    def test_compute_distance(self):
        expected_output = [349.1115083262352, 1541.8564339502927]
        assert compute_distance([((12,6), (15, 7)), ((20, 10),(10, 20))]) == expected_output
        
