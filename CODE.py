import pandas as pd

df = pd.read_csv("C:/Users/punit/OneDrive/Documents/marketing_campaign.csv", sep='\t')
print("Initial shape:", df.shape)
print("Missing values before cleaning:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Step 1: Drop duplicate rows
df = df.drop_duplicates()

# Step 2: Handle missing values
# Drop columns with more than 50% missing values
threshold = len(df) * 0.5
df = df.dropna(thresh=threshold, axis=1)

# Fill numeric columns with median
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

# Step 3: Standardize text values
df[categorical_cols] = df[categorical_cols].apply(lambda col: col.str.lower().str.strip())

# Step 4: Convert date columns to datetime
date_cols = df.columns[df.columns.str.contains("date", case=False)]
df[date_cols] = df[date_cols].apply(pd.to_datetime, errors='coerce', dayfirst=True)

# Step 5: Rename columns 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 6: Fix data types
if 'income' in df.columns:
    df['income'] = pd.to_numeric(df['income'], errors='coerce')
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)

# Save cleaned data
df.to_csv("cleaned_marketing_campaign.csv", index=False)
print("\nCleaning complete!")
print("Final shape:", df.shape)
print("Remaining missing values:\n", df.isnull().sum())
