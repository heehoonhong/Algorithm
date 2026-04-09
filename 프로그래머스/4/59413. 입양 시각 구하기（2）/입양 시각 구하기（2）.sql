with recursive hours as (
    select 0 as hour 
    union all
    select hour+1 from hours
    where hour<23

)
select hour, count(animal_id) as count from hours
left join animal_outs on hour=hour(datetime)
group by hour
order by hour
