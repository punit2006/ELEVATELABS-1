# ELEVATELABS-1

# Marketing Campaign Data Cleaning

This project focuses on cleaning and preprocessing the **Marketing Campaign** dataset using **Python (Pandas)**. It is designed to prepare raw, messy data for further analysis or modeling by handling common data quality issues such as missing values, duplicates, inconsistent formats, and incorrect data types.

# Dataset
The dataset used is `marketing_campaign.csv`, a tab-separated file containing customer and campaign information. It is commonly found on platforms like Kaggle.

# Tools & Libraries
Python
Pandas
  
# Cleaning Steps Performed
1. **Load the Dataset**  
   Handled tab-separated format

2. **Initial Data Inspection**  
   Checked for shape, missing values, and duplicates

3. **Remove Duplicates**  
   Dropped exact duplicate rows

4. **Handle Missing Values**  
   Dropped columns with more than 50% missing values  
   Filled numeric columns with median  
   Filled categorical columns with mode

5. **Standardize Text Data**  
   Converted text to lowercase and stripped whitespace

6. **Convert Date Columns**  
   Automatically converted columns containing "date" to `datetime` objects

7. **Clean Column Names**  
   Lowercased, trimmed, and replaced spaces with underscores

8. **Fix Data Types**  
   Converted `income` to float and `age` to integer (if present)

9. **Export Cleaned Dataset**  
   Saved as `cleaned_marketing_campaign.csv`

# Output
`cleaned_marketing_campaign.csv`: A ready-to-use cleaned dataset

# Next Steps
We can now use this cleaned dataset for:
- Exploratory Data Analysis (EDA)
- Visualization
- Machine Learning Models
- Business Intelligence tools like Power BI or Tableau
