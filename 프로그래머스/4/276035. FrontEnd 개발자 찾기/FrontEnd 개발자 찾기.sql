with s as (
    select sum(code) as target_code from skillcodes
    where category='Front End'
)


select id, email,first_name, last_name 
from developers 
where skill_code&(select target_code from s)>0
order by 1
