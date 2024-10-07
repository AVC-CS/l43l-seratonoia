def main():
    total = 0

    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a value: '))
    print(numbers)

    for j in (numbers):
        total += j
    print (total)       
        
    """
    ########################################
    Code Your Program here
    ########################################
    """
    # the list of number value is initialized to whatever * 5 to hold 5 inputs
    # try using another variable to keep track of the numbers
    # total = sum(numbers)
    # display the lis tof numbers first, then display the sum of them
    # initialize adding to total = 0
    ########################################
    # Do not delete the return statement
    ########################################
    return total, numbers


if __name__ == '__main__':
    main()
