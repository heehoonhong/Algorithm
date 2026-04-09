with recursive parent as (
    select id,parent_id, 1 as depth from ecoli_data
    where parent_id is null
    
    union all
    
    select e.id, e.parent_id, p.depth+1 from ecoli_data as e
    join parent as p
    on p.id=e.parent_id
)

select count(*) as count, depth as generation from parent as p
left join ecoli_data as e
on p.id=e.parent_id
where e.parent_id is null
group by generation
order by generation