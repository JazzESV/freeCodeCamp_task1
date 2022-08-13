
def arithmetic_arranger(problems, display_answer=False):
    errors_count = []
    line = ''
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for i in range(len(problems)):
        first_v, symbol, second_v = problems[i].split()
        print(first_v, symbol, second_v)
        # if len(errors_count) <= 5:
        if str(symbol) == '*' or str(symbol) == '/':
            errors_count += ['symbol_error']
            print(errors_count)
            # print("Error: Operator must be '+' or '-'.")
        if first_v.isdigit() == False or second_v.isdigit() == False:
            errors_count += ['isdigit_error', 'isdigit_error'] if first_v.isdigit() == False and second_v.isdigit() == False else ['isdigit_error']
            print(errors_count)
            # print ("Error: Numbers must only contain digits.")
        if len(first_v) > 4 or len(second_v) > 4:
            errors_count += (['len_error', 'len_error']) if len(first_v) > 4 and len(second_v) > 4 else ['len_error']
            print(errors_count)
        if len(errors_count) <= 5:
            error_result = []
            if 'symbol_error' in set(errors_count):
                x = 'Error: Operator must be ''+'' or ''-''.'
                error_result.append(x)
            if 'isdigit_error' in set(errors_count):
                y = 'Error: Numbers must only contain digits.'
                error_result.append(y)
            if 'len_error' in set(errors_count):
                z = 'Error: Numbers cannot be more than four digits.'
                error_result.append(z)
            for error in error_result:
                line += f'{error}\n'
            print(line.rstrip())
        if len(errors_count) > 5:
            print('Error: Too many problems.')
                # print ("Error: Numbers cannot be more than four digits.")
            # if len(errors_count) <= 5 and ['symbol_error'] in errors_count and ['isdigit_error'] in errors_count and ['len_error'] in errors_count:
            #     print('Error: Operator must be '+' or '-'.\nError: Numbers must only contain digits.\nError: Numbers cannot be more than four digits.')
            # if len(errors_count) <= 5 and ['symbol_error'] in errors_count and ['isdigit_error'] in errors_count:
            #     print('Error: Operator must be '+' or '-'.\nError: Numbers must only contain digits.')
            # if len(errors_count) <= 5 and ['symbol_error'] in errors_count and ['len_error'] in errors_count:
            #     print('Error: Operator must be '+' or '-'.\nError: Numbers cannot be more than four digits.')
            # if len(errors_count) <= 5 and ['isdigit_error'] in errors_count and ['len_error'] in errors_count:
            #     print('Error: Operator must be '+' or '-'.\nError: Numbers must only contain digits.\nError: Numbers cannot be more than four digits.')
        # if len(errors_count) > 5:
        #     print ("Error: Too many problems.")
    #     max_str_lenght = max(len(first_v), len(second_v)) + 2
    #     space1 = (max_str_lenght - len(first_v)) * ' '
    #     if i < len(problems) - 1:
    #         line1 += space1 + first_v + 4 * ' '
    #         space2 = (max_str_lenght - len(second_v) - 1) * ' '
    #         line2 += symbol + space2 + second_v + 4 * ' '
    #         line3 += max_str_lenght * '-' + 4 * ' '
    #         answer = eval(first_v + symbol + second_v)
    #         space3 = (max_str_lenght - len(str(answer))) * ' '
    #         line4 += space3 + str(answer) + 4 * ' '
    #     else:
    #         line1 += space1 + first_v
    #         space2 = (max_str_lenght - len(second_v) - 1) * ' '
    #         line2 += symbol + space2 + second_v
    #         line3 += max_str_lenght * '-'
    #         answer = eval(first_v + symbol + second_v)
    #         space3 = (max_str_lenght - len(str(answer))) * ' '
    #         line4 += space3 + str(answer)
    # if display_answer == True:
    #     print(f'{line1}\n{line2}\n{line3}\n{line4}')
    # else:
    #     print(f'{line1}\n{line2}\n{line3}')

arithmetic_arranger(['x / 111111111', ], True)
