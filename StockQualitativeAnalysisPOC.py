#TODO:
#1. Scrape daily news related to stock from any website(intially try using headlines as dataset, then entire news content)
#2. For training dataset: try taking last 7-8 years of data
#3. using NLP, extract the stock name and stock symbol from each news
#4. so data will have 3 columns: dateOfNews, stockName, news
#5. Find the percentage grown/decline in stock in the next trading session (if morning news then same day, else next trading day)
#6. Create 4 classification labels: 
#   Very positive(growth greater than 3%), 
#   positive (growth: close>open), 
#   negative (decline: open>close), 
#   very negative (decline greater than 3%)
# Use different classication models in ML to see which gives best result
# Use gridsearchCV for hypertuning the parameters of each of these models
# For evaluation in test and training sets we can use confusion matrix