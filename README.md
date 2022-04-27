# Project for SSD 

## Setup 

1. Crate database with schema
```sql
sqlite3 data.db < sample.schema
```
2. open database
```sql
sqlite3 db.sqlite3
``` 
3. Load data in to database
```sql
.mode csv
.import data/Car.sales.csv car
.import data/customer.csv customer
```

# DOMAIN MODEL
![image](https://user-images.githubusercontent.com/70503441/165564786-7f81a688-37ef-4e99-b1e5-d8a5ba79d3d9.png)
