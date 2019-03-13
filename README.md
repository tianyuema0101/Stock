# Stock
This is a simple django backend server for 61 financial coding test. It contains python scripts to get and store stock data from initrino to MySQL database. The django Restful Framework is used to get the list of stock according to code, start date and end date. It also contains the algorithm to calculate the max profit during a period and present the line chart.

Function:
1. Get and store stock price data from initrino
 /import_stock_data/import_stock.py

2. Get the list of stock according to code, start date and end date.
 url:http://127.0.0.1:8000/stock/
 doc url: http://127.0.0.1:8000/docs/
 
3. Get the max profit:
 url:http://127.0.0.1:8000/input_page/ (error due to no input validation)
 
 这是一个简单的Django后端程序，用于申请61 Financial工作。 其中包含python脚本来通过API获取数据存储于MySQL数据库，其中运用了DRF的功能来通过code,开始时间，结束时间来获取一段时间的某个股票close price. 并且其包含一个计算一段时间最大利润的功能和数据可视化。
 
 
 
