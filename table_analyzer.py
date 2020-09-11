import pandas as pd
import scipy.stats as ss
import seaborn as sns
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

class TableAnalyzer:
    def __init__(self, data_path, encoding='euc-kr'):
        self.data_path = data_path

        
        self.data = self._make_data(data_path, encoding)
    
    def _make_data(self, path, encoding):
        file_ext = path.split('.')[-1]
        if file_ext == 'csv':
            return pd.read_csv(path, engine='python', encoding='euc-kr')
        elif:
            return pd.read_excel(path)
        else:
            """ TO DO: make available when other extension """

            return None

    def get_pearson_matrix(self, ordinal_atts):
        """
        * Get Pearson matrix
        Args
            nominal_atts : ordinal attributes 

        Return
            Pearson matrix
        """
        self.data = self.data[[i for i in data.columns if i not in ordinal_atts]]
        return data.corr()

    def get_cramer_v(self, nominal_atts):
        """
        * Get Cramer V matrix
        * Reference : https://www.kaggle.com/chrisbss1/cramer-s-v-correlation-matrix
        Args
            nominal_atts : nominal attributes 

        Return
            Cramer matrix
        """
            
        self.data = self.data[[i for i in data.columns if i not in nominal_atts]]
        dummy = pd.get_dummies(self.data)
        rows = []
        for var1 in dummy:
            cols = []
            for var2 in dummy:
                cramers = cramers_V(dummy[var1], dummy[var2])
                cols.append(round(cramers,2))
            rows.append(cols)

        cramers_results = np.array(rows)
        cdf = pd.DataFrame(cramers_results, columns=dummy.columns, index=dummy.columns)
        return cdf
        
        
