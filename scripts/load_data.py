from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:123456@localhost:5432/superstore"
)

df = pd.read_csv("data/superstore_clean.csv")

print("Rows in CSV:", len(df))

df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded rows:", len(df))