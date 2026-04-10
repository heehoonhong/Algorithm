with most as (
    select id,
    ntile(4) over (order by size_of_colony desc) as nt
    from ecoli_data
)

select id, case
when nt=1 then 'CRITICAL'
when nt=2 then 'HIGH'
when nt=3 then 'MEDIUM'
else 'LOW' end as COLONY_NAME
from most 
order by id