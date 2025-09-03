import pandas as pd
import os
from sqlalchemy import create_engine
import time

import logging

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level = logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


# pip install mysql-connector-python


db_url = "mysql+mysqlconnector://root:password@localhost/commerce"


engine = create_engine(db_url)



# This function will injest the dataframe into database table

def inject_db(df, table_name, engine):
    with engine.connect() as connection:
        try:
           with connection.begin() as transaction:
            print(f"Injecting data into table: {table_name}...")  
            df.to_sql(table_name, 
                      con = connection, 
                      if_exists='replace', 
                      index = False,
                      chunksize=1000 # Good practice for large files
                      )
            print(f"✅ Successfully created/replaced table: {table_name}")
        except Exception as e:
            # The rollback is handled automatically. We just print the original error.
            print(f"❌ Error with table {table_name}. Transaction rolled back.")
            print(f"   Reason: {e}")




# This function will load the CSVs as dataframe and ingest into db

def load_raw_data():
   start = time.time()
   for file in os.listdir('data'):
       if '.csv' in file:
          df = pd.read_csv('data/'+file)
          logging.info(f'Ingesting {file} in db')
          inject_db(df, file[:-4], engine)
   end = time.time()
   total_time = (end - start)/60       
   logging.info('ingestion Complete')
   logging.info(f'Total Time Taken: {total_time} minutes')



   if __name__ == '__main__':
      load_raw_data()