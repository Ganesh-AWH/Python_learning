import pandas as pd
import plotly.express as px

# Load Datasets
df_shootings = pd.read_csv('fatal_shootings.csv')
df_poverty = pd.read_csv('poverty_rate.csv')
df_income = pd.read_csv('median_income.csv')
df_race = pd.read_csv('racial_demographics.csv')

# 1. Data Cleaning: Convert percentage strings to floats
df_poverty['poverty_rate'] = pd.to_numeric(df_poverty['poverty_rate'], errors='coerce')

# 2. Aggregating Shootings by Race
race_counts = df_shootings['race'].value_counts().reset_index()
race_counts.columns = ['Race', 'Fatal_Shootings']

# 3. Merging Poverty and Shootings by State
state_poverty = df_poverty.groupby('Geographic Area')['poverty_rate'].mean().reset_index()
state_shootings = df_shootings['state'].value_counts().reset_index()
state_shootings.columns = ['Geographic Area', 'Shootings']

merged_df = pd.merge(state_poverty, state_shootings, on='Geographic Area')

# 4. Visualizing Correlation
fig = px.scatter(merged_df, x='poverty_rate', y='Shootings', text='Geographic Area',
                 title='State Poverty Rate vs. Fatal Police Shootings',
                 trendline="ols")
fig.show()