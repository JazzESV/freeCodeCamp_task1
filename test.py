x = ['Error: Operator must be "+" or "-".', 'Error: Numbers must only contain digits.', 'Error: Numbers cannot be more than four digits.']
line = ''
for error in x:
    line += f'{error}\n'
print(line.rstrip())