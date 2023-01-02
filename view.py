def view_data(data, title):
    print(f'{title} = {data}')

def choice_number_class():
    return int(input('Введите 0 для работы с рациональными числами, любое другое число - для работы с комплексными числами'))

def get_value():
    return input('значение =  ')

def get_operation():
    print('Выберите операцию: + - * /')
    return input('Операция: ')