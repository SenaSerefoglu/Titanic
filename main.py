import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Importing the dataset
testDB = pd.read_csv('test.csv')
trainDB = pd.read_csv('train.csv')

# Dropping the columns that are not needed
testDB = testDB.drop(['Ticket', 'Cabin', 'Fare', 'Embarked', 'Name'], axis=1)
trainDB = trainDB.drop(['Ticket', 'Cabin', 'Fare', 'Embarked', 'Name'], axis=1)

# Replacing the NaN values with the mean of the column
testDB["Age"] = testDB["Age"].replace(np.NaN, testDB["Age"].mean())
trainDB["Age"] = trainDB["Age"].replace(np.NaN, trainDB["Age"].mean())

# checking for NaN values
# print(testDB.isnull().sum())
# print(trainDB.isnull().sum())

# visualizing the data of the training set with columns 'Pclass' and 'Survived'
fig, ax = plt.subplots()
Pclass = trainDB.groupby('Pclass').Survived.sum()*100/trainDB.groupby('Pclass').Survived.count()
ax.bar(Pclass.index, Pclass.values)
ax.set(ylim=(0, 100))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('Pclass')
ax.set_ylabel('Survived Percentage')
ax.set_title('Pclass vs Survived')

# visualizing the data of the training set with columns Sex and Survived
fig, ax = plt.subplots()
Sex = trainDB.groupby('Sex').Survived.sum()*100/trainDB.groupby('Sex').Survived.count()
ax.bar(Sex.index, Sex.values)
ax.set(ylim=(0, 100))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('Sex')
ax.set_ylabel('Survived Percentage')
ax.set_title('Sex vs Survived')

# visualizing the data of the training set with columns 'Age' and 'Survived'
fig, ax = plt.subplots(figsize=(12, 4))
Age = trainDB.groupby('Age').Survived.sum()*100/trainDB.groupby('Age').Survived.count()
ax.bar(Age.index.astype(int), Age.values, width=0.5)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('Age')
ax.set_ylabel('Survived Percentage')
ax.set_title('Age vs Survived')

# visualizing the data of the training set with columns 'SibSp' and 'Survived'
fig, ax = plt.subplots()
SibSp = trainDB.groupby('SibSp').Survived.sum()*100/trainDB.groupby('SibSp').Survived.count()
ax.bar(SibSp.index, SibSp.values)
ax.set(ylim=(0, 100))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('SibSp')
ax.set_ylabel('Survived Percentage')
ax.set_title('SibSp vs Survived')

# visualizing the data of the training set with columns 'Parch' and 'Survived'
fig, ax = plt.subplots()
Parch = trainDB.groupby('Parch').Survived.sum()*100/trainDB.groupby('Parch').Survived.count()
ax.bar(Parch.index, Parch.values)
ax.set(ylim=(0, 100))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('Parch')
ax.set_ylabel('Survived Percentage')
ax.set_title('Parch vs Survived')

# Showing the plots
plt.show()