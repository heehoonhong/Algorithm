with duration_car as (
    select car_id, datediff(end_date,start_date)+1 as duration
    from car_rental_company_rental_history
)

select car_id,round(avg(duration),1) as average_duration from duration_car

group by car_id
having round(avg(duration),1)>=7
order by average_duration desc, car_id desc
