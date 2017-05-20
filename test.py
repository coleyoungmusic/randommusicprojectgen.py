num = int(input('Please enter a number: '))

if num == 0:  # this eliminates this condition

    print('This is not a prime number')

elif num == 1:  # this eliminates this condition

    print('This is not a prime number.')

elif num > 1:  # if number is greater than 1 program checks for factors

    for x in range(2, num):

        if num % x == 0:
            print(num, 'is not a prime number.')

            break

    else:

        print(num, 'is a prime number.')
