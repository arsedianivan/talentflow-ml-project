import pandas as pd
import numpy as np
import os

# Check if we're in the right directory and the data file exists
if not os.path.exists('data/WA_Fn-UseC_-HR-Employee-Attrition.csv'):
    print("ERROR: Cannot find the data file!")
    print("Please make sure:")
    print("1. You're in the talentflow-ml-project directory")
    print("2. The CSV file is in the 'data' subdirectory")
    print("3. The file is named exactly: WA_Fn-UseC_-HR-Employee-Attrition.csv")
    exit(1)

# Load the dataset
print("Loading IBM HR dataset...")
df = pd.read_csv('data/WA_Fn-UseC_-HR-Employee-Attrition.csv')
print(f"Loaded {len(df)} records")

# Transform HR data to represent B2B HRTech customers
# We'll interpret each "employee" record as a customer company
print("\nTransforming data to HRTech customer context...")

# Create HRTech-relevant features from existing data
hrtech_df = pd.DataFrame()

# Map employee attributes to customer company attributes
hrtech_df['customer_id'] = ['CUST' + str(i).zfill(4) for i in range(1, len(df) + 1)]

# Company size based on department diversity and job level
hrtech_df['employee_count'] = df['TotalWorkingYears'] * np.random.randint(10, 50, size=len(df))
hrtech_df['company_size'] = pd.cut(hrtech_df['employee_count'], 
                                   bins=[0, 50, 200, 1000, 5000], 
                                   labels=['startup', 'small', 'medium', 'enterprise'])

# Tenure as customer (in months)
hrtech_df['tenure_months'] = df['YearsAtCompany'] * 12

# Contract value based on company size
hrtech_df['contract_value_annual'] = hrtech_df['employee_count'] * np.random.uniform(8, 15, size=len(df)) * 12

# Product usage metrics
hrtech_df['modules_subscribed'] = df['NumCompaniesWorked'].clip(1, 6)  # Number of HR modules
hrtech_df['has_payroll_module'] = (df['Department'] == 'Human Resources').astype(int)

# Engagement metrics (derived from satisfaction and performance)
hrtech_df['active_users_ratio'] = df['JobSatisfaction'] / 4 * np.random.uniform(0.7, 1.0, size=len(df))
hrtech_df['monthly_active_users'] = (hrtech_df['employee_count'] * hrtech_df['active_users_ratio']).astype(int)

# Support and health metrics
hrtech_df['support_tickets_per_month'] = (5 - df['RelationshipSatisfaction']) * np.random.uniform(0.5, 2, size=len(df))
hrtech_df['health_score'] = (df['JobSatisfaction'] + df['EnvironmentSatisfaction']) / 8 * 100

# Training and adoption
hrtech_df['training_sessions_attended'] = df['TrainingTimesLastYear']
hrtech_df['onboarding_completed'] = (df['YearsAtCompany'] > 0.5).astype(int)

# Feature usage
hrtech_df['features_used_ratio'] = df['PerformanceRating'] / 4
hrtech_df['avg_logins_per_user_month'] = hrtech_df['active_users_ratio'] * 25 * np.random.uniform(0.5, 1, size=len(df))

# Business metrics
hrtech_df['last_qbr_attendance'] = (df['WorkLifeBalance'] >= 3).astype(int)
hrtech_df['payment_delays_last_year'] = (5 - df['JobInvolvement']).clip(0, 4)
hrtech_df['critical_issues_last_quarter'] = np.random.poisson(0.5, size=len(df)).clip(0, 3)

# Industry mapping
dept_to_industry = {
    'Sales': 'Retail',
    'Research & Development': 'Technology',
    'Human Resources': 'Services',
    'Manufacturing': 'Manufacturing',
    'Marketing': 'Media',
    'Other': 'Other'
}
hrtech_df['industry'] = df['Department'].map(lambda x: dept_to_industry.get(x, 'Other'))

# Churn outcome (1 = churned, 0 = retained)
hrtech_df['churned'] = (df['Attrition'] == 'Yes').astype(int)

# Round numerical columns
numerical_cols = ['contract_value_annual', 'active_users_ratio', 'avg_logins_per_user_month', 
                 'features_used_ratio', 'support_tickets_per_month', 'health_score']
for col in numerical_cols:
    hrtech_df[col] = hrtech_df[col].round(2)

# Save the transformed dataset
output_file = 'talentflow_customer_data.csv'
hrtech_df.to_csv(output_file, index=False)

# Display summary
print(f"\n✅ Dataset transformed successfully!")
print(f"Output file: {output_file}")
print(f"Total customers: {len(hrtech_df)}")
print(f"Overall churn rate: {hrtech_df['churned'].mean():.2%}")
print(f"\nChurn rate by company size:")
print(hrtech_df.groupby('company_size')['churned'].agg(['mean', 'count']))
print(f"\nFirst 5 rows:")
print(hrtech_df.head())

# Verify the file was created
if os.path.exists(output_file):
    print(f"\n✅ Success! Your transformed data is ready in: {output_file}")
    print(f"File size: {os.path.getsize(output_file) / 1024:.1f} KB")