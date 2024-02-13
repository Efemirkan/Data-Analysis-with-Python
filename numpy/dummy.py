import numpy as np
import pandas as pd

#values = [22.50, 24.9, 28.7, 27.3]

#numpy_array = np.array(values)


#conversion = numpy_array * 1.8 +32
'''
dates = pd.date_range("20220226", periods=6)
#6 for six days from period 4 for four coloum created
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

dates2 = pd.date_range("20220226", periods=8)
#8 for six days from period 6 for four coloum created
df2 = pd.DataFrame(np.random.randn(8,6), index=dates2, columns=list('ABCDEF'))
print(df2)'''
'''
# dict key is column value is row

df = pd.DataFrame({
    'A' : 1.,
    'B' : pd.Timestamp("20220226"),
    'C' : pd.Series(1, index=list(range(4)), dtype='float64'),
    'D' : np.array([3] * 4, dtype="int32"),
    'E' : pd.Categorical(["test", "train", "test", "train"]),
    'F' : 'foo'

})

print(df)'''

df = pd.read_csv('file.csv', delimiter=" ")

df.head() # show dataS
df.head(10) # show first 10 data
df.tail(10) # last 10

df.index # tell howmany rows
df.columns # tells columns names
df.values # show data rows in arrays
df.describe # statistics summary of data such as mean count min max
# only age and education colums
df[['Age', 'Education']] # 2D array
df[df["Age"] > 30] # who is older than 30
df[(df['Age'] > 30) & (df['Education'] > 20)]


#data = pd.Series([1, 2, 3, 4, 5, None, 6])
#print(data)

#print(values)
#print(conversion)