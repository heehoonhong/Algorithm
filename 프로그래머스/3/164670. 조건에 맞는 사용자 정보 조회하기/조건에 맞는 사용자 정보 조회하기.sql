select u.user_id, nickname, 
concat(city,' ',street_address1,' ',street_address2) as 전체주소,
concat(substring(tlno,1,3),'-',substring(tlno,4,4),'-',substring(tlno,8,4))
as 전화번호 
from used_goods_user as u
join used_goods_board as b
on u.user_id=b.writer_id
group by u.user_id
having count(writer_id)>=3
order by 1 desc