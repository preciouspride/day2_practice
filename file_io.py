# To read a file:
# 1 => Open the file: You have to tell python exactly where the file is:
#   i. => Using an absolute path to the file (How to get to the file starting from the root directory) "cd c:\users\ni_mo\Documents\workspace\day2_practice\....."
#   ii. => Using the relative path to the file (How to get to the file starting from the current directory) "cd ..\day2_practice\.." | "cd day2_practice\.."
# 2 => Tell python how to open the file:
#   i. => Open in readonly mode: r
#   ii. => Open in write only mode: w
#   iii. => Open in append only mode: a
#   iv  => Open in read and write mode

## DRY => Don't Repeat Yourself

# Buffering

#How to open a file.
# The function to open a file is called open. It takes the path to the file + the mode to open with as arguments
# try:
#     file = open('exchange.csv', 'r+')

#     # print("Is file closed: ", file.closed)
#     # print("What is the mode the file is open with: ", file.mode)
#     # print("Is file readable: ", file.readable())
#     # print("Is file writable: ", file.writable())
#     # file.close()
#     # print("Is file closed: ", file.closed)


#     #readlines is a method on the file handler that reads all the content of the file and stores it in memory
#     # content = file.readlines()
#     # file.close()

#     # for line in content:
#     #     print(line, end="")


#     heading = next(file)
#     print(heading, end="")
#     for _ in range(10):
#         print(next(file), end="")
#         raise(ValueError)
# except ValueError:
#     print("There was an error")

# finally:
#     print("Closing the file right now!!")
#     file.close()
#     print("File is now closed: ", file.closed)


## An even easier way to ensure that the files get closed after using them is by using a Context Manager
# To work with a context manager, you enter a context manager using a "with" statement.

# with open('exchange.csv') as file:
#     heading = next(file)
#     print(heading, end="")
#     for _ in range(10):
#         print(next(file), end="")
## Continue work

# Use a context manager to open the file in read mode and print out the first 10 lines

with open('exchange.csv') as file:
    heading = next(file)
    print(heading, end="")
    for _ in range(10):
        print(next(file), end="")