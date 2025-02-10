select datetime from animal_ins
where datetime=
(select MIN(datetime) from animal_ins)