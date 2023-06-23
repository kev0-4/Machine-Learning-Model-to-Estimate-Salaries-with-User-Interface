import json
import pickle
import pandas as pd
import numpy as np
import sklearn


__position = None
__data_columns = None
__model = None
ct = None

def get_estimated_salary(age,gender, education, position, yoe):
    global ct
    with open('./artifacts/column_transformer.pickle','rb') as f2:
        ct = pickle.load(f2)
    with open("./artifacts/Salary_Data.pickle","rb") as f1:
        __model = pickle.load(f1)

    new_data = pd.DataFrame({'Age':[age],'Gender':[gender],'Education':[education],
    'position':[position],'YOE':[yoe]})

    new_data_encoded = ct.transform(new_data)
    salary_pred = __model.predict(new_data_encoded)
    salary_pred = float(salary_pred)
    return round(salary_pred,2)

def get_position():
    global  __data_columns
    global __position
    with open("./artifacts/colums.json", "r") as f:
        __data_columns = json.load(f)['data_colums']
        __position = __data_columns[7:]
    return __position

def load_saved_artifacts():
    print("Loading saved artifacts..")
    global __data_columns
    global __position
    global __model
    global ct

    #loading data_columns 
    with open("./artifacts/colums.json", "r") as f:
        __data_columns = json.load(f)['data_colums']
        __position = __data_columns[7:]
    
    #loading ml model
    with open("./artifacts/Salary_Data.pickle","rb") as f1:
        __model = pickle.load(f1)

    with open('./artifacts/column_transformer.pickle','rb') as f2:
        ct = pickle.load(f2)
    print("Artifacts loaded...")



if __name__ == '__main__':
    load_saved_artifacts()
    print(get_position())
    print(get_estimated_salary(30,'Male','PhD','Analyst',5))
    print(get_estimated_salary(45,'Female',"Master's",'Manager',12))
    print(get_estimated_salary(19,'Male',"Bachelor's",'Engineer',2))