with per_rank as (
    select id, percent_rank() over (order by size_of_colony desc) as per
    from ecoli_data
)

select id,
case when per <= 0.25 then 'CRITICAL'
when per <= 0.5 then 'HIGH'
when per <= 0.75 then 'MEDIUM'
when per <= 1 then 'LOW'
end as colony_name
from per_rank
order by id