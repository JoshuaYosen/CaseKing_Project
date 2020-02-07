import json
import requests
import pandas as pd

##connects to AOE API, creates text file, and loads json file for Units
units_url = "https://age-of-empires-2-api.herokuapp.com/api/v1/units"
units_response = requests.get(units_url)
units_data = units_response.text
units_parsed = json.loads(units_data)

#load json file into DataFrame
units_df = pd.DataFrame(units_parsed['units'])

#assigns objects in description column as string and splits string
units_df['description'] = units_df['description'].astype('str')
units_df['description'] = units_df['description'].str.split()

#takes each element of description, and assigns them into a set of arrays
upgraded = units_df[units_df['description'].apply(lambda x: 'Upgraded' in x)]

#creates new column in Units DataFrame with description column from upgraded DataFrame
units_df['Upgraded'] = upgraded.description

#saves Units DataFrame to a csv file
Units = units_df.to_csv(r'/home/rhulain/CaseKing_Challenge/Data/Units.csv')
