import pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurance import HealthInsurance 

# loading model
model = pickle.load( open( r'models\model_linear_regression.pkl', 'rb' ) )

# initlize API
app = Flask( __name__ )

@app.route( '/predict', methods = ['POST'] )
def health_insurance_predict():
    test_json = request.get_json()
    
    if test_json:
        if isinstance( test_json , dict ):
            
            test_raw = pd.DataFrame( test_json , index = [0] )
        else:
            test_raw = pd.DataFrame( test_json , columns = test_json[0].keys() )
            
        # Initialize Rossmann Class
        pipeline = HealthInsurance()
        
        # feature engineering
        df1 = pipeline.feature_engineering( test_raw )
        
        # data preparation
        df2 = pipeline.data_prepatation( df1 )
        
        # get prediction
        df_response = pipeline.get_prediction( model, test_raw , df2 )
        
        return df_response
    
    else:
        
        return Response( '{}', status = 200 , mimetype = 'application/json' )
    
if __name__ == '__main__':
    
    app.run( '0.0.0.0', debug = True , use_reloader=False)
        
