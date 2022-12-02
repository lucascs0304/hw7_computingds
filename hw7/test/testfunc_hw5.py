
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
    

############ 7 ##############
class Test_func7(unittest.TestCase):
    def test_get_day_month_year_valid(self):
        input = ['03-04-2000','09-10-1993','20-03-1995']
        input = [datetime.strptime(date, '%d-%m-%Y') for date in input]
        true_data = [[3,4,2000],[9,10,1993],[20,3,1995]]
        expected_output = pd.DataFrame(true_data, columns = ['day', 'month', 'year'])
        output = get_day_month_year(input)
        assert_frame_equal(output, expected_output)



############# 8 #############
class Test_func8(unittest.TestCase):        
    def test_compute_distance(self):
        expected_output = [349.1115083262352, 1541.8564339502927]
        assert compute_distance([((12,6), (15, 7)), ((20, 10),(10, 20))]) == expected_output


########### 9 ###############
class Test_func9(unittest.TestCase):    
    def test_sum_general_int_list(self):
        expected_output = 48
        assert sum_general_int_list([[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]) == expected_output
