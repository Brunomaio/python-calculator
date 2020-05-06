def presentResults(result):
    print('-- The result is:', result)
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
    if userChoice == 'sum' or userChoice == 'add':
        add(input('1st number: '), input('2nd number: '))
    elif userChoice == 'multiply' or userChoice == 'mult':
        multiply(input('1st number: '), input('2nd number: '))
    elif userChoice == 'divide':
        divide(input('1st number: '), input('2nd number: '))
    elif userChoice == 'subtract' or userChoice == 'subtraction':
        subtract(input('1st number: '), input('2nd number: '))
    elif userChoice == 'exit program' or userChoice == 'exit':
        calculating = False
    else:
        print('Sorry, the option ', userChoice, 'is not available')
        print('-------------')
