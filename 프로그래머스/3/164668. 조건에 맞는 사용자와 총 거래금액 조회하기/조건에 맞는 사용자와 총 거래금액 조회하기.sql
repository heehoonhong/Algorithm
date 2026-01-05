with done as (
    select writer_id, price from used_goods_board
    where status='DONE'
)

select u.user_id, u.nickname, sum(d.price) as total_price from done d
join used_goods_user u
on u.user_id = d.writer_id
group by d.writer_id
having total_price>=700000
order by 3