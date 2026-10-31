WITH ThreatMatrix AS (
    SELECT 
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS shared_signature_count,
        COUNT(*) OVER(PARTITION BY lat, lon) AS location_collision_count
    FROM Insurance
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM ThreatMatrix
WHERE shared_signature_count > 1 
  AND location_collision_count = 1;