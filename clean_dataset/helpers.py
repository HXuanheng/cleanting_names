import re

def clean_dataset(df,column,wordlist):
    for word in wordlist:
        df = df[~df[column].str.match('(?i)^.*' + word +'.*$')== True]
    return df