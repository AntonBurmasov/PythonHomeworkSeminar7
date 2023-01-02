import rational
import complex
import view
import logger



def button_click():
    choice = view.choice_number_class()
    if not choice:
        a = view.get_value()
        b = view.get_value()
        c = view.get_value()
        d = view.get_value()
        action = view.get_operation()
        rational.init(a, b, c, d)
        result = rational.do_it(action)
        view.view_data(result, 'результат')
        data = f'{rational.return_x()} {action} {rational.return_y()} = {result}'
        logger.log(str(data))
    else:
        a = int(view.get_value())
        b = int(view.get_value())
        c = int(view.get_value())
        d = int(view.get_value())
        action = view.get_operation()
        complex.init(a, b, c, d)
        result = complex.do_it(action)
        view.view_data(result, 'результат')
        data = f'{complex.return_x()} {action} {complex.return_y()} = {result}'
        logger.log(str(data))

