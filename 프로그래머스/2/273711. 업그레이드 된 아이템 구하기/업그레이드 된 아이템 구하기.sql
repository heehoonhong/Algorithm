with iip as (
    select item_id from item_info 
    where rarity='RARE'

)

select ii.item_id,ii.item_name,ii.rarity from item_info ii
join item_tree it on ii.item_id=it.item_id
join iip on iip.item_id=it.parent_item_id

order by ii.item_id desc