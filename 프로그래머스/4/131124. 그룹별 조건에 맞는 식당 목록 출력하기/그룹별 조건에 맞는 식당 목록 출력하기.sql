with s as (
    select member_id,count(member_id) as cnt from rest_review
    group by member_id
    
)
select m.member_name,r.review_text,date_format(r.review_date,'%Y-%m-%d')  as review_date
from rest_review as r
join member_profile as m
on m.member_id=r.member_id
where m.member_id in (
    select member_id from s
    where cnt= (
        select max(cnt) from s
    )
)
order by 3 asc, 2 asc
