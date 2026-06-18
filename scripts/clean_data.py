import pandas as pd
import os

def clean_data():
    raw_path = os.path.join('data', 'superstore(in).csv')
    clean_path = os.path.join('data', 'superstore_clean.csv')
    
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw data file not found at {raw_path}")
        
    print(f"Loading raw data from {raw_path}...")
    df = pd.read_csv(raw_path)
    
    # 1. Clean Postal Code
    # Burlington, VT zip code is 05401. 
    # Fill missing postal codes for Burlington, Vermont.
    print("Filling missing postal codes and formatting ZIP codes...")
    burlington_mask = (df['City'] == 'Burlington') & (df['State'] == 'Vermont')
    df.loc[burlington_mask, 'Postal Code'] = 5401.0
    
    # Convert all postal codes to 5-digit strings, padding with leading zeros where necessary.
    df['Postal Code'] = df['Postal Code'].apply(lambda x: f"{int(x):05d}" if pd.notnull(x) else "")
    
    # 2. Format Dates (DD/MM/YYYY to YYYY-MM-DD)
    print("Formatting date fields to YYYY-MM-DD...")
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    
    # 3. Save cleaned data
    print(f"Saving cleaned data to {clean_path}...")
    df.to_csv(clean_path, index=False)
    print("Data cleaning completed successfully.")

if __name__ == '__main__':
    clean_data()
