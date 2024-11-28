import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def multiply(sum_numbers):
    result = 0
    for sum_number in sum_numbers:
        result *= sum_number
    return result

actions = [
    ('+', '1', 'addition',          lambda lambda_numbers: sum(lambda_numbers)),
    ('-', '2', 'subtraction',       lambda lambda_numbers: lambda_numbers[0] - lambda_numbers[1]),
    ('*', '3', 'multiplication',    lambda lambda_numbers: multiply(lambda_numbers)),
    ('/', '4', 'division',          lambda lambda_numbers: lambda_numbers[0] / lambda_numbers[1]),
]

def select_action(selected):
    for action in actions:
        if selected == action[1] or selected == action[2]:
            return action
    logging.error(f'Invalid action! ({selected})')
    exit(0)

def is_subtraction_or_division(selected):
    return selected == actions[1] or selected == actions[3]

def is_number(typed):
    if not typed.isnumeric():
        logging.error(f'{typed} is not a number!')
        exit(0)

print('actions:')
for action in actions:
    print(f'\t{action[1]}. {action[2]}')

selectedAction = select_action(input('\nSelect action: '))
numbers = []
for x in range(1, 3) if is_subtraction_or_division(selectedAction) else range(1, 101):
    number = input(f'Please type {x} number{" or 'exit'" if x > 2 else ""}: ')
    while selectedAction == actions[3] and x == 2 and number == '0':
        number = input('You can not divide by 0, please re-type number: ')
    if x > 2 and number.upper() == 'EXIT':
        break
    is_number(number)
    numbers.append(int(number))

logging.info(f'Selected action: "{selectedAction[2]}" for numbers {numbers}. The result is {selectedAction[3](numbers)}')
