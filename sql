-- Top 10 Components by Average Failure Probability
SELECT
    component,
    ROUND(AVG(failure_probability_pct), 2) AS avg_failure_probability
FROM powertrain_failure_profile
GROUP BY component
ORDER BY avg_failure_probability DESC
LIMIT 10;

-- Severity Distribution
SELECT
    severity,
    COUNT(*) AS total_failures
FROM powertrain_failure_profile
GROUP BY severity
ORDER BY total_failures DESC;

-- Average Repair Cost by Component
SELECT
    component,
    ROUND(AVG(repair_cost_inr), 2) AS avg_repair_cost
FROM powertrain_failure_profile
GROUP BY component
ORDER BY avg_repair_cost DESC;
