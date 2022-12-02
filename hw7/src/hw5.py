# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light == "red":
        print("stop")
    elif light == "yellow":
        print("wait")
    elif light == "green":
        print("go")
    else:
        raise Exception("Undefined instruction for color: " + str(light))

car_at_light("green")

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(x,y):
    if isinstance(x, (int, float)) & isinstance(y, (int, float)):
        print(y - x)
    else:
        print("None")

safe_subtract(5, 9)

#except type error

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

# se n tem o birth deveris retornar um key error

dicio1 = {'name': 'Renato', 'last_name': 'Vassalo', 'birth': 1994}
dicio2 = {'name': 'Vicente', 'last_name': 'Lisboa', 'gender': 'male'}


def retrieve_age_eafp(dicio):
    try:
        return (2022 - dicio['birth'])
    except KeyError:
        print("We don't have that information")

def retrieve_age_lbyl(dicio2):
    if "birth" in dicio2:
        print(2022 - dicio2['birth'])
    else:
        print("We don't have that information")

 
# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

import pandas as pd

def read_data(file):
    try:
        df = pd.read_csv(file)
        print(df.head())
    except: FileNotFoundError
    print("This file doesn't exists")

read_data("teste.csv")


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

# change "elem" to "double" will solve the problem, because in the actual function we
# are adding the element and not the double of it as wished

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

# The error is in the ''strings = string+"_"+string'', we are adding the same string
# to correct we need to swith the first "string" to "strings" than the output will
# change to _I_am_Groot

### (c) Careful!
j=10
while j < 100:
   j += 1

# the error is because the while will be running forever, you need to specify a condition to
# stop like while j < 100: return (j)
# OBS: the original one is "j=10 while j > 0: j += 1" but we changed to j < 100 to avoid the
# infinity execution

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem

# you need to set the initial value of productory to 1 instead of 0, because every
# number multiplied by zero results in zero.

################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
from functools import reduce


def count_simba(list_of_strings):
    counter = list(map(lambda x: x.count("Simba"), list_of_strings))
    add = reduce(lambda a, b: a+b, counter)
    print(add)

example = ["Simba and Nala are lions.", "I laugh in the face of danger.",
        "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

count_simba(example)

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 
def get_day_month_year(listdt):
    dia,mes,ano = ([],[],[])
    for data in listdt:
        dia.append(data.day)
        mes.append(data.month)
        ano.append(data.year)
    final_df = pd.DataFrame(
    {'day': dia,
     'month': mes,
     'year': ano})
    print(final_df.head())
# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from geopy.distance import geodesic

lista_pontos = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

def compute_distance(coord_list):
    distances = []
    for pair in coord_list:
        dist_calc = geodesic(pair[0], pair[1]).km
        distances.append(dist_calc)
    print(distances)

compute_distance(lista_pontos)
#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#
import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable

from collections import Iterable
def sum_general_int_list(collection):
  for element in collection:
    if isinstance(element, Iterable):
      for x in sum_general_int_list(element):
        yield x
    else:
      yield element
    
example = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
sum(sum_general_int_list(example))
