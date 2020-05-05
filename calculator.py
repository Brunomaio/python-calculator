def presentResults(result):
    print('-- The result is: ', result)
    print('-------------')


def add(x, y):
    result = int(x) + int(y)
    presentResults(result)


def subtract(x, y):
    result = int(x) - int(y)
    presentResults(result)


def multiply(x, y):
    result = int(x) * int(y)
    presentResults(result)


def divide(x, y):
    result = float(x) / float(y)
    presentResults(result)


calculating = True
while calculating:
    print('- Select operation type:')
    print('---- sum')
    print('---- subtract')
    print('---- multiply')
    print('---- divide')
    print('-- exit program')
    userChoice = input('Waiting for input... ')
    print(userChoice, 'operation')
    print('-------------')
    if userChoice == 'sum':
        add(input('1st number: '), input('2nd number: '))
        userChoice = ''
    elif userChoice == 'multiply':
        multiply(input('1st number: '), input('2nd number: '))
    elif userChoice == 'divide':
        divide(input('1st number: '), input('2nd number: '))
    elif userChoice == 'subtract':
        subtract(input('1st number: '), input('2nd number: '))
    elif userChoice == 'exit program' or 'exit':
        calculating = False
    else:
        print('Sorry, that option isn`t available:', userChoice)
