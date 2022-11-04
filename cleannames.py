from clean_company.clean_name import company
from helpers import *
from data import *
import sys


file = 'fec_sample11-14.dta'                                   #file name

def main():
    df = import_dta(resources + file)                          #import .dta file from the folder "resources"
    df = clean_companyname_dta(df, column='employer')          #clean the company name in the column "employer"
    df = clean_personname_dta(df, column='name')               #clean the person name in the column "name"
    write_dta(df, results + file[:-4] + '_cleaned.dta')        #output the result in .dta file located in the folder "results"
    print(f'Operation on {file} completed')

if __name__ == "__main__":
    main()

