SELECT TOP 5
    Campaign_Name,
    SUM(Sale_Amount) AS total_revenue,
    SUM(Cost) AS total_cost,
    SUM(Sale_Amount) / NULLIF(SUM(Cost), 0) AS roas
FROM
    Sheet1$
GROUP BY
    Campaign_Name
ORDER BY
    roas DESC;

SELECT
    Device,
    SUM(Clicks) * 1.0 / NULLIF(SUM(Impressions), 0) AS avg_ctr
FROM
    Sheet1$
GROUP BY
    Device;

SELECT
    Ad_Date,
    SUM(Cost) / NULLIF(SUM(Conversions), 0) AS cpa
FROM
    Sheet1$
GROUP BY
    Ad_Date
ORDER BY
    Ad_Date;