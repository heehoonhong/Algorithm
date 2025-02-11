select MCDP_CD AS 진료과코드, COUNT(*) AS 5월예약건수
from appointment
where year(apnt_ymd)=2022 and month(apnt_ymd)=5
group by 1
order by 2,1