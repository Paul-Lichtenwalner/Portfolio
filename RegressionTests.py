#Paul Lichtenwalner
#plichtenwalner1@student.gsu.edu
#002682843

# Import libraries
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import train_test_split

# Load the dataset
#colnames=['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5','Poker Hand']
#dataset = pd.read_csv(r'C:\Users\plichtenwalner1\Desktop\poker-hand-training-true.csv', names=colnames, header=None)
#dataset.dropna()

# Split the dataset into training and testing sets
#X = dataset.iloc[:, :-1].values
#y = dataset.iloc[:, -1].values
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
#regressor = LinearRegression()
#regressor.fit(X_train, y_train)

# Make predictions on the test set
#y_pred = regressor.predict(X_test)

# Evaluate the model
#from sklearn.metrics import mean_squared_error, r2_score
#mse = mean_squared_error(y_test, y_pred)
#r2 = r2_score(y_test, y_pred)
#print('Mean squared error: ', mse)
#print('Coefficient of determination (R^2): ', r2)

#plt.scatter(X, y, color='red')
#plt.plot(X_test, y_pred, color='blue')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()


# Generate some random data
#x = np.array([1, 2, 3, 4, 5])
#y = np.array([2, 4, 5, 4, 6])

# Create a linear regression object
#model = LinearRegression()

# Fit the model using our data
#model.fit(x.reshape(-1, 1), y)

# Generate some new data to make predictions on
#x_new = np.array([6, 7, 8, 9, 10])

# Use the model to make predictions on the new data
#y_pred = model.predict(x.reshape(-1, 1))

# Plot the data and the regression line
#plt.scatter(x, y, color='red')
#plt.plot(x, y_pred, color='blue')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()

#colnames=['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5','Poker Hand']
#dataset = pd.read_csv(r'C:\Users\plichtenwalner1\Desktop\poker-hand-training-true.csv', names=colnames, header=None)
#dataset.dropna()

#x = np.array(dataset.iloc[:, 10])
#y = np.array(dataset.iloc[:, 1])

#model = LinearRegression()
#model.fit(x.reshape(-1, 1), y)
#y_pred = model.predict(x.reshape(-1, 1))

#plt.scatter(x, y, color = 'red')
#plt.plot(x, y_pred, color = 'blue')
#plt.xlabel('Card 1')
#plt.ylabel('Poker Hand')
#plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

colnames=['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5','Poker Hand'] 
df = pd.read_csv(r'C:\Users\plichtenwalner1\OneDrive - Georgia State University\Desktop\CSSpring_2023\CSFinal_Spring2023\poker-hand-training-true.csv', names=colnames, header=None)

X = df.drop('Poker Hand', axis=1) # Independent variables
y = df['Poker Hand'] # Dependent variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print(classification_report(y_test, y_pred))

coefficients = pd.DataFrame({'feature': X.columns, 'coefficient': logreg.coef_[0]})
sns.barplot(x='coefficient', y='feature', data=coefficients)
plt.title('Coefficients of the Logistic Regression Model')
plt.show()
