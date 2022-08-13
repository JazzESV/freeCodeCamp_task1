
def arithmetic_arranger(problems, display_answer=False):
    errors_count = 0
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for i in range(len(problems)):
        first_v, symbol, second_v = problems[i].split()
        print(first_v, symbol, second_v)
        if errors_count <= 5:
            if str(symbol) == '*' or str(symbol) == '/':
                errors_count += 1
                print(errors_count)
                print("Error: Operator must be '+' or '-'.")
            if first_v.isdigit() == False or second_v.isdigit() == False:
                errors_count += 2 if first_v.isdigit() == False and second_v.isdigit() == False else 1
                print(errors_count)
                print ("Error: Numbers must only contain digits.")
            if len(first_v) > 4 or len(second_v) > 4:
                errors_count += 2 if len(first_v) > 4 and len(second_v) > 4 else 1
                print(errors_count)
                print ("Error: Numbers cannot be more than four digits.")
            if errors_count > 5:
                print(errors_count)
                print ("Error: Too many problems.")
        # try:
        #     x, y = int(first_v), int(second_v)
        # except ValueError:
        #     print(errors_count)
        #     print ("Error: Numbers must only contain digits.")
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
        print(f'{line1}\n{line2}\n{line3}\n{line4}')
    else:
        print(f'{line1}\n{line2}\n{line3}')

arithmetic_arranger(['1 / 2', '3801 / 3', '15 * 43', '123 + 49'], True)
