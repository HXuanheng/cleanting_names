from clean_dataset.helpers import *


class dataset:
    def __init__(self,df):
        self.df = df

    def droprow_ifwordlist(self,column,wordlist):
        cleaned = clean_dataset(self.df,column,wordlist)
        return cleaned