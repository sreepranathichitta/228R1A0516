# Function to generate binary numbers from 1 to n
def generatePrintBinary(n):
    for i in range(1, n + 1):
        str = ""
        temp = i
        # Convert decimal number to binary number
        while temp:
            if temp & 1:
                str = "1" + str
            else:
                str = "0" + str
            temp >>= 1  # Right shift the bits of temp by 1 position
        print(str)


n = 10

# Function call
generatePrintBinary(n)