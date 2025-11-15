# Prompt user for pattern size
size= int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    # Use for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")       
    print() # Move to the next line after completing the row
    
    row += 1 