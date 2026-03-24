with recursive gen as (
    select id, parent_id, 1 as depth
    from ecoli_data
    where parent_id is null
    
    union all
    
    select c.id,c.parent_id, p.depth+1 depth
    from gen as p
    join ecoli_data as c
    on c.parent_id=p.id
    
    
)

select count(g.id) as COUNT, g.depth as GENERATION
from gen as g
left join ecoli_data as c
on g.id=c.parent_id
where c.id is null
group by g.depth
order by g.depth