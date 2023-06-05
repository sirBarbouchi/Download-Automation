import pandas as pd
import glob
from pathlib import Path
from datetime import datetime
import numpy as np
def transformation():
    dfs = []
    #read all csv files in the directory and put them in a list
    today = str(datetime.today().strftime('%Y%m%d'))

    for filepath in glob.iglob(r"./"+ today +" Downloaded_files/TAXRATES_ZIP5/*.csv"):
        dfs.append(pd.read_csv(filepath, encoding='cp1252'))
    #contatenate all dataframes
    df = pd.concat(dfs).reset_index(drop = True)
    #select the right columns
    tax_rates = df[['State', 'ZipCode', 'EstimatedCombinedRate']]
    #add country column
    tax_rates['Country'] = 'US'

    class Latent:
        def __init__(self):
            self.state = ''
            self.number = 0
    #code process: apply this format: 'US-x['state']{i} with i is the ith row for each state
    def code_process(x, latent):
        if x == latent.state:
            latent.number += 1
        else:
            latent.state = x
            latent.number =1
        return 'US-' + x + '-Rate' + str(latent.number)
    #rate process by multiplying the EstimatedCombinedRate column by 100
    def process_rate(x):
        try:
            return x*100
        except:
            return 0.0

    latent = Latent()
    tax_rates['Code'] = tax_rates.State.apply(lambda x: code_process(x, latent))
    tax_rates['EstimatedCombinedRate'] = tax_rates.EstimatedCombinedRate.apply(process_rate)
    #rename some columns
    tax_rates.rename(columns={'EstimatedCombinedRate': 'Rate', 'ZipCode': 'Zip/Post Code'}, inplace=True)
    #adda row on the top
    new_row = pd.DataFrame({'Code': 'No-Tax', 'Country': 'US', 'State': '*', 'Zip/Post Code': '*', 'Rate': 0}, index =[0])
    tax_rates = pd.concat([new_row, tax_rates]).reset_index(drop = True)
    #convert the type of zipcode column to string
    tax_rates['Zip/Post Code'] = tax_rates['Zip/Post Code'].astype('str')
    #save the dataframe to csv file
    Path("./"+today+" output").mkdir(parents=True, exist_ok=True)
    #tax_rates.to_csv("./"+today+" output/tax_rates.csv", index=False)
    groups = tax_rates.groupby(np.arange(len(tax_rates.index))//2000)
    for (frameno, frame) in groups:
        if int(frameno) + 1 < 10:
            frame.to_csv("./"+today+" output/tax_rates.0%s.csv" % str(int(frameno)+1), index=False)
        else:
            frame.to_csv("./"+today+" output/tax_rates.%s.csv" % str(int(frameno)+1), index=False)