
import unittest
import pytest
from pandas.testing import assert_frame_equal
from datetime import datetime
from liblucas.hw5_solutions import *
from geopy.distance import geodesic
import pandas as pd
from functools import reduce


################## 1 ###############
class Test_func1(unittest.TestCase):
    
    def test_car_at_light_g(self):
        assert car_at_light("green") == "go"
    
    def test_car_at_light_y(self):
        assert car_at_light("yellow") == "wait"
    
    def test_car_at_light_r(self):
        assert car_at_light("red") == "stop"
    
    def test_car_at_light_wrong(self):
        light = "purple"
        with pytest.raises(Exception, match = f"Undefined instruction for color: {light}"):
            car_at_light(light)


############## 2 ####################
class Test_func2(unittest.TestCase):    
    def test_safe_subtract1(self):
        assert safe_subtract(5, 3) == 2
    
    def test_safe_subtract2(self):
        with pytest.raises(TypeError):
            safe_subtract(5)

    


################ 3 ####################
class Test_func3(unittest.TestCase):
    def test_retrieve_age_eafp(self):
        output=retrieve_age_eafp({'name': 'Renato', 'last_name': 'Vassallo', 'birth': 1994})
        expected_output = 28
        self.assertEqual(output,expected_output)
        with self.assertRaises(KeyError):
            retrieve_age_eafp({'name': 'Vicente', 'last_name': 'Lisboa', 'gender': 'male'})

    def test_retrieve_age_lbyl(self):
        output=retrieve_age_lbyl({'name': 'Renato', 'last_name': 'Vassallo', 'birth': 1994})
        expected_output = 28
        self.assertEqual(output,expected_output)
        with self.assertRaises(KeyError):
            retrieve_age_lbyl({'name': 'Vicente', 'last_name': 'Lisboa', 'gender': 'male'})
    

    
############# 4 ############

class TestReadData(unittest.TestCase):
    def test_read_data1(self):
        output = read_data('sample_diabetes_mellitus_data.csv')
        expected_output = pd.read_csv('sample_diabetes_mellitus_data.csv')
        assert_frame_equal(output,expected_output,check_dtype = False)


############# 6 ##############

class TestCountWords(unittest.TestCase):
    
    def test_count_simba(self):
      example = ["Simba and Nala are lions.", "I laugh in the face of danger.","Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
      output = count_simba(example)
      expected_output = 3
      self.assertEqual(output,expected_output)

