from evaluator import evaluate_expression
import re

def parse_config(yaml_data, context={}, is_top_level=True):
    for key, value in yaml_data.items():
        if not isinstance(value, str) or not value.startswith("!"):
            context[key] = value

    result = ""
    for key, value in yaml_data.items():
        if isinstance(value, dict):
            result += f"$[\n{parse_config(value, context, False)}\n]\n" # обработка словарей
        elif isinstance(value, list):
            items = [str(item) for item in value]
            result += f"array({', '.join(items)})\n" # обработка массивов
        elif isinstance(value, str) and value.startswith("!"):
            try:
                res = evaluate_expression(value[1:], context)
                if isinstance(res, str) and "Ошибка" in res:
                    raise ValueError(res)
                result += f"{key} is {res}\n" # обработка константных вычислений
            except ValueError as e:
                raise ValueError(f"Ошибка вычисления выражения '{value}': {e}")
        elif isinstance(value, str) and re.match(r"^\s*'", value):
            continue
        elif is_top_level:
            continue
        else:
            result += f"{key} is {value}\n" # обработка констант

    return result.strip()