select floor(price/10000)*10000 as PRICE_GROUP, count(*) as PRODUCTS
from PRODUCT
GROUP BY PRICE_GROUP
order by PRICE_GROUP asc