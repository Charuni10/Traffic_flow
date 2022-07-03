import pandas as pd

def new_dataframe(new_data):
    data=pd.DataFrame(new_data, columns=['hour','min','day'])
    return data