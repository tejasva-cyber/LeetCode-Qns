WITH Consecutive AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
ValidGroups AS (
    SELECT grp
    FROM Consecutive
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT c.id, c.visit_date, c.people
FROM Consecutive c
JOIN ValidGroups v ON c.grp = v.grp
ORDER BY c.visit_date;