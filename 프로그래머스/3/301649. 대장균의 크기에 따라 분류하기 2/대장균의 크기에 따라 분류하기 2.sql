with most as (
    select id,
    percent_rank() over (order by size_of_colony desc) as pr
    from ecoli_data
)

select id, case
when pr>0.75 then 'LOW'
when pr>0.5 then 'MEDIUM'
when pr>0.25 then 'HIGH'
else 'CRITICAL' end as colony_name
from most order by id