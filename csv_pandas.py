import pandas as pd 

df = pd.read_csv('data/hrdata.csv')
print(df)

df1 = pd.read_csv('data/hrdata.csv', index_col='Name')
print(df1)

df2 = pd.read_csv('data/hrdata.csv' ,
        index_col= 'Name' ,
         parse_dates=['Hire Date'])
print(df2)

df3 = pd.read_csv('data/hrdata.csv' ,
        index_col= 'Employee' ,
         parse_dates=['Hired'], 
         header= 0,
         names= ['Employee','Hired','Salary','Sick Days'])
print(df3)