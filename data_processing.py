import pandas as pd
import numpy as np

folder = r'C:\Users\luis_\Documents\Workspace\iphone_index_dash\data\\'
file = 'iphone_index_data.xlsx'

iphone_data = pd.read_excel(folder+file, sheet_name='iphone_13')

avg_wage_data = pd.read_csv(folder+'countries average wage OECD.csv')
min_wage_data = pd.read_csv(folder+'countries minimum wage OECD.csv')

exchange_data = pd.read_csv(folder+'exchange_rates.csv')

countries_dict = {'US': 'United States',
                  'MX':'Mexico',
                  'AE':'United Arab Emirates',
                  'AU':'Australia',
                  'JP':'Japan',
                  'DE':'Germany',
                  'CA':'Canada',
                  'IN':'India',
                  'HK':'Hong Kong'}

def filter_max_year(data):
    max_year = data['year'].max()
    filtered_data = data[data['year'] == max_year]
    return filtered_data
    
def filter_iso_nulls(data):
    filtered_data = data.dropna(subset=['iso_2'])
    return filtered_data

avg_wage_data = avg_wage_data.pipe(filter_max_year).pipe(filter_iso_nulls).reset_index(drop=True)

min_wage_data = min_wage_data.pipe(filter_max_year).pipe(filter_iso_nulls).reset_index(drop=True)

### Complete country name from dict
iphone_data['country_name'] = iphone_data['country'].replace(countries_dict)

### Convert price local to usd
iphone_data = iphone_data.merge(exchange_data[['country','to-usd']], on=['country'])
iphone_data['price_usd'] = round(iphone_data['price_local'] / iphone_data['to-usd'], 2)

### Add average and minimum wage
iphone_data = iphone_data.merge(min_wage_data[['iso_2','minimum_wage_usd']], left_on=['country'], right_on=['iso_2'])
iphone_data = iphone_data.merge(avg_wage_data[['iso_2','avg_wage_usd']], left_on=['country'], right_on=['iso_2'])

### Calculate how many days are taken to buy an iphone (minimum wage)
iphone_data['days_to_buy_min_wage'] = round(iphone_data['price_usd'] / (iphone_data['minimum_wage_usd'] / 365), 0)
iphone_data['days_to_buy_min_wage'] = iphone_data['days_to_buy_min_wage'].astype(int)

### Calculate how many days are taken to buy an iphone (average wage)
iphone_data['days_to_buy_avg_wage'] = round(iphone_data['price_usd'] / (iphone_data['avg_wage_usd'] / 365), 0)
iphone_data['days_to_buy_avg_wage'] = iphone_data['days_to_buy_avg_wage'].astype(int)



