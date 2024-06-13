import category_encoders as ce
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load .env file
load_dotenv()

# Get the dataframe from the excel file
file_path = os.getenv('DATA_PATH')
df = pd.read_excel(file_path, sheet_name='query_result')
df_copy = df.copy()

# Display information about the dataframe
print(df.info())

# Display random sample rows
random_rows = df.sample(n=8)
print(random_rows)

# Calculate null value counts and percentages
null_counts = df.isnull().sum()
null_percentages = (null_counts / len(df)) * 100

# Create a combined table for null values
null_info = pd.DataFrame({
    'Null Count': null_counts,
    'Null Percentage': null_percentages
})
print(null_info)

# Fill missing values in 'education_status' with the mode
df['education_status'] = df['education_status'].fillna(df['education_status'].mode()[0])

# Fill missing values in 'experience_month' with the median
df['experience_month'] = df['experience_month'].fillna(df['experience_month'].median())

# Fill missing values in 'age' with the mean
df['age'] = df['age'].fillna(df['age'].mean())

# Fill missing values in 'gender' with the mode
df['gender'] = df['gender'].fillna(df['gender'].mode()[0])

# Fill missing values in 'work_time_preference' with the mode
df['work_time_preference'] = df['work_time_preference'].fillna(df['work_time_preference'].mode()[0])

# Check for remaining missing values
null_counts_after = df.isnull().sum()
print(null_counts_after)

# Convert float columns to int if possible
def convert_float_to_int(df):
    for col in df.columns:
        if df[col].dtype == 'float64':
            if (df[col] % 1 == 0).all():
                df[col] = df[col].astype('int64')
    return df

df = convert_float_to_int(df)
print(df.info())

# Replace 'na' values with NaN
df = df.replace(to_replace='na', value=np.nan)

# Convert columns with 'na' values to numeric
columns_with_na = df.columns[df.isin(['na']).any()]
for column in columns_with_na:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Drop rows with NaN values
df = df.dropna()
null_counts_after = df.isnull().sum()
print(null_counts_after)

# Select categorical and numeric columns
categorical_cols = df.select_dtypes(include=['object']).columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Label Encoding for work_time_preference and ordinal encoding for education_status
label_encoder = LabelEncoder()
encoder= ce.OrdinalEncoder(cols=['education_status'],return_df=True,
                           mapping=[{'col':'education_status','mapping':{'elementary_school':1,'middle_school':2,'high_school':3,'university':4}}])

df["education_status"] = encoder.fit_transform(df["education_status"])

df['work_time_preference'] = label_encoder.fit_transform(df['work_time_preference'].astype(str))

# Binary encoding for appointment_status and gender
df['appointment_status'] = df['appointment_status'].apply(lambda x: 1 if x == 'worker_came' else 0)
df['gender'] = df['gender'].map({'male': 0, 'female': 1})

# Create correlation matrices
correlation_matrix = df.corr()
relevant_columns = ['appointment_status', 'appointment_delay', 'appointment_came_count', 'experience_month', 'age']
subset_df = df[relevant_columns]
correlation_matrix_subset = subset_df.corr()
relevant_columns_each = ['application_count', 'seen_application_count', 'applicationSL_count', 'message_count']
subset_df_each = df[relevant_columns_each]
correlation_matrix_subset_each = subset_df_each.corr()

# Visualize the correlation matrices in subplots
plt.figure(figsize=(20, 15))

plt.subplot(3, 1, 1)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')

plt.subplot(3, 1, 2)
sns.heatmap(correlation_matrix_subset, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Relevant Features with Target')

plt.subplot(3, 1, 3)
sns.heatmap(correlation_matrix_subset_each, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Application-Related Features')

plt.tight_layout()
plt.show()

# Detect and remove outliers for appointment_delay using IQR method
Q1 = df['appointment_delay'].quantile(0.15)
Q3 = df['appointment_delay'].quantile(0.85)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df_no_outliers = df[(df['appointment_delay'] >= lower_bound) & (df['appointment_delay'] <= upper_bound)]

# Visualize data without outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_no_outliers, y='appointment_delay', x='appointment_status')
plt.title('Box Plot of Appointment Delay (Without Outliers)')
plt.ylabel('Appointment Delay')
plt.xlabel('Appointment Status')
plt.show()

# Detect and remove outliers for distance_to_company using IQR method
Q1 = df['distance_to_company'].quantile(0.15)
Q3 = df['distance_to_company'].quantile(0.85)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df_dtc_no_outliers = df[(df['distance_to_company'] >= lower_bound) & (df['distance_to_company'] <= upper_bound)]

# Visualize data without outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_dtc_no_outliers, y='distance_to_company', x='appointment_status')
plt.title('Box Plot of Distance to Company (Without Outliers)')
plt.ylabel('Distance to Company')
plt.xlabel('Appointment Status')
plt.show()

# Scatter plot to analyze relationship between appointment_status and distance_to_company
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_dtc_no_outliers, x='appointment_status', y='distance_to_company')
plt.title('Appointment Status vs. Distance to Company')
plt.xlabel('Appointment Status')
plt.ylabel('Distance to Company')
plt.show()
