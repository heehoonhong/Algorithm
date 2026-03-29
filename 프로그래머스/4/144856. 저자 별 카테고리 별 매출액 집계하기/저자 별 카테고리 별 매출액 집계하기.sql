select a.author_id, a.author_name, b.category, sum(bs.sales*b.price) as total_price  from book as b

join book_sales as bs 
on b.book_id=bs.book_id
join author as a
on a.author_id=b.author_id
where sales_date like '2022-01%'
group by a.author_id, b.category
order by 1 asc, 3 desc
