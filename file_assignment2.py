#Read the contents of exchange.csv file and write just the exchange for each date to a new file called rates.txt. Each exchange should be on its own line.
#For days where there is no exchange, put 0.
#The output should be to 3 decimal places, with trailing zeroes 1.234, 1.200
#Example out
#1.099
#1.812

#Hint, you can open two files at the same time with content managers like below
# with open('file1', 'r') as f1:
#   with open('file2', 'w') as f2:
#       var = f1.read()
#       f2.write(var)

file_name = "exchange.csv"

with open("exchange.csv") as input_file:
    with open("rates.txt", "a") as output_file:
            headers = next(input_file)
            for line in input_file:
                exchange = line.split(',')[1]
                exchange = exchange.strip()
                try:
                    exchange = float(exchange)
                except ValueError:
                    exchange = 0
                # Write the exchange to the output file
                output_file.write(str(f'{exchange:.3f}')+"\n")