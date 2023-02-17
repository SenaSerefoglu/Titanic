import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score
from matplotlib.ticker import MaxNLocator

# Importing the dataset
testDF = pd.read_csv('test.csv')
trainDF = pd.read_csv('train.csv')
#print(trainDF.head())
#print(trainDF.describe())
#print(trainDF.nunique())

trainDB = trainDF.copy()
testDB = testDF.copy()


# Save passengerId column for submission
passengerId = testDF['PassengerId']


# Preprocessing

# Deletion of the columns that are not needed
trainDF.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
testDF.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# Check for missing data
plt.subplot(1, 2, 1)
sns.heatmap(trainDF.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.subplot(1, 2, 2)
sns.heatmap(testDF.isnull(), yticklabels=False, cbar=False, cmap='viridis')
#plt.show()

# Drop the Cabin column
trainDF.drop('Cabin', axis=1, inplace=True)
testDF.drop('Cabin', axis=1, inplace=True)

# Fill the missing values in the Embarked column in trainDF and Fare column in testDF
trainDF['Embarked'].fillna(trainDF['Embarked'].mode()[0], inplace=True)
testDF['Fare'].fillna(testDF['Fare'].mode()[0], inplace=True)

# Append the test data to the train data for age prediction model
ageDF = pd.concat([trainDF, testDF], axis=0)
# Drop the Survived column and none values in the age column
ageDF.drop(['Survived'], axis=1, inplace=True)
ageDF.dropna(subset=['Age'], inplace=True)

# Creation of dummies for the Embarked and Sex columns for both train and age dataframes
trainDF = pd.get_dummies(trainDF, columns=['Embarked', 'Sex'])
ageDF = pd.get_dummies(ageDF, columns=['Embarked', 'Sex'])
testDF = pd.get_dummies(testDF, columns=['Embarked', 'Sex'])

sns.heatmap(trainDF.corr(), annot=True, cmap='viridis')
#plt.show()
sns.heatmap(ageDF.corr(), annot=True, cmap='viridis')
#plt.show()

# Spliting the age data into train and test
train, test = train_test_split(ageDF, test_size=0.3, random_state=42)
train_x = train.drop(['Age'], axis=1)
train_y = train['Age']
test_x = test.drop(['Age'], axis=1)
test_y = test['Age']


# Model Training
lr = LinearRegression()
lr.fit(train_x, train_y)
lr_pred = lr.predict(test_x)

print('Linear Regression')
print('Mean Squared Error: ', mean_squared_error(test_y, lr_pred))
print('Mean Absolute Error: ', mean_absolute_error(test_y, lr_pred))
print('R2 Score: ', r2_score(test_y, lr_pred))
print()

# Fill the missing values in the age column of trainDF and testDF

# Pull nan values from the age column
ageNone = trainDF[trainDF['Age'].isnull()]
# Drop the age column and the survived column
ageNone.drop(['Age', 'Survived'], axis=1, inplace=True)
# Predict the age values
agePred = lr.predict(ageNone)
# Fill the age column with the predicted values
trainDF.loc[trainDF['Age'].isnull(), 'Age'] = agePred

# Pull nan values from the age column
ageNone = testDF[testDF['Age'].isnull()]
# Drop the age column
ageNone.drop('Age', axis=1, inplace=True)
# Predict the age values
agePred = lr.predict(ageNone)
# Fill the age column with the predicted values
testDF.loc[testDF['Age'].isnull(), 'Age'] = agePred


# Logistic Regression
train_x = trainDF.drop(['Survived'], axis=1)
train_y = trainDF['Survived']
test_x = testDF

# Model Training
model = LogisticRegression()
model.fit(train_x, train_y)
lr_pred = model.predict(test_x)

# save the predictions to a csv file
predictions = pd.DataFrame({'PassengerId': passengerId, 'Survived': lr_pred})
predictions.to_csv('predictions.csv', index=False)


def visualize():
    # Visualizing the data of the training set with columns 'Pclass' and 'Survived'
    _, ax = plt.subplots()
    Pclass = trainDB.groupby('Pclass').Survived.sum()*100/trainDB.groupby('Pclass').Survived.count()
    ax.bar(Pclass.index, Pclass.values)
    ax.set(ylim=(0, 100))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel('Pclass')
    ax.set_ylabel('Survived Percentage')
    ax.set_title('Pclass vs Survived')

    # Visualizing the data of the training set with columns Sex and Survived
    _, ax = plt.subplots()
    Sex = trainDB.groupby('Sex').Survived.sum()*100/trainDB.groupby('Sex').Survived.count()
    ax.bar(Sex.index, Sex.values)
    ax.set(ylim=(0, 100))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel('Sex')
    ax.set_ylabel('Survived Percentage')
    ax.set_title('Sex vs Survived')

    # Visualizing the data of the training set with columns 'Age' and 'Survived'
    _, ax = plt.subplots(figsize=(12, 4))
    Age = trainDB.groupby('Age').Survived.sum()*100/trainDB.groupby('Age').Survived.count()
    ax.bar(Age.index.astype(int), Age.values, width=0.5)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel('Age')
    ax.set_ylabel('Survived Percentage')
    ax.set_title('Age vs Survived')

    # Visualizing the data of the training set with columns 'SibSp' and 'Survived'
    _, ax = plt.subplots()
    SibSp = trainDB.groupby('SibSp').Survived.sum()*100/trainDB.groupby('SibSp').Survived.count()
    ax.bar(SibSp.index, SibSp.values)
    ax.set(ylim=(0, 100))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel('SibSp')
    ax.set_ylabel('Survived Percentage')
    ax.set_title('SibSp vs Survived')

    # Visualizing the data of the training set with columns 'Parch' and 'Survived'
    _, ax = plt.subplots()
    Parch = trainDB.groupby('Parch').Survived.sum()*100/trainDB.groupby('Parch').Survived.count()
    ax.bar(Parch.index, Parch.values)
    ax.set(ylim=(0, 100))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel('Parch')
    ax.set_ylabel('Survived Percentage')
    ax.set_title('Parch vs Survived')

    # Showing the plots
    plt.show()

if __name__ == '__main__':
    visualize()