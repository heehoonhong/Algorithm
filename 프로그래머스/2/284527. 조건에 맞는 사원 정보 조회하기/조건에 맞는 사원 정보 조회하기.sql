select T.TOTAL_SCORE AS SCORE ,E.EMP_NO,E.EMP_NAME,E.POSITION,E.EMAIL
from HR_EMPLOYEES AS E
join (
    select EMP_NO, SUM(SCORE) AS TOTAL_SCORE
    from HR_GRADE
    where YEAR=2022
    group by EMP_NO
) T
on E.EMP_NO=T.EMP_NO
order by SCORE desc
limit 1
