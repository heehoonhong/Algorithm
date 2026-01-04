select id, 
case when size_of_colony between 0 and 100 then 'LOW'
when size_of_colony between 100 and 1000 then 'MEDIUM'
when size_of_colony >=1000 then 'HIGH'
end as size
from ecoli_data
order by id