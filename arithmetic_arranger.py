# Решение изначальной задачи
def arithmetic_arranger(problems, display_answer=False):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for i in range(len(problems)):
        first_v, symbol, second_v = problems[i].split()
        if len(problems) > 5:
            return "Error: Too many problems."
        if str(symbol) == '*' or str(symbol) == '/':
            return "Error: Operator must be '+' or '-'."
        if first_v.isdigit() == False or second_v.isdigit() == False:
            return "Error: Numbers must only contain digits."
        if len(first_v) > 4 or len(second_v) > 4:
            return "Error: Numbers cannot be more than four digits."
        max_str_lenght = max(len(first_v), len(second_v)) + 2
        space1 = (max_str_lenght - len(first_v)) * ' '
        if i < len(problems) - 1:
            line1 += space1 + first_v + 4 * ' '
            space2 = (max_str_lenght - len(second_v) - 1) * ' '
            line2 += symbol + space2 + second_v + 4 * ' '
            line3 += max_str_lenght * '-' + 4 * ' '
            answer = eval(first_v + symbol + second_v)
            space3 = (max_str_lenght - len(str(answer))) * ' '
            line4 += space3 + str(answer) + 4 * ' '
        else:
            line1 += space1 + first_v
            space2 = (max_str_lenght - len(second_v) - 1) * ' '
            line2 += symbol + space2 + second_v
            line3 += max_str_lenght * '-'
            answer = eval(first_v + symbol + second_v)
            space3 = (max_str_lenght - len(str(answer))) * ' '
            line4 += space3 + str(answer)
    if display_answer == True:
        arranged_problems = f'{line1}\n{line2}\n{line3}\n{line4}'
    else:
        arranged_problems = f'{line1}\n{line2}\n{line3}'
    return arranged_problems