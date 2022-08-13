# По сравнению с изначальным заданием данный код не только фиксирует типы ошибок, но и по-разному раегирует на их количество.
# Если общее количество ошибок меньше пяти, то выводятся сообщения по каждой уникальной ошибке,
# если количество ошибок больше пяти, то выводится сообщение "Error: Too many problems.".

def arithmetic_arranger(problems, display_answer=False):
    errors_count = []
    error_result = []
    error_message = ''
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for i in range(len(problems)):
        first_v, symbol, second_v = problems[i].split()
        if str(symbol) == '*' or str(symbol) == '/':
            errors_count += ['symbol_error']
        if first_v.isdigit() == False or second_v.isdigit() == False:
            errors_count += ['isdigit_error', 'isdigit_error'] if first_v.isdigit() == False and second_v.isdigit() == False else ['isdigit_error']
        if len(first_v) > 4 or len(second_v) > 4:
            errors_count += (['len_error', 'len_error']) if len(first_v) > 4 and len(second_v) > 4 else ['len_error']
        if 'symbol_error' in errors_count:
            x = 'Error: Operator must be ''+'' or ''-''.'
            error_result.append(x)
        if 'isdigit_error' in errors_count:
            y = 'Error: Numbers must only contain digits.'
            error_result.append(y)
        if 'len_error' in errors_count:
            z = 'Error: Numbers cannot be more than four digits.'
            error_result.append(z)
        if 0 < len(error_result) <= 5:
            for error in error_result:
                error_message += f'{error}\n'
            print(error_message.rstrip())
        if len(error_result) > 5:
            print('Error: Too many problems.')
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

# Тестовый пример
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)