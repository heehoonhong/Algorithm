with car as (
    select car_id, start_date,end_date, case 
    when '2022-10-16' between start_date and end_date then 1 
    else 0 end as re
    from car_rental_company_rental_history
)
select car_id,case 
when sum(re)>0 then '대여중'
else '대여 가능' end as availability
from car
group by car_id
order by car_id desc