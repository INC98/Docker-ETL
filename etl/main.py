import time
import pandas as pd
from sqlalchemy import create_engine

time.sleep(15)

df = pd.read_csv("/data/spotify_songs.csv")

engine = create_engine(
    "postgresql+psycopg2://admin:admin@postgres:5432/company"
)

df.to_sql(
    "songs",
    engine,
    if_exists="replace",
    index=False
)

print("Datos cargados correctamente")