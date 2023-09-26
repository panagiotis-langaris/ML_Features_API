import featuretools as ft
import pandas as pd
import json
from woodwork.logical_types import Categorical

def feature_extraction(json_data):
    
    ''' Load the JSON file and create a DataFrame '''
    data_list = json_data.get("data", [])
    
    ### Change format of file
    # From { customer_id_X: {
    #                   loan_0, loan_1, loan_2, ....
    # To   { customer_id_X // loan_0
    #        customer_id_X // loan_1
    #        .....
    loans = []
    for item in data_list:
        customer_loans = item.get("loans", [])
        for loan in customer_loans:
            loans.append(loan)

    loans_df = pd.DataFrame(loans)
    
    ### Change types of dataframe columns    
    # Convert date strings to datetime objects
    loans_df['loan_date'] = pd.to_datetime(loans_df['loan_date'], format='%d/%m/%Y')
    # Convert categorical values
    loans_df['term'] = loans_df['term'].astype('category')
    # Convert numeric columns to appropriate data types
    numeric_columns = ['customer_ID', 'amount', 'fee', 'loan_status', 'annual_income']
    loans_df[numeric_columns] = loans_df[numeric_columns].apply(pd.to_numeric, errors='coerce') # If an element cannot be converted to a numeric type, it will be set to NaN 
    
    
    ''' Using the feature tools library to extract features '''
    # Create an EntitySet
    es = ft.EntitySet(id = "customer_data")  

    es = es.add_dataframe(
        dataframe_name = "Loans",
        dataframe = loans_df,
        index = "loan_ID",
        logical_types = {
            "term": Categorical,
        }
    )    

    es.normalize_dataframe(base_dataframe_name ='Loans', new_dataframe_name ='customers', index = 'customer_ID')

    feature_matrix, feature_defs = ft.dfs(entityset = es, target_dataframe_name = "customers", max_depth = 1)
    
    ### Handle NaN values
    # ....
    # ....
    
    result = feature_matrix.to_json(orient="index")

    parsed = json.loads(result)
    json.dumps(parsed, indent=4)
    
    return parsed