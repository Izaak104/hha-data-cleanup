#libraries are imported to ensure proper reading of the various file formats
import pandas as pd
import datetime as dt
import uuid
import numpy as np

#upload raw data
df = pd.read_csv('hha-data-cleanup\School_Learning_Modalities.csv')

#run code to display content of raw
print(df)

#get the count of the rows and columns
df.shape

#run code to print out the names of columns in the dataframe
list(df.columns)

#run code to insert underscore (_) into the columns to make it more human & machine readable
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')

#change all column names to upper case
df.columns = df.columns.str.upper()

#list types of data within columns
df.dtypes

#identify dataset that are stings and save them as such
strings = df.select_dtypes(include=['object']).columns
strings

numbers = df.select_dtypes(include=['int64', 'float64']).columns
numbers

#run codes to convert column types to right types
#in this case from "object" to "string"
df['DISTRICT_NAME'] = df['DISTRICT_NAME'].astype(str)
df['DISTRICT_NAME']

df['WEEK'] = df['WEEK'].astype(str)
df["WEEK"]

df['LEARNING_MODALITY'] = df['LEARNING_MODALITY'].astype(str)
df['LEARNING_MODALITY']

df['CITY'] = df['CITY'].astype(str)
df['CITY']

df['STATE'] = df['STATE'].astype(str)
df['STATE']

#remove duplicate rows
df.drop_duplicates(keep='first', inplace= True)
df.drop_duplicates

#get the total missing value per column
df.isnull().sum()









