import json
import requests
import pandas as pd

#connects to AOE API, creates text file, and loads json file for Structures
strcts_url = "https://age-of-empires-2-api.herokuapp.com/api/v1/structures"
strcts_response = requests.get(strcts_url)
strcts_data = strcts_response.text
strcts_parsed = json.loads(strcts_data)

#loads json file into pandas dataframe for transforming and loading
strcts_df = pd.DataFrame(strcts_parsed['structures'])

strcts_df.head()

#fill missing values from 'line_of_sight' column with 0
strcts_df.line_of_sight.fillna(0, inplace=True)

strcts_df.head()

#save DataFrame into a csv file
Structures = strcts_df.to_csv(r'/home/rhulain/CaseKing_Challenge/Data/Structures.csv')
