with users as (
    select user_id 
    from user_info
    where joined like '2021%'
)
select year(o.sales_date) as year, month(o.sales_date) as month,
count(distinct o.user_id) as purchased_users,
round(count(distinct o.user_id)/(select count(*) from users),1) 
as purchased_ratio
from users as u
join online_sale as o
on o.user_id=u.user_id
group by 1,2
order by 1,2