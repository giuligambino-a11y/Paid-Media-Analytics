# Paid-Media-Analytics
En este proyecto analizo el impacto y los resultados de una campaña de Paid Media (Google Ads). El objetivo principal es evaluar la rentabilidad y eficacia de la campaña mediante KPIs clave, y presentar la información en un dashboard claro e interactivo. Finalmente, en base a los resultados obtenidos, se plantean conclusiones y recomendaciones para optimizar la estrategia publicitaria.

---

## Objetivo del Proyecto

Analizar campañas de marketing digital para:
- Medir eficiencia publicitaria mediante KPIs clave.
- Identificar qué campañas funcionan mejor.
- Generar insights accionables para optimizar la inversión.

---

## Tecnologías Utilizadas

- **Python** 🐍 → Limpieza de datos y cálculo de KPIs.
- **SQL** 🗄️ → Consultas avanzadas para segmentación y métricas de negocio.  
- **Power BI** 📈 → Creación de un dashboard interactivo con storytelling visual.  

---

# KPIs

- **CTR (Click Through Rate)** = Clicks / Impressions  
- **CPC (Cost per Click)** = Cost / Clicks  
- **CPA (Cost per Acquisition)** = Cost / Conversions  
- **ROAS (Return on Ad Spend)** = Revenue / Cost  

---

##  Python

1. **Limpieza de Datos**  
   - Manejo de valores nulos y duplicados.  
   - Normalización de fechas y formatos monetarios.  
   - Corrección de errores tipográficos en nombres de campañas y ubicaciones.  

---

## SQL

Ejemplos de queries implementadas:

```sql
-- Top 5 campañas por ROAS
SELECT campaign, SUM(revenue) / SUM(cost) AS ROAS
FROM campaigns
GROUP BY campaign
ORDER BY ROAS DESC
LIMIT 5;

-- CTR promedio por canal
SELECT channel, SUM(clicks) * 1.0 / SUM(impressions) AS CTR
FROM campaigns
GROUP BY channel;
```
---

## Dashboard en Power BI

El dashboard incluye:

### KPIs principales
- CTR (Click Through Rate)  
- CPC (Cost per Click)  
- CPA (Cost per Acquisition)  
- ROAS (Return on Ad Spend)  

### Visualizaciones
- Evolución temporal de CTR y CPA  
- Comparación de campañas por ROAS  
- Funnel de conversión (Impresiones → Clicks → Conversiones)  
- Distribución del presupuesto por dispositivo  

---

#  Insights

- **ROAS de 0,08** → por cada dólar invertido, la campaña solo genera **7,5 centavos**, lo que la hace **no rentable**.  
- El **CTR promedio fue de 3%**, lo que indica espacio para mejorar la segmentación o la creatividad de los anuncios.  
- El **CPA promedio se mantuvo en torno a $300–$345**, sin grandes variaciones entre dispositivos.  
- El **funnel de conversión muestra un cuello de botella crítico**: solo el **0,1% de las impresiones terminan en conversiones**, evidenciando una gran pérdida de eficiencia.  
- La **distribución de costos** es similar en desktop, mobile y tablet, pero ninguna plataforma logra compensar el bajo rendimiento global.  

---

# Feedback y Recomendaciones

- **Auditar la campaña** para revisar segmentación, copy y creatividad de anuncios.  
- **Mejorar la tasa de clics (CTR)** con creatividades más relevantes y una mejor selección de keywords.  
- **Reducir el CPA** optimizando landings y simplificando el proceso de conversión.  
- **Reestructurar la inversión publicitaria**: el ROAS actual no justifica el gasto, se recomienda redistribuir el presupuesto hacia campañas o canales más rentables.  
- Considerar **pruebas A/B** para validar hipótesis de mejora en segmentación, anuncios y páginas de destino.  

---

# Recursos

- Dataset: [Google Ads Sales Dataset – Kaggle]([https://www.kaggle.com/datasets/nayakganesh007/google-ads-sales-dataset/data](https://www.kaggle.com/datasets/nayakganesh007/google-ads-sales-dataset))  

---

# Autor

**Giuliano Gambino**  
[LinkedIn](https://www.linkedin.com/in/giulianogambino/) 


