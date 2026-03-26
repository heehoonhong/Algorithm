with car as (
    select cc.car_id, cc.car_type,cc.daily_fee,rh.history_id,
    datediff(rh.end_date,rh.start_date)+1 as df,
    case
    when datediff(rh.end_date,rh.start_date)+1>=90 then '90일 이상'
    when datediff(rh.end_date,rh.start_date)+1>=30 then '30일 이상'
    when datediff(rh.end_date,rh.start_date)+1>=7 then '7일 이상'
    else '할인 없음' end as dis_rate
    from car_rental_company_car as cc
    join car_rental_company_rental_history as rh
    on cc.car_id=rh.car_id
    where cc.car_type='트럭'
)

select history_id, round(df*daily_fee*(100-ifnull(dp.discount_rate,0))/100,0) as fee
from car
left join car_rental_company_discount_plan as dp
on dp.duration_type=car.dis_rate and dp.car_type='트럭'
order by 2 desc, 1 desc