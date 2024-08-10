import csv

with open('nasdaq_screener.csv', 'r') as file:
    reader = csv.DictReader(file)
    for column in reader:
        if "Country" in column:
            country = column["Country"]
        if "Sector" in column:
            sector = column["Sector"]
        if "Industry" in column:
            industry = column["Industry"]
    
        if "Symbol" in column:
            stock = column["Symbol"]
            if country == "United States" and sector == "Technology" and industry == "Semiconductors":
                print(stock)
        else:
            print("Symbol not found in selection range.")