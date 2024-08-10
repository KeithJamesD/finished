import csv

with open("nasdaqlisted.csv", "a") as file:
    stock = input("Symbol: ")
    writer = csv.writer(file)  # Define the writer object
    reader = csv.reader(file) # Define the reader object

    a = writer.writerow([stock, "Market Category"])  # Write the data row
print(a)
file.close()