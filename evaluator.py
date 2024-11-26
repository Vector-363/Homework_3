

def evaluate_expression(expression):

    try:
        exec(f"result = {expression}")
        return
    except (NameError, SyntaxError, TypeError):
        return "Ошибка вычисления выражения"
