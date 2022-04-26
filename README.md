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