with b_sales as (
    select book_id, sales from book_sales
    where year(sales_date)=2022 and month(sales_date)=1
)
select b.category, sum(s.sales) as total_sales from book b
join b_sales s 
on b.book_id=s.book_id
group by b.category
order by b.category
