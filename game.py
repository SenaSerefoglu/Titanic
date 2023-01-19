import random
import time
from main import *

passengers = trainDB
points = 0

def finish():
    print("Game Over")
    exit(0)

def random_passenger():
    index = random.randint(0, len(passengers))
    return passengers.iloc[index]

def guess():
    global points
    lives = 2
    print("\n\n")
    print("Welcome to the Titanic Survival Predictor")
    print("You have to survive the Titanic crash!!!")
    print("You have to estimate the survival of the passengers")
    print("You have 2 lives")
    print("Every true prediction gives you 100 points")
    print("When you lose all of your lives, you can buy attributes to increase your chance of survival")
    print("Lets start the game!!")
    print()
    while 1:
        passenger = random_passenger()
        print("Passenger details;")
        print("Passenger ID: ", passenger['PassengerId'])
        print("Passenger Age: ", int(passenger['Age']))
        print("Passenger Sex: ", passenger['Sex'])
        print("Passenger Pclass: ",passenger['Pclass'])
        print("Passenger SibSp: ", passenger['SibSp'])
        print("Passenger Parch: ", passenger['Parch'])
        print()
        answer = input("Do you think this passenger can survive? (y/n): ")
        print("\n\n")
        if answer == 'y':
            if passenger['Survived'] == 1:
                print("Correct")
                points += 100
            else:
                print("Wrong")
                lives -= 1
                if lives == 0:
                    break
        elif answer == 'n':
            if passenger['Survived'] == 0:
                print("Correct")
                points += 100
            else:
                print("Wrong")
                lives -= 1
                if lives == 0:
                    break
        else:
            print("Wrong input")
        print()

    print("You have lost all of your lives")
    print("You have ", points, " points")
    print("Now you can buy attributes to increase your chance of survival")
    time.sleep(2)
    print()

def choices(name, passenger):
    global points
    if name == 'age':
        if points < 50:
            print("You don't have enough points")
        else:
            points -= 50
            newage = int(input("Enter your new age: "))
            passenger['Age'] = newage
            print("Now you have ", points, " points\n")
    elif name == 'sex':
        if points < 100:
            print("You don't have enough points\n")
        else:
            points -= 100
            if passenger['Sex'].any() == 'female':
                passenger['Sex'] = 'male'
            else:
                passenger['Sex'] = 'female'
            print("Now you have ", points, " points\n")
    elif name == 'pclass':
        if points < 50:
            print("You don't have enough points\n")
        else:
            points -= 50
            newpclass = int(input("Enter your new passenger class: (1/2/3): "))
            passenger['Pclass'] = newpclass
            print("Now you have ", points, " points\n")
    elif name == 'sibsp':
        if points < 50:
            print("You don't have enough points\n")
        else:
            points -= 50
            newsibsp = int(input("Enter your new sibling/spouse count: "))
            passenger['SibSp'] = newsibsp
            print("Now you have ", points, " points\n")
    elif name == 'parch':
        if points < 50:
            print("You don't have enough points\n")
        else:
            points -= 50
            newparch = int(input("Enter your parent/children count: "))
            print("Now you have ", points, " points\n")
    else:
        print("Wrong input\n")
    print()

def buy():
    guess()
    age = random.choice(list(trainDB['Age'].unique()))
    sex = random.choice(list(trainDB['Sex'].unique()))
    pclass = random.choice(list(trainDB['Pclass'].unique()))
    sibsp = random.choice(list(trainDB['SibSp'].unique()))
    parch = random.choice(list(trainDB['Parch'].unique()))
    data = {'PassengerId': 1310, 'Pclass': pclass, 'Sex': sex, 'Age': age, 'SibSp': sibsp, 'Parch': parch, }
    passenger = pd.DataFrame(data, index=[0])
    print("Your attributes:")
    print("Age: ", age)
    print("Sex: ", sex)
    print("Passenger Class: ", pclass)
    print("Siblings/Spouses: ", sibsp)
    print("Parents/Children: ", parch)
    print()
    print("You have ", points, " points")
    print("You can buy the following attributes:")
    print("Change your age: 50 points")
    print("Change your gender: 100 points")
    print("Change your passenger class: 50 points")
    print("Change your sibling/spouse count: 50 points")
    print("Change your parent/children count: 50 points")
    print()
    choice = input("Do you want to change your age? (y/n): ")
    if choice == 'y':
        choices('age', passenger)
    choice = input("Do you want to change your gender? (y/n): ")
    if choice == 'y':
        choices('sex', passenger)
    choice = input("Do you want to change your passenger class? (y/n): ")
    if choice == 'y':
        choices('pclass', passenger)
    choice = input("Do you want to change your sibling/spouse count? (y/n): ")
    if choice == 'y':
        choices('sibsp', passenger)
    choice = input("Do you want to change your parent/children count? (y/n): ")
    if choice == 'y':
        choices('parch', passenger)
    print("Your final attributes:")
    print("Age: ", passenger.iloc[0]['Age'])
    print("Sex: ", passenger.iloc[0]['Sex'])
    print("Passenger Class: ", passenger.iloc[0]['Pclass'])
    print("Siblings/Spouses: ", passenger.iloc[0]['SibSp'])
    print("Parents/Children: ", passenger.iloc[0]['Parch'])
    if passenger['Sex'].any() == 'female':
        passenger['Sex_female'] = 1
        passenger['Sex_male'] = 0
    else:
        passenger['Sex_female'] = 0
        passenger['Sex_male'] = 1
    passenger.drop('Sex', axis=1, inplace=True)
    prediction = model.predict(passenger)
    print("Now lets see if you survived")
    time.sleep(3)
    if prediction == 1:
        print("Congratulations. You survived")
    else:
        print("You died. Better luck next time (if there is a next time)")
    finish()


buy()