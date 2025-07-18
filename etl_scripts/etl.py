import pandas as pd
from sqlalchemy import create_engine

def extract_data():
    df = pd.read_csv("../data/sales_data.csv")
    print(" Extracted Data:\n", df)
    return df

def transform_data(df):
    df['total_revenue'] = df['selling_price'] * (1 - df['discount']) * df['units_sold']
    print("Transformed Data:\n", df)
    return df

def load_data(df):
    # Replace root & password with your MySQL credentials
    engine = create_engine("mysql+pymysql://root:admin@localhost/retail_sales")
    df.to_sql("sales_fact", engine, if_exists="append", index=False)
    print(" Data successfully loaded into MySQL!")

if __name__ == "__main__":
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)
