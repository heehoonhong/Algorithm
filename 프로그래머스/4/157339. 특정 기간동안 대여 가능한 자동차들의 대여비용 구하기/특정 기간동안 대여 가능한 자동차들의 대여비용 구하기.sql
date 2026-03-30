# 2022 11월 1일부터 30일까지 대여 가능한 car_id
with able as (
    select car_id from car_rental_company_car
    where car_id not in (
        select car_id from car_rental_company_rental_history
        where datediff('2022-11-01',end_date)<0
    )
    and car_type in ('세단','SUV')
),
plan as (
    select car_type, discount_rate from car_rental_company_discount_plan
    where car_type in ('세단','SUV') and duration_type = '30일 이상'
)

select c.car_id,c.car_type,
round(c.daily_fee*30*(100-p.discount_rate)/100,0) as fee 
from car_rental_company_car as c
join plan as p
on c.car_type=p.car_type
where car_id in (select car_id from able) and
round(c.daily_fee*30*(100-p.discount_rate)/100,0)>=500000 and
round(c.daily_fee*30*(100-p.discount_rate)/100,0)<2000000
order by 3 desc,2,1 desc