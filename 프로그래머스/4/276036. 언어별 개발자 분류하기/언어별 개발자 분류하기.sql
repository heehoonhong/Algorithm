with s as (
    select case
    when d.skill_code& (select code from skillcodes where name='Python') =
    (select code from skillcodes where name='Python') 
    and d.skill_code& 
    (select sum(code) from skillcodes where category='Front End') >0
     then 'A'
    when d.skill_code& (select code from skillcodes where name='C#')=
    (select code from skillcodes where name='C#') then 'B'
    when d.skill_code&
    (select sum(code) from skillcodes where category='Front End')>0
    then 'C' 
    
    
    
    end as grade,
    d.id, d.email from developers as d

)
select * from s
where grade is not null
order by grade,id