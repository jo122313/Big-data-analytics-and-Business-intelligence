import pandas as pd

def extract_data(file_path):
    # Load the dataset from CSV file
    df = pd.read_csv(file_path)
    
    # Return the DataFrame
    return df

if __name__ == "__main__":
    # Specify your file path
    file_path = 'Data/Pakistan Largest Ecommerce Dataset.csv'
    df = extract_data(file_path)
    print(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
    # Optionally save a preview of the extracted data
    df.head().to_csv('Data/extracted_data_preview.csv', index=False)
