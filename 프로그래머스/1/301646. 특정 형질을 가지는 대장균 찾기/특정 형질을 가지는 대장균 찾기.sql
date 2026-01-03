select count(*) as count from ecoli_data
where genotype & 2 =0 and genotype & 5>0