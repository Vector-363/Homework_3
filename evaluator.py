import ast

def evaluate_expression(expression, context):
    try:
        tree = ast.parse(expression, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ['__import__', 'eval', 'exec']:
                return "Ошибка: Запрещенная функция"
        code = compile(tree, '<string>', 'eval')
        result = eval(code, {}, context)
        return result
    except (NameError, SyntaxError, TypeError, ValueError) as e:
        return f"Ошибка вычисления выражения: {e}"



