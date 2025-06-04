import pandas as pd

def preprocess_data(file):
    print(" Loading dataset")
    df = pd.read_csv(file)
    print(f"Dataset loaded. Total samples: {len(df)}\n")

    print(" Dataset Info:")
    print(df.info(), "\n")

    print(" Checking for missing values:")
    print(df.isnull().sum(), "\n")

    df.dropna(subset=['URL', 'Label'], inplace=True)

    print("Checking for duplicate rows...")
    dup_count = df.duplicated().sum()
    print(f" Duplicate rows found: {dup_count}")
    df.drop_duplicates(inplace=True)
    print(f"️ Dataset shape after dropping duplicates: {df.shape}\n")



    df.reset_index(drop=True, inplace=True)

    print("Preprocessing complete.")
    return df

