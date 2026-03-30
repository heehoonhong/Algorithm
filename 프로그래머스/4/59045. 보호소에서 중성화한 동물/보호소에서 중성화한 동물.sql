# 중성화를 거치지 않은 동물은 Intact,
# 중성화를 거친 동물은 Spayed 또는 Neutered
select i.animal_id, i.animal_type, i.name
from animal_ins as i
join animal_outs as o
on i.animal_id=o.animal_id
where i.sex_upon_intake like 'Intact%' and 
(o.sex_upon_outcome like 'Spayed%' or o.sex_upon_outcome like 'Neutered%')
