#importing pandas toolkit
import pandas as pd

#list of column names
colnames=['Idx','Record_Type','Customer Name', 'Customer ID', 'Customer Open Date', 'Last Consulted Date', 'Vaccination Type', 'Doctor Consulted', 'State', 'Country', 'Date of Birth', 'Active Customer']

#reading the data from pipe delimited data file and creating a Pandas DataFrame from the data
df = pd.read_csv("data.txt", sep = '|', names=colnames, dtype={'Idx':str,'Record_Type':str,'Customer Name':str, 'Customer ID':str, 'Customer Open Date':str, 'Last Consulted Date':str, 'Vaccination Type':str, 'Doctor Consulted':str, 'State':str, 'Country':str, 'Date of Birth':str, 'Active Customer':str})

#pre-processing the data
df = df[df['Record_Type']=='D']
df = df.iloc[: , 2:]
df['Customer Open Date'] = pd.to_datetime(df['Customer Open Date'], format="%Y%m%d")
df['Last Consulted Date'] = pd.to_datetime(df['Last Consulted Date'], format="%Y%m%d")
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], format="%d%m%Y")

#printing the DataFrame
print(df)
