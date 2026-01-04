select p.id, count(c.id) as child_count from ecoli_data c 
right join ecoli_data p 
on c.parent_id=p.id
group by p.id
order by p.id
