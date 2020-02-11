from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('mysql://root@localhost/')


df = pd.read_sql('SELECT * FROM simplon', engine)



print(df)
