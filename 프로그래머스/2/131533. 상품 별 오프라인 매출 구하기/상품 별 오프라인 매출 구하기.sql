select p.product_code as PRODUCT_CODE,SUM(p.price*os.sales_amount) as SALES
from product as p
join offline_sale as os
on p.product_id=os.product_id
group by p.product_code
order by sales desc,product_code asc
