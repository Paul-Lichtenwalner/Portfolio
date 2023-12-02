#Paul Lichtenwalner

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

colnames=['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5','Poker Hand'] 
df = pd.read_csv(r'poker-hand-training-true.csv', names=colnames, header=None)

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
