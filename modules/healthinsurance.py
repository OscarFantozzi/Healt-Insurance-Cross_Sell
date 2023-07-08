import pickle
import numpy as np
import pandas as pd

class HealthInsurance:
    
    def __init__( self ):
        self.home_path                    =  r'\Users\oscar\Documents\repos\pa004\features_transformation\\'
        self.annual_premium_scaler        = pickle.load( open( self.home_path + 'annual_premium_scaler.pkl' , 'rb' )  )
        self.fe_policy_sales_channel      = pickle.load( open( self.home_path + 'fe_policy_sales_channel.pkl' , 'rb' ) ) 
        self.mms_age                      = pickle.load( open( self.home_path + 'mms_age.pkl' , 'rb') )
        self.mms_vintage                  = pickle.load( open( self.home_path + 'mms_vintage.pkl' , 'rb' ) )
        self.target_encoding_gender       = pickle.load( open( self.home_path + 'target_encoding_gender.pkl' , 'rb' ) )
        self.target_enconding_region_code = pickle.load( open( self.home_path + 'target_enconding_region_code.pkl' , 'rb' ) )
        
    def feature_engineering( self , df2 ):
        # vehicle_age
        df2['vehicle_age'] = df2['vehicle_age'].apply( lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_years' 
                                                                        if x == '1-2 Year' else 'below_1_year')
        # vehicle_damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply( lambda x : 1 if x == 'Yes' else 0 )
        
        return df2
        
    def data_prepatation( self, df5 ):
    
        # annual premium
        df5['annual_premium'] = self.annual_premium_scaler.transform(df5[['annual_premium']].values)

        # age
        df5['age'] = self.mms_age.transform(df5[['age']].values)

        # vintage
        df5['vintage'] = self.mms_vintage.transform(df5[['vintage']].values)

        # gender - One Hot Encoding / Target Encoding
        df5.loc[:,'gender'] = df5['gender'].map( self.target_encoding_gender  )

        # region code - Frequency Encoding / Target Encoding / Weighted Target Encoding
        df5.loc[:,'region_code'] = df5['region_code'].map( self.target_enconding_region_code )

        # vehicle_age
        df5 = pd.get_dummies( data = df5, prefix = 'vehicle_age', columns = ['vehicle_age']  )

        # policy_sales_channel

        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map( self.fe_policy_sales_channel )

        cols_selected = ['vintage',
                 	'annual_premium',
                 	'age',
                 	'region_code',
                	 'vehicle_damage',
                 	'policy_sales_channel',
                 	'previously_insured']

        return df5[ cols_selected ]

    def get_prediction( self, model, original_data, test_data ):
        # prediction
        pred = model.predict_proba( test_data )[:,1]
        
        # join prediction into original data
        original_data['prediction'] = pred
        
        return original_data.to_json( orient = 'records' , date_format = 'iso' )
        