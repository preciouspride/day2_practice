# To read a file:
# 1 => Open the file: You have to tell python exactly where the file is:
#   i. => Using an absolute path to the file (How to get to the file starting from the root directory) "cd c:\users\ni_mo\Documents\workspace\day2_practice\....."
#   ii. => Using the relative path to the file (How to get to the file starting from the current directory) "cd ..\day2_practice\.." | "cd day2_practice\.."
# 2 => Tell python how to open the file:
#   i. => Open in readonly mode: r
#   ii. => Open in write only mode: w
#   iii. => Open in append only mode: a
#   iv  => Open in read and write mode

# Buffering

#How to open a file.
# The function to open a file is called open. It takes the path to the file + the mode to open with as arguments
file = open('exchange.csv', 'a')
print(file.closed)
print(file.mode)
file.close()
print(file.closed)