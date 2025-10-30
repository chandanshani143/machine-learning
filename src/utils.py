import os
import sys

import pandas as pd
import numpy as np
import dill
import pickle

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