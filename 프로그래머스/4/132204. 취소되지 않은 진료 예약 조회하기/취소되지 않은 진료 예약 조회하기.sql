select a.apnt_no, p.pt_name,a.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd from appointment as a
join patient as p 
on a.pt_no=p.pt_no
join doctor as d
on d.dr_id=a.mddr_id
where a.apnt_ymd like '2022-04-13%' and a.mcdp_cd='CS' and a.apnt_cncl_yn='N'
order by 6 asc