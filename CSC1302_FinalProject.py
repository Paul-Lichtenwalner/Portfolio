import pandas as pd

df = pd.read_csv(r'poker-hand-training-true.csv')

colnames=['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5','Poker Hand'] 

df = pd.read_csv(r'poker-hand-training-true.csv', names=colnames, header=None)

df.dropna()

print(df[10:311])

#Statistics
#Creates a new DataFrame to hold the statistic
#values of the main DataFrame
rowNames = ['Mean', 'Median', 'Variance', 'Standard Deviation']
statDF = pd.DataFrame(index = rowNames, columns = colnames)

#Calculate the mean for each column and enter it
#into the statistics dataframe
colMeans = df.mean().round(2)
statDF.loc['Mean'] = colMeans

#Calculate the median for each column and enter it
#into the statistics dataframe
colMedian = df.median()
statDF.loc['Median'] = colMedian

#Calculate the variance for each column and enter it
#into the statistics dataframe
colVar = df.var().round(2)
statDF.loc['Variance'] = colVar

#Calculate the standard deviation for each column and enter it
#into the statistics dataframe
colSTD = df.std().round(2)
statDF.loc['Standard Deviation'] = colSTD

#Print the statistics dataframe
print(statDF.to_string())