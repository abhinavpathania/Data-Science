import pandas as pd

# Creating a DataFrame

df=pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Paris', 'Tokyo']
})


# Methods in Pandas
# 1. shape:
    # This method returns a tuple representing the dimensions of the DataFrame,
    # (number of rows, number of columns)
print("Shape of dataframe",df.shape)

# Attributes in Pandas
# 1. info():
    # This method provides a summary of the DataFrame, including the number of rows, columns, data types, memory usage, and the number of non-null values in each column.
print ("Info of dataframe",df.info())

# 2. head():
    # This method returns the first n rows of the DataFrame (default is 5).
print ("First five rows of data frame",df.head())

# 3. tail():
    # This method returns the last n rows of the DataFrame (default is 5).
print ("Last five rows of dataframe",df.tail())

#4. describe():
    # This method returns a summary statistics of the numerical columns in the DataFrame.
print("Statistical data of dataframe",df.describe())