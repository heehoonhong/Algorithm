select ANIMAL_TYPE,COUNT(*) AS COUNT
from animal_ins
group by ANIMAL_TYPE
order by ANIMAL_TYPE