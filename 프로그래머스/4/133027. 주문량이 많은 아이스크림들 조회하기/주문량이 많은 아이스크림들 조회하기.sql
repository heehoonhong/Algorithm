with s as (
    select j.shipment_id, h.flavor, h.total_order+ sum(j.total_order) as o1 
    from first_half as h
    join july as j
    on j.flavor=h.flavor
    group by flavor
    order by o1 desc
    limit 3
)

select flavor from s