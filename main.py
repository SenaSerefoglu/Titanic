import pandas as pd
import numpy as np

# Importing the dataset
testDB = pd.read_csv('testt.csv')
trainDB = pd.read_csv('train.csv')

# Dropping the columns that are not needed
testDB = testDB.drop(['Ticket', 'Cabin', 'Fare', 'Embarked', 'Name'], axis=1)
trainDB = trainDB.drop(['Ticket', 'Cabin', 'Fare', 'Embarked', 'Name'], axis=1)

# Replacing the NaN values with the mean of the column
testDB["Age"] = testDB["Age"].replace(np.NaN, testDB["Age"].mean())
trainDB["Age"] = trainDB["Age"].replace(np.NaN, trainDB["Age"].mean())