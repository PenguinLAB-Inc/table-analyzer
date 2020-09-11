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

    def set_ordinal_attributes(self, att):
        
        
