def main():
    total = 0

    numbers = [0] * 5
    for i in range(5):
        numbers[i] = int(input('Enter a value: '))
        total = total + numbers
        i += 1
    """
    ########################################
    Code Your Program here
    ########################################
    """
    # the list of number value is initialized to whatever * 5 to hold 5 inputs


    # total = sum(numbers)
    print(total)
    print(numbers)

    ########################################
    # Do not delete the return statement
    ########################################
    return total, numbers


if __name__ == '__main__':
    main()
