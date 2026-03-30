with fish as (
    select id, fish_type, case
    when length is null then 10
    else length end as length
    from fish_info
)
select count(*) as fish_count, max(length) as max_length,fish_type
from fish
group by fish_type
having avg(length)>=33
order by 3