import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Load and Clean Data
df = pd.read_csv('mission_launches.csv')

# Convert Date to datetime and extract Year/Month
df['Date'] = pd.to_datetime(df['Date'], utc=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()

# Clean Price Column (Remove commas, convert to numeric)
df['Price'] = df['Price'].str.replace(',', '').astype(float)
df['Price'] = df['Price'].fillna(0)

# 2. Who launched the most missions per year?
launches_per_year = df.groupby(['Year', 'Organisation']).size().reset_index(name='Count')
top_organisations = launches_per_year.sort_values(['Year', 'Count'], ascending=[True, False]).drop_duplicates('Year')

fig_launches = px.bar(top_organisations, x='Year', y='Count', color='Organisation', 
                      title='Organisation with Most Launches per Year')

# 3. Mission Success Rate Over Time
status_per_year = df.groupby(['Year', 'Mission_Status']).size().reset_index(name='Count')
fig_safety = px.line(status_per_year, x='Year', y='Count', color='Mission_Status',
                     title='Space Mission Outcomes Over Time (Success vs Failure)')

# 4. Popularity by Month
month_counts = df['Month'].value_counts().reindex([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
])
fig_months = px.bar(x=month_counts.index, y=month_counts.values, 
                    title='Total Launches by Month', labels={'x': 'Month', 'y': 'Launches'})

# 5. Sunburst Chart: Organisation -> Rocket Status -> Mission Status
fig_sunburst = px.sunburst(df, path=['Organisation', 'Rocket_Status', 'Mission_Status'], 
                           title='Mission Hierarchy: Organisation & Success')

# Show Figures
fig_launches.show()
fig_safety.show()
fig_months.show()
fig_sunburst.show()