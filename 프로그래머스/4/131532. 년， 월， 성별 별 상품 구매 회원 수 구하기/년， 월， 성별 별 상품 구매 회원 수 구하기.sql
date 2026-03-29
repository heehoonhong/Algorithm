with s as (
    select year(o.sales_date) as year, month(o.sales_date) as month, 
    u.gender, u.user_id 
    from user_info as u
    join online_sale as o
    on u.user_id=o.user_id
    
    
)
select year,month,gender,count(distinct user_id) as users from s
where gender is not null
group by 1,2,3
order by year,month,gender
