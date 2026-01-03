select count(user_id) as users from user_info
where age between 20 and 29 and age is not null and year(joined)=2021