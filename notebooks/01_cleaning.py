# Paso 0: Cargar las librerias.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Paso 1: Cargar el dataset.
df = pd.read_excel(r'C:\Users\giuli\OneDrive\Documents\ISTEA\Portfolio Giu\data\raw\GoogleAds_DataAnalytics_Sales_organized.xlsx')

# Paso 2: Limpieza de datos
# Convertir columnas a tipos de datos numéricos. 'errors=coerce' asegura que los valores no numéricos se conviertan a NaN.
numeric_cols = ['Clicks', 'Impressions', 'Cost', 'Leads', 'Conversions', 'Sale_Amount']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Rellenar los valores nulos en 'Conversions' con 0.
# Esto lo hacemos porque en el contexto del negocio, un valor nulo en 'Conversions' significa que no hubo ninguna.
df['Conversions'] = df['Conversions'].fillna(0)

""""" Esto era el relleno de 0 en los null, algo que hice antes pero parecería mejor es hacerlo desde pd.to_numeric, 
donde te devuelve ya valores float64 o int64

df['Conversion Rate'] = df['Conversion Rate'].fillna(0)
df['Leads'] = df['Leads'].fillna(0)
df['Clicks'] = df['Clicks'].fillna(0)
df['Impressions'] = df['Impressions'].fillna(0)
df['Sale_Amount'] = df['Sale_Amount'].fillna(0)
df['Cost'] = df['Cost'].fillna(0).astype(float)
"""

# Limpieza de valores de texto


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

""" Viejo, antes lo calculaba pero se volcio redundante con el calculo nuevo de KPIs
df['Conversion Rate'] = df['Conversions'] / df['Clicks']
df['Conversion Rate'] = df['Conversion Rate'].replace([np.inf, -np.inf], 0)

"""

df.drop_duplicates(inplace=True)

# Paso 3: Cálculo de KPIs Clave
# Aquí es donde aplicamos .replace(0, np.nan) a los divisores
# para manejar la división por cero correctamente.

df['CTR'] = (df['Clicks'] / df['Impressions'].replace(0, np.nan)) * 100
df['CPC'] = df['Cost'] / df['Clicks'].replace(0, np.nan)
df['CPA'] = df['Cost'] / df['Conversions'].replace(0, np.nan)
df['ROAS'] = df['Sale_Amount'] / df['Cost'].replace(0, np.nan)


# Agrupa los datos por la columna 'Campaign_Name'
# y calcula el promedio del ROAS para cada campaña.
campaign_kpis = df.groupby('Campaign_Name').agg(
    promedio_CTR = ('CTR', 'mean'),
    promedio_CPC = ('CPC', 'mean'),
    promedio_CPA = ('CPA', 'mean'),
    promedio_ROAS = ('ROAS', 'mean')
).reset_index()

#df.to_excel('GoogleAds_DataAnalytics_Clean.xlsx', index=False)

print("DataFrame después de la limpieza:")
print(df.head())
print(df.info())

# Muestra los resultados
print("\nKPIs promedio por Campaña:")
print(campaign_kpis)

exit()