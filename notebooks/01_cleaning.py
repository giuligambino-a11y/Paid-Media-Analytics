import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_excel(r'C:\Users\giuli\OneDrive\Documents\ISTEA\Portfolio Giu\data\raw\GoogleAds_DataAnalytics_Sales_organized.xlsx')

numeric_cols = ['Clicks', 'Impressions', 'Cost', 'Leads', 'Conversions', 'Sale_Amount']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


df['Conversions'] = df['Conversions'].fillna(0)

df['Campaign_Name'] = df['Campaign_Name'].str.lower().str.replace('data analytics corse', 'data analytics course')
df['Campaign_Name'] = df['Campaign_Name'].str.replace('data analytcis course', 'data analytics course')
df['Campaign_Name'] = df['Campaign_Name'].str.replace('data anlytics corse', 'data analytics course')
df['Campaign_Name'] = df['Campaign_Name'].str.replace('dataanalyticscourse', 'data analytics course')


df['Location'] = df['Location'].str.lower().str.replace('hyderbad', 'hyderabad')
df['Location'] = df['Location'].str.replace('hydrebad', 'hyderabad')


df['Ad_Date'] = pd.to_datetime(df['Ad_Date'], format='%d-%m-%Y')

df['Device'] = df['Device'].str.lower()

df['Keyword'] = df['Keyword'].str.replace('data analitics course', 'data analytics course') 
df['Keyword'] = df['Keyword'].str.replace('data anaytics training', 'data analytics training') 
df['Keyword'] = df['Keyword'].str.replace('online data analytic', 'data analytics online')  
df['Keyword'] = df['Keyword'].str.replace('data analitics online', 'data analytics online')

df.drop_duplicates(inplace=True)


df['CTR'] = (df['Clicks'] / df['Impressions'].replace(0, np.nan)) * 100
df['CPC'] = df['Cost'] / df['Clicks'].replace(0, np.nan)
df['CPA'] = df['Cost'] / df['Conversions'].replace(0, np.nan)
df['ROAS'] = df['Sale_Amount'] / df['Cost'].replace(0, np.nan)


campaign_kpis = df.groupby('Campaign_Name').agg(
    promedio_CTR = ('CTR', 'mean'),
    promedio_CPC = ('CPC', 'mean'),
    promedio_CPA = ('CPA', 'mean'),
    promedio_ROAS = ('ROAS', 'mean')
).reset_index()

df.to_excel('GoogleAds_DataAnalytics_Clean.xlsx', index=False)

print("DataFrame después de la limpieza:")
print(df.head())
print(df.info())

print("\nKPIs promedio por Campaña:")
print(campaign_kpis)


exit()
