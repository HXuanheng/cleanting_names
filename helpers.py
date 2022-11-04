import pandas as pd
from clean_company.clean_name import company
from clean_person.clean_person import person
from clean_dataset.clean_dataset import dataset
from data import *
from wordlist import *
from tqdm import tqdm


def import_dta(file):
    df = pd.read_stata(file)
    return df

def write_dta(df, file):
    df.to_stata(file, write_index=False, version=118)

def clean_companyname_dta(df, column):
    tqdm.pandas()
    df = dataset(df).droprow_ifwordlist(column,wordlist)
    print(f'Rows dropped')
    print(f'Start cleaning company names in column {column}...')
    df[column + '_cleaned'] = df[column].progress_apply(lambda x: company(x).clean())
    print(f'Operation on column {column} completed')
    return df

def clean_name(word):
    #cleaned = person(word).name() + " " + person(word).mid() +  " " + person(word).last() + " " + person(word).suffix()
    cleaned = person(word).name() +  " " + person(word).last() + " " + person(word).suffix()
    cleaned =  " ".join(cleaned.split())
    return cleaned

def clean_personname_dta(df, column):
    tqdm.pandas()
    print(f'Start cleaning people names in column {column}...')
    df[column + '_cleaned'] = df[column].progress_apply(lambda x: clean_name(x))
    print(f'Operation on column {column} completed')
    return df