import os
import sys

import pandas as pd
import numpy as np
import dill
# import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


# with this function we can save any object as a pickle file that we are receiving from data transformation file
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)    #getting dir path

        os.makedirs(dir_path, exist_ok=True)   #create dir if not exists

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)    #saving the obj to file
 
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]       #ex:- param["Random Forest"] -> para = {'n_estimators': [8,16,32,64,128,256]}

            gs = GridSearchCV(model, para, cv=3)    #it will test every combination of parameters with 3 cross validation
            gs.fit(X_train, y_train)                #Trains the model with every parameter combination and finds the best one

            #setting the best params found to our model
            model.set_params(**gs.best_params_)

            # Train final model with best parameters
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e, sys)