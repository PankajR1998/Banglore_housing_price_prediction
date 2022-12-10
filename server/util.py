import json
import pickle
import numpy as np

__data_columns = None
__location = None
__model = None
def get_location_names():
    # load_saved_artifacts()
    return __location
def get_price_estimation(location, sqft, bath, bhk):
    # load_saved_artifacts()
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    global __data_columns
    global __location
    global __model
    
    print('loading artifacts....')
    with open('./artifacts/column_info.json','r') as f:
        __data_columns = json.load(f)['column_data']
        print(__data_columns[:5])
        __location = __data_columns[3:]
    
    print('location retived....')
    with open('./artifacts/banglore_price_prediction_model.pickle','rb') as f:
        __model = pickle.load(f)
    
    print('model retrived....')
    
if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_location_names())
    print(get_price_estimation(" devarachikkanahalli",2000,2,3))