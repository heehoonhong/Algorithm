with new_grade as (
    select emp_no, avg(score) as score from hr_grade
    group by emp_no
),

s  as (
    select e.emp_no, e.emp_name,g.score,e.sal, case
    when score>=96 then 'S'
    when score>=90 then 'A'
    when score>=80 then 'B'
    else 'C' end as grade
    from hr_employees as e
    join new_grade as g
    on g.emp_no=e.emp_no
)

select emp_no,emp_name,grade, case
when grade='S' then sal*0.2
when grade='A' then sal*0.15
when grade='B' then sal*0.1
else 0 end as bonus
from s
order by 1