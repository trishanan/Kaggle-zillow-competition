import pandas as pd
import numpy as np

class get_data_intersection:
    def __init__(self,data):
        self.data = data
        
    def filter_cols(self):
        common_cols = self.intersection_cols(self.data.train_df,self.data.test_df)
        self.data.train_df = self.data.train_df.loc[:,common_cols]
        self.data.train_df = self.data.train_df.sample(n = 20000,replace = True, random_state = 2)
        self.data.test_df = self.data.test_df.loc[:,common_cols]
        self.data.test_df = self.data.train_df.sample(n = 20000,replace = True, random_state = 2)
        common_cols.remove('logerror')
        self.data.feature_cols = common_cols
              
    def intersection_cols(self,df1,df2):    
        cols = list(set(df1.columns).intersection(set(df2.columns)))
        return cols