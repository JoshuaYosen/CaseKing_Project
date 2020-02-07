import requests
import bonobo
import json
import pandas as pd


#create Extract Transform Load class called ETL
class ETL:

    #initiate 2 variables, name of data and url to access data
    def __init__(self, name, url):
        self.name = name
        self.url = url

    #function to connect to API and retrieve data
    def aoe_connect(self):
        r = requests.get(self.url)
        data = r.text
        data_parsed = json.loads(data)
        return data_parsed


    #function to extract data
    def extract(self):
        yield aoe_connect(self.url)


    #function to transform data based on data engineering exploration as a pandas DataFrame
    def transform(self, data_parsed):
        if self.name == 'Units':
            df = pd.DataFrame(data_parsed['units'])
            df['description'] = df['description'].astype('str')
            df['description'] = df['description'].str.split()
            upgraded = df[units_df['description'].apply(lambda x: 'Upgraded' in x)]
            df['Upgraded'] = upgraded.description


        elif self.name == 'Structures':
            df = pd.DataFrame(data_parsed['structures'])
            df.line_of_sight.fillna(0, inplace=True)

        return df

    #function to load data into sqlite3 database
    def load(self, df):
        conn = lite.connect('db_file.db')
        df.to_sql("{}".format(self.name), conn, if_exists='replace')



#execute our instances of ETL class through bonobo
if __name__ == '__main__':
    #defines API urls
    units_url = "https://age-of-empires-2-api.herokuapp.com/api/v1/units"
    strcts_url = "https://age-of-empires-2-api.herokuapp.com/api/v1/structures"

    #creates instances of ETL class
    units_etl = ETL('Units', units_url)
    strcts_etl = ETL('Structures', strcts_url)

    #defines bonobo graphs for Extact Tnransorm Load processes
    graph1 = bonobo.Graph(
        units_etl.extract,
        units_etl.transform,
        units_etl.load,
    )
    graph2 = bonobo.Graph(
    strcts_etl.extract,
    strcts_etl.transform,
    strcts_etl.load,
    )

    #run graphs
    bonobo.run(graph1)
    bonobo.run(graph2)
