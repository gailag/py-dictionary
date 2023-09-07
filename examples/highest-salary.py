#two tables, Worker and Title
#find the worker title that earns the highest salary

import pandas as pd

#changing the column name
title_worker_id = title.rename(columns =
{'worker_ref_id':'worker_id'})

#merging the tables with the fk 'id'
merge_df = pd.merge(worker, title_worker_id, on = 'worker_id')

#checks the max salary
merged_df['salary'].max()

# Get max salary
rows_with_max_salary = merged_df[merged_df['salary'] ==
merged_df['salary'].max()]

result = rows_with_max_salary['worker_title']
