import pandas as pd

def clean_data():
    print("Loading the dataset...")
    raw_df = pd.read_csv('Data/Pakistan Largest Ecommerce Dataset.csv', dtype=str, low_memory=False)

    # --- Fix Column Names ---
    raw_df.columns = raw_df.columns.str.strip()  # Remove spaces around column names

    # --- Handle Missing Values ---
    print("Handling missing values...")
    raw_df['sales_commission_code'] = raw_df['sales_commission_code'].replace('\\N', 'Unknown').fillna('Unknown')
    raw_df['BI Status'] = raw_df['BI Status'].replace('#REF!', 'Unknown').fillna('Unknown')

    # --- Convert Numeric Columns ---
    print("Converting numeric columns...")
    num_cols = ['price', 'grand_total', 'discount_amount', 'qty_ordered']
    for col in num_cols:
        if col in raw_df.columns:
            raw_df[col] = raw_df[col].astype(str).str.replace(',', '').astype(float)
            raw_df[col] = raw_df[col].fillna(raw_df[col].median())  # Use median for missing values

    # --- Convert Integer Columns ---
    int_cols = ['item_id', 'qty_ordered', 'Customer ID', 'increment_id']
    for col in int_cols:
        if col in raw_df.columns:
            raw_df[col] = pd.to_numeric(raw_df[col], errors='coerce').fillna(0).astype(int)

    # --- Handle Date Columns ---
    print("Fixing date columns...")
    date_cols = ['created_at', 'Working Date', 'M-Y']
    for col in date_cols:
        if col in raw_df.columns:
            raw_df[col] = pd.to_datetime(raw_df[col], errors='coerce')

    # --- Remove Unnecessary Columns ---
    print("Removing unnecessary columns...")
    cols_to_drop =  [
        'MV', 'Year', 'Month', 'Customer Since', 
        'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21',
        'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25','sales_commission_code'
    ]
    cols_to_drop = [col for col in cols_to_drop if col in raw_df.columns]
    raw_df = raw_df.drop(columns=cols_to_drop)

    # --- Remove Duplicates ---
    print("Removing duplicates...")
    raw_df = raw_df.drop_duplicates()

    # --- Strip Spaces from String Values ---
    raw_df = raw_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # --- Save Cleaned Data ---
    print("Saving cleaned data to 'cleaned.csv'...")
    raw_df.to_csv('Data/cleaned.csv', index=False)
    print("Data cleaning completed successfully!")

if __name__ == "__main__":
    clean_data()
