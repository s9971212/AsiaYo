## 資料庫測驗  
#### 題目一  
答案：  
```
SELECT b.id AS bnb_id,
       b.name AS bnb_name,
       SUM(o.amount) AS may_amount
FROM bnbs b
JOIN orders o ON b.id = o.bnb_id
WHERE o.created_at >= '2023-05-01' AND o.created_at <= '2023-05-31'
  AND o.currency = 'TWD'
GROUP BY b.id, b.name
ORDER BY may_amount DESC
LIMIT 10;
```
  
#### 題目二  
答案：  
1. 索引優化：可以在bnb_id, created_at, currency上加上索引以加快SQL在JOIN和WHERE時的執行速度，例如  
```
CREATE INDEX idx_bnb_id ON orders(bnb_id);
CREATE INDEX idx_created_at ON orders(created_at);
CREATE INDEX idx_currency ON orders(currency);
```
  
2. 查詢語句優化：可以的話**盡量避免**在SUM裡面使用CASE語法，例如  
```
SELECT b.id AS bnb_id,
       b.name AS bnb_name,
       SUM(CASE WHEN o.currency = 'TWD' THEN o.amount ELSE 0 END) AS may_amount
```
  
## API 實作測驗  
#### 題目一  
答案：  
SOLID原則(僅列出有使用到的原則)  
單一職責原則：每個類別只負責一個功能（驗證或轉換）。  
開放封閉原則：類別應該容易擴展但不修改，方便添加新功能。  
失敗：  
![image](https://github.com/s9971212/AsiaYo/blob/85b652c0fcd266dead2bed574e6f2dc4532d7650/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-07-19%20223828.png)
成功：  
![image](https://github.com/s9971212/AsiaYo/blob/85b652c0fcd266dead2bed574e6f2dc4532d7650/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-07-19%20223907.png)
