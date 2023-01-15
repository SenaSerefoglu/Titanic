import random
import pandas as pd

trainDB = pd.read_csv('train.csv')
passangers = trainDB

def finish():
    print("Game Over")
    exit(0)

 
def random_passanger():
    index = random.randint(0, len(passangers))
    return passangers.iloc[index]

def main():
    lives = 2
    points= 100
    print("Welcome to the Titanic Survival Predictor")
    print("You have to survive the Titanic crash!!!")
    print("You msut predict the survival of the passengers")
    print("You have 2 lives")
    print("every true prediction gives you 100 point")
    print("When you lose all your lives, you can buy attiributes to increase your chances of survival")
    print("Lets start the game!!")
    while 1:
        passanger = random_passanger()
        print("Passanger details:")
        print("Passanger ID: ", passanger['PassengerId'])
        print("Passanger Name: ", passanger['Name'])
        print("Passanger Age: ", passanger['Age'])
        print("Passanger Sex: ", passanger['Sex'])
        print("Passanger Pclass: ",passanger['Pclass'])
        print("Passanger SibSp: ", passanger['SibSp'])
        print("Passanger Parch: ", passanger['Parch'])
        print("Passanger Ticket: ", passanger['Ticket'])
        print("Passanger Fare: ", passanger['Fare'])
        print("Passanger Cabin: ", passanger['Cabin'])
        print("Passanger Embarked: ", passanger['Embarked'])
        answer = input("Will this passanger survive? (y/n): ")
        if answer == 'y':
            if passanger['Survived'] == 1:
                print("Correct")
                points += 100
            else:
                print("Wrong")
                lives -= 1
                if lives == 0:
                    break
        elif answer == 'n':
            if passanger['Survived'] == 0:
                print("Correct")
                points += 100
            else:
                print("Wrong")
                lives -= 1
                if lives == 0:
                    break
        else:
            print("Wrong input")
    
    print("You have lost all your lives")
    print("You have ", points, " points")
    print("You can buy attributes to increase your chances of survival")



main()