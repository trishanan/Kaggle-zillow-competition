import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle

class Data:
    def __init__(self,train_file, properties_2016_file, test_file, properties_2017_file , cat_cols, num_cols, date_col, target_col, id_col):
        self.cat_cols = list(cat_cols)
        self.num_cols = list(num_cols)
        self.feature_cols = cat_cols + num_cols
        self.target_col = target_col
        self.id_col = id_col
        self.label_encoders = {}
        self.date_col = date_col
        self.target_col = target_col
        self.train_df = self._create_train_df(train_file, properties_2016_file)
        self.test_df = self._create_test_df(test_file, properties_2017_file)
        
        
    ## Function to create a train dataframe that will load the data, clean and preprocess the data    
    def _create_train_df(self,train_file, properties_2016_file,preprocess = True, label_encode = False,create_dummies = True,modify_dates = True):
        train_features = self._load_data(train_file)
        train_properties = self._load_data(properties_2016_file)
        train_df = self._join_data(train_features,train_properties)
        if preprocess:
            train_df = self._preprocess_data(train_df)
            ##train_df = self._shuffle_data(train_df)
        if label_encode:
            self.label_encode_df(train_df, self.cat_cols)
        if create_dummies:
            dummied_df = self._create_dummies (train_df, self.cat_cols)
        if modify_dates:
            dates_modify_df = self._modify_datecol(dummied_df, self.date_col)
        return dates_modify_df
    
    
    ## Function to create a test dataframe that will load the data, clean and preprocess the data
    def _create_test_df(self,test_file, properties_2017_file, preprocess = True, label_encode = False,create_dummies = True,modify_dates = True):
        test_features = self._load_data(test_file)
        test_properties = self._load_data(properties_2017_file)
        test_df = self._join_data(test_features,test_properties)
        if preprocess:
            test_df = self._preprocess_data(test_df)
        if label_encode:
            self.label_encode_df(test_df, self.cat_cols)
        if create_dummies:
            dummied_df = self._create_dummies(test_df,self.cat_cols)
        if modify_dates:
            new_df = self._modify_datecol(dummied_df, self.date_col)
        return new_df
        
    ## Function to load data usin.l,g pandas    
    def _load_data(self,file):
        return pd.read_csv(file)
    
    
    ## Function to join datasets using pd.merge
    def _join_data (self, df1, df2):
        df = pd.merge(df1, df2,how = 'left',on = 'parcelid')
        return df
    
    
    ## Function to preprocess data by dropping duplicates and removing zero salaries entries
    def _preprocess_data(self, df):
        cleaned_train_df = df.drop_duplicates(subset='parcelid')
        cleaned_train_df = cleaned_train_df.drop(['rawcensustractandblock', 'censustractandblock', 'propertyzoningdesc', 
                                 'regionidneighborhood', 'regionidzip','parcelid'], axis=1)
        ##cleaned_train_df = cleaned_train_df[cleaned_train_df.salary > 0]
        return cleaned_train_df
    
    
    ## Shuffle the dataframe
    def _shuffle_data(self, df):
        return shuffle(df).reset_index()
    
    
    ## Function created for label encoding the variables
    def label_encode_df(self, df, cols):
        '''creates one label encoder for each column in the data object instance'''
        for col in cols:
            if col in self.label_encoders:
                #if label encoder already exits for col, use it
                self._label_encode(df, col, self.label_encoders[col])
            else:
                self._label_encode(df, col)
                
    
    ## Function created for label encoding the variables
    def _label_encode(self, df, col, le=None):
        '''label encodes data'''
        if le:
            df[col] = le.transform(df[col])
        else:
            le = LabelEncoder()
            le.fit(df[col])
            df[col] = le.transform(df[col])
            self.label_encoders[col] = le
            
    def _create_dummies(self,df,cols):
        dummies = pd.get_dummies(df,columns = cols, dummy_na = True)
        dummies = dummies.fillna(-1)
        return dummies
    
    def _modify_datecol(self,df, date_col):
        for x in date_col:
                df[x + '_month'] = pd.to_datetime(df[x]).apply(lambda x: x.month)
                df = df.drop(x, axis=1)
        return df
    
  
    
    
    