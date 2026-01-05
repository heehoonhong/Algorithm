with emp as (
    select dept_id,round(avg(sal),0) as salary from hr_employees
    group by dept_id
)

select d.dept_id, d.dept_name_en, p.salary as avg_sal from hr_department d
join emp p on d.dept_id=p.dept_id
order by avg_sal desc