select c.id as id from ecoli_data as p
join ecoli_data as c
on p.id=c.parent_id
where p.parent_id is not null and p.parent_id in 
(select id from ecoli_data  where parent_id is null)
order by id asc
