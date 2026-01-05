with most as(
    select board_id,views from used_goods_board
    order by views desc
    limit 1
)

select concat('/home/grep/src/',u.board_id,'/',u.file_id,u.file_name,u.file_ext) as file_path
from used_goods_file u
join most m 
on u.board_id=m.board_id
order by u.file_id desc