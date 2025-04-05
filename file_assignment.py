# Read the contents of exchange.csv

# 1. print out the exchange rate to 2 decimal places for each line. Do Bankers rounding for the decimals (HALF_EVEN rounding)
# 2. if there is no exchange rate for a particular date, just print 0.0

file_name = "exchange.csv"

with open(file_name) as file:
    headers = next(file)
    for line in file:
        exchange = line.split(',')[1]
        exchange = exchange.strip()
        try:
            exchange = float(exchange)
        except ValueError:
            exchange = 0
        # exchange = round(exchange)
        # print("{:.2f}".format(exchange))
        # print(f'{exchange:.2f}')
        with open('rates.txt', 'a') as output:
            output.write(str(exchange))
            output.write("\n")