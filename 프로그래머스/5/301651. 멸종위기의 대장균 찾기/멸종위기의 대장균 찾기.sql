with recursive gen as (
    select id,parent_id,1 as depth from ecoli_data 
    where parent_id is null

    union all
    
    select c.id,c.parent_id, p.depth+1 as depth from gen as p
    join ecoli_data as c
    on c.parent_id = p.id
)

select count(*) as count, p.depth as generation from gen as p
left join ecoli_data as c
on c.parent_id=p.id
where c.id is null
group by depth
order by depth