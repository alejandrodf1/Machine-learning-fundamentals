import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def salary_experience_series(X,Y,regressor):
    viz_train =plt
    viz_train.scatter(X, Y, color = 'blue')
    viz_train.plot(X, regressor.predict(X), color = 'black')
    viz_train.title('Salary vs Experience')
    viz_train.xlabel('Experience (years)')
    viz_train.ylabel('Salary (usd)')


def validation_graph(X,Y, regressor):
    viz_train =plt
    viz_train.scatter(X, Y, color = 'red')
    viz_train.plot(X, regressor.predict(X), color = 'black')
    viz_train.title('Salary vs Experience')
    viz_train.xlabel('Experience (years)')
    viz_train.ylabel('Salary (usd)')

#CHALLENGE GRAPHS

def trainig_graph(X,Y,regressor, countries_encoded, encoder):
    fig = plt.figure()
    viz_train = fig.add_subplot(111,projection='3d')
    viz_train.scatter(X['Aexperiencia'],X['countries'], Y, color='blue')
    viz_train.plot_trisurf(X['Aexperiencia'],X['countries'], regressor.predict(X),color = 'black', alpha=0.5)
    viz_train.set_title('Salary vs experience vs Work Countries')
    viz_train.set_xlabel('Experiece')
    viz_train.set_ylabel('country')
    viz_train.set_zlabel('salary')
    viz_train.set_yticks(range(len(countries_encoded)))
    viz_train.set_yticklabels(encoder.inverse_transform(countries_encoded))
    viz_train.azim=-10
    fig.show

def testing_graph(X,X_train, Y, regressor, countries_encoded, encoder):
    fig = plt.figure()
    viz_train = fig.add_subplot(111,projection='3d')
    viz_train.scatter(X['Aexperiencia'],X['countries'], Y, color='blue')
    viz_train.plot_trisurf(X_train['Aexperiencia'],X_train['countries'], regressor.predict(X_train),color = 'black', alpha=0.5)
    viz_train.set_title('Salary vs experience vs Work Countries')
    viz_train.set_xlabel('Experiece')
    viz_train.set_ylabel('country')
    viz_train.set_zlabel('salary')
    viz_train.set_yticks(range(len(countries_encoded)))
    viz_train.set_yticklabels(encoder.inverse_transform(countries_encoded))
    viz_train.azim=-10
    fig.show