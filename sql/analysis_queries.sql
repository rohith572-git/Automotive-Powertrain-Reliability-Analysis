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

-- 4 Which components fail most often?
SELECT component,
       COUNT(*) AS failure_count
FROM powertrain_failure_profile_final_pgadmin
GROUP BY component
ORDER BY failure_count DESC;
 
--5 Top 10 most failure-prone components
select component,
	   count(*) as failures
from powertrain_failure_profile_final_pgadmin
group by component
order by failures desc
limit 10;

-- 6 Components with highest failure probability
SELECT component,
       round(AVG(failure_probability_pct),2) AS avg_probability
FROM powertrain_failure_profile_final_pgadmin
GROUP BY component
ORDER BY avg_probability DESC;

-- 7 Components with highest High severity failures
select component,count(*)as total
from powertrain_failure_profile_final_pgadmin
where severity='High'
group by component 
order by total desc;

-- 8 Most expensive components
SELECT distinct component,
       repair_cost_range_inr
FROM powertrain_failure_profile_final_pgadmin
ORDER BY repair_cost_range_inr DESC;

-- 9 Which powertrain has the most failure records?
select powertrain_id,count(*) as failures
from powertrain_failure_profile_final_pgadmin
group by powertrain_id 
order by failures desc;

-- 10 High severity failures by powertrain
select powertrain_id,count(*) as total 
from powertrain_failure_profile_final_pgadmin
where severity ='High'
group by powertrain_id
order by total desc;

-- 11 Components with High Severity AND High Probability
select component,severity,failure_probability_pct 
from powertrain_failure_profile_final_pgadmin
where severity='High' and failure_probability_pct >=8
order by failure_probability_pct desc;

-- 12 Most reliable powertrains
select powertrain_id,round(avg(failure_probability_pct),2) as avg_failure
from powertrain_failure_profile_final_pgadmin
group by powertrain_id
order by avg_failure desc
limit 10;
