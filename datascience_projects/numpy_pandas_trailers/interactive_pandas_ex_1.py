# %% [markdown]
# # Intro to Pandas
# It is used for data manipulation and analysis. It provides special data structures and operations for the manipulation of numerical tables and time series.
#

# %% [markdown]
# ## Series and DataFrame
# - Series: a one-dimensional labeled array holding data of any type
# - DataFrame: a two dimensional data structure  holds data like a two-dimension array or a table with rows and columns.
#
#

# %%
import pandas as pd
import numpy as np

A = np.array([1, 3, 5, 6, 8])
print(A)
S = pd.Series([1, 3, 5, 6, 8])
print(S.index)
print(S.values)
# both are the same type:
print(type(A), type(S.values))
## defining Series objects with individual indices
fruits = ["apples", "oranges", "cherries", "pears", "peaches"]
quantities = [20, 33, 52, 10, 42]
S1 = pd.Series(quantities, index=fruits)
# print(S1)
quantities_2 = [10, 20, 30, 40, 50]
# Add two series with same indices
S2 = pd.Series(quantities_2, index=fruits)
print(S1 + S2)
print("--------------")
print("The indices do not have to be the same for the Series addition")
# The index will be the "union" of both indices. If an index doesn't occur in both Series, the value for this Series will be NaN:
# However the length of the two series should be the same
fruits_2 = ["apples", "oranges", "cherries", "pears", "grapes"]
S3 = pd.Series(quantities_2, index=fruits_2)
print(S1 + S3)
print("--------------")
print("Accessing elements of a Series")
print(S1["apples"])
# print(S1[0]) # treating keys as positions is deprecated
print("--------------")
print(
    "Series objects can also be accessed by multiple indexes at the same time"
)
print(S1[["apples", "cherries", "oranges"]])
print("--------------")
print("scalar and mathematical operations - similar to numpy")
print((S1 * 2) + 100)
print(np.exp(S1))
print("--------------")
print("a function can be applied to the series")
# Series.apply(func, convert_dtype=True, args=(), **kwds)
# The function "func" will be applied to the Series and it returns either a Series or a DataFrame, depending on "func".
# The parameter "convert_dtype" specifies whether to convert the data type of the Series to a numeric type.
print(S1.apply(np.sqrt))
print(S1.apply(lambda x: x if x > 50 else x + 10))

print("--------------")
print(
    "A series can be seen as an ordered Python dictionary with a fixed length"
)
print("apples" in S1, "mangoes" in S1)
print("--------------")
print("Filtering with a Boolean array")
print(S1[S1 > 30])

# %%
# Creating Series objects from dictionaries
# The keys of the dictionary are used as indices

cities = {
    "London": 8615246,
    "Berlin": 3562166,
    "Madrid": 3165235,
    "Rome": 2874038,
    "Paris": 2273305,
    "Vienna": 1805681,
    "Bucharest": 1803425,
    "Hamburg": 1760433,
    "Budapest": 1754000,
    "Warsaw": 1740119,
    "Barcelona": 1602386,
    "Munich": 1493900,
    "Milan": 1350680,
}

city_series = pd.Series(cities)

print(city_series)
print("--------------")
my_cities = ["London", "Paris", "Zurich", "Berlin", "Stuttgart", "Hamburg"]

my_city_series = pd.Series(cities, index=my_cities)
## isnull() & notnull()
print(my_city_series.isnull())
print(my_city_series.notnull())
print("--------------")
## NaN - missing data
my_city_series = pd.Series(cities, index=my_cities)
print("--------------")
print(my_city_series)
## Filtering out missing data using notnull() and dropna()
print("--------------")
print(my_city_series[my_city_series.notnull()])
print("--------------")
print(my_city_series.dropna())
## Filling in missing data using fillna()
print("--------------")
print(my_city_series.fillna(0))
