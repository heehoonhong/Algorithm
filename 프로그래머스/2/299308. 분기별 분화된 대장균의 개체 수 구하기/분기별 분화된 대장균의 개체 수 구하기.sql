select
case 
when month(differentiation_date) <4 then '1Q'
when month(differentiation_date) <7 then '2Q'
when month(differentiation_date) < 10 then '3Q'
when month(differentiation_date) <=12 then '4Q'
end as quarter,count(*) as ecoli_count
from ecoli_data
group by quarter
order by quarter