select hg.score, he.emp_no, he.emp_name, he.position, he.email from hr_employees as he
join (
select emp_no, sum(score) as score from hr_grade 
    where year=2022 group by emp_no
) hg
on he.emp_no=hg.emp_no
order by hg.score desc
limit 1