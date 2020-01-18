import psycopg2
import pandas as pd

#loads Structures csv into Pandas DataFrame
strcts_df = pd.read_csv(r'/home/rhulain/CaseKing_Challenge/Data/Structures.csv', index_col=0)

#loads Units csv into Pandas DataFrame
units_df = pd.read_csv(r'/home/rhulain/CaseKing_Challenge/Data/Units.csv', index_col=0)

#generates sql engine
#engine = sqlalchemy.create_engine("postgresql://postgres:Esef2BxPQm6Zdl4oa3le@localhost/bi_challenge", pool_pre_ping=True)

conn = psycopg2.connect(host="caseking-developer-challenge-jyosen.cnnurent09we.eu-central-1.rds.amazonaws.com", dbname="bi_challenge", user="postgres", password="Esef2BxPQm6Zdl4oa3le")
#creates connection variable to the sql engine
#con = engine.connect()

#creates table Structures and assigns Structures DataFrame to table and schema
table1_name = 'Structures'
strcts_df.to_sql(table1_name, con, schema='aoe')

#creates table Units and assigns Units DataFrame to table and schema
table2_name = 'Units'
units_df.to_sql(table2_name, con, schema='aoe')


con.close()
